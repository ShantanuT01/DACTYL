# Finetuning-Parameter-Search

Source code on initial parameter searching and generating texts. 
## Setup for Finetuning Parameter Search

Make an .env file with your HuggingFace token to access private and gated models.

```
HF_TOKEN="SECRET_KEY_GOES_HERE"
```

File paths should be inspected and modified before running code. 

We arrived at temperature = 1.1, top_p = 1, and top_k = 100. 
The results folder is intentionally empty due to out of date results. 

## Setup for Generation

We provide a sample generation usage:
```json
{
    "domain": "RedditWritingPrompts",
    "split": "training",
    "repetition_penalty": 1.0,
    "temperature": 1.1,
    "top_p": 1.0,
    "top_k": 100.0
}
```
Then run:
```
python generate_texts.py --config_path=PATH/TO/JSON --data_path=PATH/TO/JSON/TEXTS
```

