import dotenv
import os
dotenv.load_dotenv()

from huggingface_hub import login, HfApi
login(token=os.environ["HF_TOKEN"])
api = HfApi()


import pandas as pd
import libauc.losses
import libauc.optimizers
from libauc.metrics import pauc_roc_score
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sklearn.metrics import average_precision_score, roc_auc_score
from lightning_libauc.trainer import LibAUCTrainer
import torch.nn 
import torch.optim
import json

import torch
torch.set_float32_matmul_precision('high')
import numpy as np
from libauc.utils import set_all_seeds

import argparse

def train_and_evaluate_model(training_args):
    domain = "complete"
    print("training for", domain)
    training_split = training_args["training_split"]
    evaluation_split = training_args["evaluation_split"]
    model_path = training_args["model_path"]
    tokenizer_name  = training_args["tokenizer"]
    loss_type = training_args["loss_type"]
    optimizer_type = training_args["optimizer_type"]
    num_epochs = training_args["num_epochs"]
    print("Training model", model_path, "with loss function", training_args["loss_fn"])
    print("Optimizing model with", training_args["optimizer"] )
    file_prefix_path = "dactyl-data"
    training_df = pd.read_parquet(f"{file_prefix_path}/{domain}_training.parquet")
    validation_df = pd.read_parquet(f"{file_prefix_path}/{domain}_validation.parquet")
    testing_df = pd.read_parquet(f"{file_prefix_path}/{domain}_testing.parquet")
    
    #training_df = training_df.sample(1000)
    training_df = training_df.reset_index()
    
    print(training_df["target"].value_counts(normalize=True))
    print(training_df["target"].value_counts())
    
    #validation_df = validation_df.sample(1000)
    validation_df = validation_df.reset_index()
    
    #testing_df = testing_df.sample(1000)
    testing_df = testing_df.reset_index()
    
    
    model = AutoModelForSequenceClassification.from_pretrained(model_path, num_labels=1)    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    if training_args.get("reset_classification_head", False):
        for layer in model.classifier.modules():
            if hasattr(layer, 'reset_parameters'):
                layer.reset_parameters()
                print("Parameters reset for:", layer)
        #model.classifier.reset_parameters()
    
    if optimizer_type == "libauc":
        loss_ = getattr(libauc.losses, training_args["loss_fn"])
        loss_fn = loss_(**training_args["loss_fn_args"])
        optimizer_ = getattr(libauc.optimizers, training_args["optimizer"])
        if training_args["needs_loss_fn_as_parameter"]:
            optimizer = optimizer_(model.parameters(), loss_fn=loss_fn, **training_args["optimizer_args"])
        else:
            optimizer = optimizer_(model.parameters(), **training_args["optimizer_args"])
    else:
        loss_ = getattr(torch.nn, training_args["loss_fn"])
        loss_fn = loss_(**training_args["loss_fn_args"])
        optimizer_ = getattr(torch.optim, training_args["optimizer"])
        optimizer = optimizer_(model.parameters(),**training_args["optimizer_args"])
    
    local_best_path = training_args["best_model_path"]
    training_params = training_args["training_args"]
    model.save_pretrained(local_best_path)
    eval_batch_size = training_args.get("eval_batch_size", 64)
    trainer = LibAUCTrainer(model, tokenizer, loss_fn, optimizer, needs_sampler=training_params["needs_sampler"], needs_index=training_params["needs_index"], device="cuda", seed=2025)
    results = trainer.evaluate(validation_df, "text","target", eval_batch_size)
    max_fpr = 0.05
    min_tpr = 0.80
    best_pauc_roc_score = pauc_roc_score(results["target"], results["prediction"], max_fpr=max_fpr, min_tpr=min_tpr)
    print(best_pauc_roc_score)
    best_pauc_roc_score = -1.0 
    for epoch in range(num_epochs):
        trainer.train(training_df, 1, training_params["batch_size"], "text","target",shuffle=training_params["shuffle"], sampling_rate=training_params["sampling_rate"], apply_sigmoid=training_params["apply_sigmoid"])
        results = trainer.evaluate(validation_df, "text","target", eval_batch_size)
        print("AP Score:", average_precision_score(results["target"], results["prediction"]))
        print("AUC Score:", roc_auc_score(results["target"], results["prediction"]))
        print("pAUC Score:", roc_auc_score(results["target"], results["prediction"], max_fpr=max_fpr))
        print("tpAUC Score:", pauc_roc_score(results["target"], results["prediction"], max_fpr=max_fpr, min_tpr=min_tpr))
        pauc_score = pauc_roc_score(results["target"], results["prediction"], max_fpr=max_fpr, min_tpr=min_tpr)
        print(f"Epoch {epoch+1} tpauc_score:", pauc_score)
        if best_pauc_roc_score < pauc_score:
            best_pauc_roc_score = pauc_score
            model.save_pretrained(local_best_path)
            print("Saved best model!")
            
    # load best model
    model = AutoModelForSequenceClassification.from_pretrained(local_best_path, num_labels=1)  
    model.push_to_hub(training_args["save_path"],private=True)
    
    results = trainer.evaluate(testing_df, "text","target", eval_batch_size)
    
    results["model"] = testing_df["model"].to_list()
    print("AP Score:", average_precision_score(results["target"], results["prediction"]))
    print("AUC Score:", roc_auc_score(results["target"], results["prediction"]))
    print("pAUC Score:", roc_auc_score(results["target"], results["prediction"], max_fpr=max_fpr))
    print("tpAUC Score:", pauc_roc_score(results["target"], results["prediction"], max_fpr=max_fpr, min_tpr=min_tpr))
    human_texts = results[results.target == 0]
    results.to_csv(training_args["results_path"],index=False)
    scores = list()
    for model_name, sf in results.groupby("model"):
        if model_name == "human":
            continue
        sf = pd.concat([human_texts, sf])
        ap_score = average_precision_score(sf["target"], sf["prediction"])
        auc_score = roc_auc_score(sf["target"], sf["prediction"])
        pauc_score = roc_auc_score(sf["target"], sf["prediction"],max_fpr=max_fpr)
        tppauc_score = pauc_roc_score(sf["target"], sf["prediction"], max_fpr=max_fpr, min_tpr=min_tpr)
        scores.append(
            {
                "model": model_name, 
                "AP Score": ap_score,
                "AUC Score": auc_score,
                "OPAUC Score": pauc_score,
                "TPAUC Score": tppauc_score
            }
        )
    scores.append({
        "model": "overall",
        "AP Score": average_precision_score(results["target"], results["prediction"]),
        "AUC Score": roc_auc_score(results["target"], results["prediction"]),
        "OPAUC Score": roc_auc_score(results["target"], results["prediction"], max_fpr=max_fpr),
        "TPAUC Score": pauc_roc_score(results["target"], results["prediction"], max_fpr=max_fpr, min_tpr=min_tpr),
    })
    markdown_string = pd.DataFrame(scores).to_markdown(index=False)
    training_config_string = json.dumps(training_args, indent=4)
    with open("README.md",'w+') as f:
        f.write("---\nlibrary_name: transformers\ntags: []\n---\n")
        f.write(f"# DACTYL Text Detector\n")
        f.write(f"## Training Configuration\n```json\n{training_config_string}\n```\n")
        f.write(f"## Results\n{markdown_string}\n")
    
    api.upload_file(
        path_or_fileobj="README.md",
        path_in_repo="README.md",
        repo_id=training_args["save_path"],
        repo_type="model",
    )



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",type=str)
    
    args = parser.parse_args()
    
    with open(args.config,'r') as f:
        training_args = json.load(f)
    
    
    set_all_seeds(2025)
    train_and_evaluate_model(training_args)
