# Training DACTYL Classifiers

## Installation

Install requirements:

```shell
pip install -r requirements.txt
```

## Example Usage

Here is an example JSON config file. 
```json
{
    "training_split": "training",
    "evaluation_split": "testing",
    "results_path": "tpauc-debertav3-large.csv",
    "num_epochs": 1,
    "model_path": "microsoft/deberta-v3-large",
    "tokenizer": "microsoft/deberta-v3-large",
    "optimizer": "SOTAs",
    "optimizer_type": "libauc",
    "optimizer_args": {
        "lr": 1e-05
    },
    "loss_fn": "tpAUC_KL_Loss",
    "reset_classification_head": false,
    "loss_type": "libauc",
    "loss_fn_args": {
        "data_len": 466005
    },
    "needs_loss_fn_as_parameter": false,
    "save_path": "USERNAME/dactyl-deberta-v3-large-finetuned",
    "training_args": {
        "batch_size": 16,
        "needs_sampler": true,
        "needs_index": true,
        "shuffle": false,
        "sampling_rate": 0.5,
        "apply_sigmoid": true
    },
    "best_model_path": "best-debertav3-model-tpauc",
    "eval_batch_size": 8
}

```
To train your detector with your own config, run:
```shell
python train_detector.py --config=PATH/TO/JSON
```

To evaluate your detector with your own dataset, run:
```shell
python evaluate_detector.py --parquet_path=PATH/TO/DATASET --model=PATH/TO/MODEL --tokenizer=PATH/TO/TOKENIZER
```