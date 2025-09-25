from huggingface_hub import login
import os
from dotenv import load_dotenv

load_dotenv()
login(token=os.environ["HF_TOKEN"])
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from libauc.metrics import pauc_roc_score
from sklearn.metrics import average_precision_score, roc_auc_score

from tqdm import tqdm
import pandas as pd
import argparse


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--parquet_path",type=str)
    parser.add_argument("--tokenizer",type=str)
    parser.add_argument("--model",type=str)
    parser.add_argument("--use_fast",type=str, default="true")
    args = parser.parse_args()
    testing_frame = pd.read_parquet(args.parquet_path)
    if args.use_fast == "true":
        tokenizer = AutoTokenizer.from_pretrained(args.tokenizer)
    else:
        print("using slow tokenizer")
        tokenizer = AutoTokenizer.from_pretrained(args.tokenizer, use_fast=False)
    model = AutoModelForSequenceClassification.from_pretrained(args.model)
    
    pipe = pipeline("text-classification", model=model,tokenizer=tokenizer )
    
    def data():
        for text in testing_frame["text"].values:
            yield text
    y_pred = list()
    for result in tqdm(pipe(data(),batch_size=64, max_length=512,truncation=True, return_all_scores=True), total=len(testing_frame)):
        for output in result:
            if output["label"] == "LABEL_0":
                y_pred.append(output["score"])
    
    model_output_path = args.model.split("/")[-1]
    
    # %% [code] {"execution":{"execution_failed":"2025-05-28T21:27:06.752Z"}}
    testing_frame["prediction"] = y_pred
    max_fpr = 0.05
    min_tpr = 0.8
    testing_frame[["id","prediction","target","model","domain","category","dataset"]].to_csv(f"predictions/{model_output_path}-results.csv",index=False)
    scores = list()
    for dataset, sf in testing_frame.groupby("dataset"):
        ap_score = average_precision_score(sf["target"], sf["prediction"])
        auc_score = roc_auc_score(sf["target"], sf["prediction"])
        pauc_score = roc_auc_score(sf["target"], sf["prediction"],max_fpr=max_fpr)
        tppauc_score = pauc_roc_score(sf["target"], sf["prediction"], max_fpr=max_fpr, min_tpr=min_tpr)
        scores.append(
            {
                "dataset": dataset, 
                "AP Score": ap_score,
                "AUC Score": auc_score,
                "OPAUC Score": pauc_score,
                "TPAUC Score": tppauc_score
            }
        )
    scores.append({
        "dataset": "overall",
        "AP Score": average_precision_score(testing_frame["target"], testing_frame["prediction"]),
        "AUC Score": roc_auc_score(testing_frame["target"], testing_frame["prediction"]),
        "OPAUC Score": roc_auc_score(testing_frame["target"], testing_frame["prediction"], max_fpr=max_fpr),
        "TPAUC Score": pauc_roc_score(testing_frame["target"], testing_frame["prediction"], max_fpr=max_fpr, min_tpr=min_tpr),
    })
    pd.DataFrame(scores).to_markdown(f"predictions/{model_output_path}.md", index=False)
    print(pd.DataFrame(scores).to_markdown(index=False))