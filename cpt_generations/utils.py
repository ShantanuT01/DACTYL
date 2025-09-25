from constants import *
from transformers import pipeline
import tqdm
import pandas as pd
from sklearn.metrics import roc_auc_score, average_precision_score
from collections import Counter
import numpy as np

def generate_fine_tuned_continuation_prompts(texts, num_tokens, tokenizer):
    prompts = list()
    for text in texts:
        token_ids = tokenizer(text, return_tensors="pt")["input_ids"][0][0:num_tokens]
        prompt = tokenizer.decode(token_ids, skip_special_tokens=True)
        prompts.append(prompt)
    return prompts




def generate_texts_from_parameters(pipe, model_name, domain,split,human_texts, start_tokens, max_new_tokens, repetition_penalty,top_k, top_p, temperature ):

    prompts = generate_fine_tuned_continuation_prompts(human_texts, start_tokens, pipe.tokenizer)

    def return_prompts():
        for prompt in prompts:
            yield prompt
    fine_tuned_texts = list()
    for result in tqdm.tqdm(pipe(return_prompts(),max_length=max_new_tokens + start_tokens, repetition_penalty=repetition_penalty,top_k=top_k, top_p=top_p, temperature=temperature, batch_size=2), total=len(prompts)):
        output = result[0]["generated_text"]
        fine_tuned_texts.append(output)
    output_frame = pd.DataFrame({PROMPT: prompts, TEXT: fine_tuned_texts,"source_text": human_texts})
    output_frame[TARGET] = 1
    output_frame[DOMAIN] = domain
    output_frame[TEMPERATURE] = temperature
    output_frame[TOP_P] = top_p
    output_frame[TOP_K] = top_k
    output_frame[REPETITION_PENALTY] = repetition_penalty
    output_frame[SPLIT] = split
    output_frame[MODEL] = model_name
    return output_frame

def generate_text_from_parameters_dynamic_max_length(maximum_tokens_to_gen, pipe, model_name, domain, split, human_texts, repetition_penalty, top_k, top_p, temperature):
    frames = list()
    human_index = 0
    for max_tokens in maximum_tokens_to_gen:
        num_gens = maximum_tokens_to_gen[max_tokens]
        start_tokens = max_tokens//3
        max_new_tokens = max_tokens - start_tokens
        temp_frame = generate_texts_from_parameters(pipe, model_name, domain, split, human_texts[human_index:human_index+num_gens], start_tokens, max_new_tokens, repetition_penalty, top_k, top_p, temperature)
        frames.append(temp_frame)
        human_index += num_gens
    return pd.concat(frames)

def evaluate_by_group(columns, dataframe_to_group, constant_dataframe):
    results = list()
    groups = dataframe_to_group.groupby(columns)
    for _, subframe in groups:
        test_df = pd.concat([subframe, constant_dataframe])
        entry = dict()
        for column in columns:
            entry[column] = subframe[column].values[0]
        entry[AUC_SCORE] = roc_auc_score(y_score=test_df[SCORE], y_true=test_df[TARGET])
        entry[PAUC_SCORE] =  roc_auc_score(y_score=test_df[SCORE], y_true=test_df[TARGET], max_fpr=0.05)
        entry[AP_SCORE] =  average_precision_score(y_score=test_df[SCORE], y_true=test_df[TARGET])
        results.append(entry)
    return pd.DataFrame(results)



def evaluate_texts(dataframe):
    pipe = pipeline("text-classification", model="yaful/MAGE")
    def data():
        for text in dataframe[TEXT].values:
            yield text
    y_pred = list()
    for result in tqdm.tqdm(pipe(data(),batch_size=32, max_length=512,truncation=True, top_k=None), total=len(dataframe)):
        for output in result:
            if output["label"] == 0:
                y_pred.append(output[SCORE])
    dataframe[SCORE] = y_pred
    return dataframe

 
def count_llama_tokens(texts, tokenizer):
    token_counts = list()
    for text in tqdm.tqdm(texts):
        k = tokenizer.tokenize(text)
        token_counts.append(len(k))
    token_counts.sort()
    lqr = np.percentile(token_counts, 25)
    uqr = np.percentile(token_counts, 75)
    start_index = token_counts.index(lqr)
    stop_index = len(token_counts) - 1 - token_counts[::-1].index(uqr)
    token_counts = token_counts[start_index: stop_index + 1]
    counter = Counter(token_counts)
    max_tokens = list()
    counts = list()
    total = sum(counter.values())
    for elem in counter:
        max_tokens.append(elem)
        counts.append(counter[elem]*1.0/total)
    return {
        MAX_TOKENS: max_tokens,
        PROBABILITIES: counts
    }
