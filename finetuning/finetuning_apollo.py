import dotenv
import os
dotenv.load_dotenv()

from huggingface_hub import login
login(token=os.environ["HF_TOKEN"])
os.environ["WANDB_DISABLED"] = "true"
import argparse
import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForLanguageModeling, set_seed


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain")
    parser.add_argument("--split")
    args = parser.parse_args()
    
    set_seed(2025)
    domain = args.domain
    split = args.split
    model_name = "meta-llama/Llama-3.2-1B-Instruct"
    parquet_path = f"finetuning_data/{domain}_finetuning_{split}.parquet"
    parquet_path_test = f"finetuning_data/{domain}_finetuning_testing.parquet"
    df = pd.read_parquet(parquet_path)
    # Sanity check
    print(df["text"].values[10])

    tokenizer = AutoTokenizer.from_pretrained(model_name, device_map="auto")

    

    if "text" not in df.columns:
        raise ValueError('The CSV file must contain a "text" column.')
    

    dataset = Dataset.from_pandas(df)
    test_dataset = Dataset.from_pandas(pd.read_parquet(parquet_path_test))

    
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    # Tokenize the dataset
    def tokenize_function(examples):
        tokens = tokenizer(
            examples["text"],
            padding="max_length",
            truncation=True,
            max_length=512
        )
        return tokens
    
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, 
        mlm=False  
    )
    
    tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=["text"])
    tokenized_test_dataset = test_dataset.map(tokenize_function, batched=True, remove_columns=["text"])

    training_args = TrainingArguments(
        output_dir=f"./fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-{domain}-{split}",
        eval_strategy="epoch",
        learning_rate=1e-4,
        per_device_train_batch_size=8,
        num_train_epochs=1,
        weight_decay=0.001,
        save_total_limit=2,
        warmup_steps=45,
        gradient_accumulation_steps=4,
        optim="apollo_adamw",
        optim_target_modules=[r".*.attn.*", r".*.mlp.*"],
        optim_args="proj=random,rank=1,scale=128.0,scale_type=tensor,update_proj_gap=200",
        fp16=True,
        hub_private_repo=True,
        save_strategy="no"
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        eval_dataset=tokenized_test_dataset,
        data_collator=data_collator
    )
    
    trainer.train()
    trainer.push_to_hub()
