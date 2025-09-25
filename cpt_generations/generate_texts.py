from huggingface_hub import login
from dotenv import load_dotenv
import os
load_dotenv()
login(os.environ["HF_TOKEN"])
from transformers import pipeline
import pandas as pd
import torch
import gc
import argparse
from argparse import Namespace
import json
import numpy as np

from utils import *
from constants import *



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_path", type=str)
    parser.add_argument("--data_path",type=str)
    args = parser.parse_args()
    with open(args.config_path, 'r') as f:
        config = json.load(f)
    
    
    config = Namespace(**config)
    domain = config.domain
    split = config.split
    temperature = config.temperature
    top_p = config.top_p
    repetition_penalty = config.repetition_penalty
    top_k = int(config.top_k)
    with open(config.generation_length_config, 'r') as f:
        generation_length_config = json.load(f)

    finetuned_model_name =  f"ShantanuT01/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-{domain}-{split}"
    save_finetuned_texts_path = f"human-length-production/llama-3.2-1b-instruct-finetuned-{domain}-{split}.json"
    vanilla_model_name = "meta-llama/Llama-3.2-1B-Instruct"
    save_vanilla_texts_path = f"human-length-control/llama-3.2-1b-instruct-{domain}-{split}.json"
    all_texts = pd.read_json(args.data_path)
    all_texts = all_texts[all_texts.domain == domain]
    ai_texts = all_texts[all_texts.target == 1]
    human_texts = all_texts[all_texts.target == 0]
    samples_to_draw = len(ai_texts[ai_texts.model == "gpt-4o-mini"])
    human_texts = human_texts.sample(samples_to_draw) 
    human_texts = human_texts[TEXT].to_list()
    finetuned_pipe = pipeline("text-generation", model=finetuned_model_name,device_map="cuda")
    finetuned_pipe.tokenizer.padding_side="left"
    finetuned_pipe.tokenizer.pad_token_id = finetuned_pipe.tokenizer.eos_token_id
    finetuned_pipe.model.generation_config.pad_token_id = finetuned_pipe.tokenizer.pad_token_id
    
    maximum_tokens_to_gen = np.random.choice(generation_length_config[MAX_TOKENS], size=samples_to_draw, p=generation_length_config[PROBABILITIES])
    maximum_tokens_to_gen = Counter(maximum_tokens_to_gen)
    finetuned_frames = list()
    human_index = 0
    
    finetuned_frame = generate_text_from_parameters_dynamic_max_length(maximum_tokens_to_gen, finetuned_pipe, finetuned_model_name, domain, split, human_texts, repetition_penalty, top_k, top_p, temperature)
    finetuned_frame.to_json(save_finetuned_texts_path, orient="records",indent=4, index=False)
    
    del finetuned_pipe
    gc.collect()
    torch.cuda.empty_cache()

    vanilla_pipe = pipeline("text-generation", model=vanilla_model_name,device_map="cuda")
    vanilla_pipe.tokenizer.padding_side="left"
    vanilla_pipe.tokenizer.pad_token_id = vanilla_pipe.tokenizer.eos_token_id
    vanilla_pipe.model.generation_config.pad_token_id = vanilla_pipe.tokenizer.pad_token_id


    vanilla_frame = generate_text_from_parameters_dynamic_max_length(maximum_tokens_to_gen, vanilla_pipe, vanilla_model_name, domain, split, human_texts, repetition_penalty, top_k, top_p, temperature)   
    vanilla_frame.to_json(save_vanilla_texts_path,  orient="records",indent=4, index=False)

    output_frame = pd.concat([finetuned_frame, vanilla_frame])
    del vanilla_pipe
    gc.collect()
    torch.cuda.empty_cache()
    #  evaluate final texts
    output_frame = evaluate_texts(output_frame)
    mage_predictions = pd.read_csv("mage-results.csv")
    mage_predictions[SCORE] = mage_predictions[MAGE_PRED]
    testing_frame = pd.concat([mage_predictions[(mage_predictions.domain == domain)], output_frame])
    human_df = testing_frame[testing_frame.target == 0]
    ai_df = testing_frame[testing_frame.target == 1]
    results = evaluate_by_group([MODEL], ai_df,  human_df)
    results.sort_values(AP_SCORE).to_markdown(f"results/{split}-{domain}.md",index=False)
    print(results.sort_values(AP_SCORE).to_markdown(index=False))
