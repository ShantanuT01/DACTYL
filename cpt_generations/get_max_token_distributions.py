from transformers import AutoTokenizer
import argparse
import json
import pandas as pd
from utils import count_llama_tokens
from constants import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain")
    parser.add_argument("--split")
    parser.add_argument("--data_path")
    args = parser.parse_args()
    domain = args.domain
    split = args.split
    data_path = args.data_path
    model_name = f"ShantanuT01/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-{domain}-{split}"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    all_texts = pd.read_json(data_path)
    all_texts = all_texts[all_texts.domain == domain]
    human_texts = all_texts[(all_texts.target == 0)]
    with open(f"configs/{domain}-{split}.json",'w+') as f:
        json.dump(count_llama_tokens(human_texts[TEXT].to_list(), tokenizer), f, indent=4)
