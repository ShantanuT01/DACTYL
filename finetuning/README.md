# Finetuning with APOLLO


## Installation

Install the latest version of transformers from source, then install the requirements:
```shell
pip install git+https://github.com/huggingface/transformers
pip install -r requirements.txt
```

Then set up an `.env` file with your HuggingFace token.

```
HF='YOUR TOKEN'
```

## Example Usage

```shell
python finetuning_apollo.py --domain=tweets --domain=training
```

## Results

You can view the model's README cards to see their results.