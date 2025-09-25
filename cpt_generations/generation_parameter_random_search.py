from huggingface_hub import login
from dotenv import load_dotenv
import os
load_dotenv()
login(os.environ["HF_TOKEN"])
import pathlib
from transformers import AutoTokenizer, pipeline
import pandas as pd
import tqdm
import argparse
from sklearn.model_selection import ParameterSampler
import json
from utils import *
from constants import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain")
    parser.add_argument("--split")
    parser.add_argument("--generation_length_config")
    parser.add_argument("--parameter_combinations_to_test", type=int, default=10)
    parser.add_argument("--sample_texts", type=int, default=50)
    parser.add_argument("--data_path")
    args = parser.parse_args()
    # make directory to save results
    pathlib.Path(f"{args.split}/{args.domain}").mkdir(parents=True, exist_ok=True) 

    domain = args.domain
    split = args.split
    sample_texts = args.sample_texts
    parameter_sample_count = args.parameter_combinations_to_test
    data_path = args.data_path
    with open(args.generation_length_config,'r') as f:
        generation_length_config = json.load(f)
    parameter_grid = {
        TEMPERATURE: [0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9],
        TOP_P:[0.5, 0.6,0.7,0.8,0.9,1.0],
        REPETITION_PENALTY: [1,1.05,1.1,1.15,1.2,1.25,1.3],
        TOP_K :[20,30,40,50,60,70,80,90,100]
    }
    parameter_sampler = list(ParameterSampler(parameter_grid,n_iter=parameter_sample_count, random_state=2025))
    parameter_samples = [dict((k, v) for (k, v) in d.items()) for d in parameter_sampler]
    model_name = f"ShantanuT01/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-{domain}-{split}"
    pipe = pipeline("text-generation", model=model_name,device_map="cuda")
    pipe.tokenizer.padding_side="left"
    pipe.tokenizer.pad_token_id = pipe.tokenizer.eos_token_id
    pipe.model.generation_config.pad_token_id = pipe.tokenizer.pad_token_id
    tokenizer = AutoTokenizer.from_pretrained(model_name)
 

  
    all_texts = pd.read_json(data_path)
    all_texts = all_texts[all_texts.domain == domain]
    human_texts = all_texts[(all_texts.target == 0)]
    ai_texts = all_texts[(all_texts.target == 1)]
    human_texts = human_texts.sample(sample_texts, random_state=2025)[TEXT].to_list()
    maximum_tokens_to_gen = np.random.choice(generation_length_config[MAX_TOKENS], size=len(human_texts), p=generation_length_config[PROBABILITIES])
    maximum_tokens_to_gen = Counter(maximum_tokens_to_gen)
    output_frames = list()
    for parameters in parameter_samples:
        repetition_penalty = parameters[REPETITION_PENALTY]
        temperature = parameters[TEMPERATURE]
        top_k = parameters[TOP_K]
        top_p = parameters[TOP_P]
        output_frame = generate_text_from_parameters_dynamic_max_length(maximum_tokens_to_gen,pipe, model_name, domain, split, human_texts, repetition_penalty, top_k, top_p, temperature)
        output_frames.append(output_frame)
    sample_output_path = f"{split}/{domain}/sample_generations.json"
    pd.concat(output_frames).to_json(sample_output_path,index=False,orient="records",indent=4)
    testing_frame = pd.read_json(sample_output_path)
    
    # run evaluation
    mage_predictions = pd.read_csv("mage-results.csv")
    testing_frame = evaluate_texts(testing_frame)
    mage_predictions[SCORE] = mage_predictions[MAGE_PRED]
    mage_testing_frame = pd.concat([mage_predictions[(mage_predictions.target == 0) & (mage_predictions.domain == domain)], testing_frame])
    human_df = mage_testing_frame[mage_testing_frame.target == 0]
    ai_df = mage_testing_frame[mage_testing_frame.target == 1]
    
    # generation parameter comparison
    generation_results = evaluate_by_group([TEMPERATURE,TOP_P,TOP_K,REPETITION_PENALTY], ai_df, human_df)
    generation_results = generation_results.sort_values(AP_SCORE)
    generation_results.to_markdown(f"{split}/{domain}/parameter_scores.md",index=False)
    temperature = generation_results[TEMPERATURE].values[0]
    top_p = generation_results[TOP_P].values[0]
    top_k = generation_results[TOP_K].values[0]
    repetition_penalty = generation_results[REPETITION_PENALTY].values[0]

    # model comparison
    # only use best generation parameters
    testing_frame = testing_frame[(testing_frame.temperature == temperature) & (top_p == testing_frame.top_p) & (testing_frame.top_k == top_k) & (testing_frame.repetition_penalty == repetition_penalty)]
    testing_frame.to_json(f"{split}/{domain}/best-texts.json",index=False, orient="records",indent=4)
    testing_frame = pd.concat([mage_predictions[(mage_predictions.domain == domain)], testing_frame])
    human_df = testing_frame[testing_frame.target == 0]
    ai_df = testing_frame[testing_frame.target == 1]
    results = evaluate_by_group([MODEL], ai_df, human_df)
    results.sort_values(PAUC_SCORE).to_markdown(f"{split}/{domain}/best_result.md",index=False)
    
    arguments = vars(args)
    del arguments["parameter_combinations_to_test"]
    arguments[REPETITION_PENALTY] = repetition_penalty
    arguments[TEMPERATURE] = temperature
    arguments[TOP_P] = top_p
    arguments[TOP_K] = top_k
    with open(f"{split}/{domain}/args.json",'w+') as f:
        json.dump(arguments, f, indent=4)
    