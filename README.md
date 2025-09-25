# DACTYL: Diverse Adversarial Corpus of Texts Yielded from Large language models

[![arXiv](https://img.shields.io/badge/arXiv-2508.00619-b31b1b.svg)](https://arxiv.org/abs/2508.00619)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-yellow)](https://huggingface.co/collections/ShantanuT01/dactyl-68c66597362bfa4f0f8247f8)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

This repository contains the code and resources for my master's thesis at Cambridge: **DACTYL: Diverse Adversarial Corpus of Texts Yielded from Large language models**. 

## Datasets

- [DACTYL dataset for AI-text detection](https://huggingface.co/datasets/ShantanuT01/DACTYL)
- [DACTYL dataset for continued-pretraining](https://huggingface.co/datasets/ShantanuT01/DACTYL-Pretraining)

## Models

- [DACTYL-trained AI-text detectors](https://huggingface.co/collections/ShantanuT01/dactyl-classifiers-6835e223c98d69430022e0ba)

- [Domain-Specific Llama 3.2 1B Instruct models](https://huggingface.co/collections/ShantanuT01/dactyl-finetuned-slms-680d39faf9ffc6701da11fa0)

## Generating DACTYL

We used the [`dactyl-generation`](https://github.com/ShantanuT01/dactyl_generation/tree/main) package to generate texts. This can be installed via `pip`:

```shell
pip install dactyl-generation
```

## Code

- `finetuning`: Continues pre-training a Llama 3.2 1B Instruct model for a specific domain.
- `baselines`: Contains code to get predictions from existing AI-text detectors on the DACTYL dataset.
- `cpt_generations`: Performs a randomized generation parameter sweep to determine which parameters evade detection better for the Llama 3.2 1B Instruct models.
- `training`: Trains an AI-text classifier.
- `evaluation`: Evaluates DACTYL-trained classifiers.

## Citation

```bibtex
@misc{thorat2025dactyldiverseadversarialcorpus,
      title={DACTYL: Diverse Adversarial Corpus of Texts Yielded from Large Language Models}, 
      author={Shantanu Thorat and Andrew Caines},
      year={2025},
      eprint={2508.00619},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.00619}, 
}

```