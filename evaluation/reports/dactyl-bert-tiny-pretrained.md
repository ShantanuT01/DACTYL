# dactyl-bert-tiny-pretrained - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 80.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |    0    |  69.19 | 87.03 | 36.94 |
| test-1b-no-finetuning |    0    |  70.3  | 86.73 | 40.5  |
| test                  |   72.42 |  97.17 | 99.19 | 98.87 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   55.95 |  95.46 | 98.98 | 97.54 |
| abstracts            |   61.19 |  95.93 | 98.78 | 99.21 |
| news                 |   41.11 |  93.96 | 96.83 | 97.58 |
| reviews              |    3.79 |  89.05 | 95.53 | 89.88 |
| student_essays       |    8.29 |  90.26 | 94.83 | 93.11 |
| tweets               |    6.05 |  89.08 | 96.76 | 97.45 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  51.72 | 84.97 |  1.62 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  52.36 | 67.6  |  1.19 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |    0    |  57.46 | 77.62 |  2.15 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |    0    |  62.1  | 79.9  |  2.17 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    0    |  70.3  | 86.73 | 40.5  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    0    |  73.5  | 95.05 | 20.78 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |    0.12 |  82.68 | 94.7  | 38.92 |
| gemini-1.5-pro                                                                     |   22.18 |  91.52 | 97.16 | 86.68 |
| llama-3.2-90b                                                                      |   38.36 |  93.54 | 98.11 | 90.08 |
| gemini-1.5-flash                                                                   |   60.64 |  95.93 | 99.1  | 93.96 |
| gpt-4o-2024-11-20                                                                  |   70.7  |  96.98 | 99.07 | 95.32 |
| llama-3.3-70b                                                                      |   71.73 |  97.09 | 99.3  | 95.6  |
| claude-3-5-haiku-20241022                                                          |   80.48 |  97.99 | 99.5  | 96.95 |
| mistral-large-latest                                                               |   88.42 |  98.81 | 99.7  | 98.14 |
| claude-3-5-sonnet-20241022                                                         |   89.71 |  98.94 | 99.76 | 98.35 |
| DeepSeek-V3                                                                        |   92.26 |  99.21 | 99.73 | 98.73 |
| mistral-small-latest                                                               |   92.44 |  99.22 | 99.75 | 98.83 |
| gpt-4o-mini                                                                        |   96.02 |  99.59 | 99.9  | 99.35 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   88.36 |  98.81 | 99.82 | 99.4  |
| abstracts            |   79.63 |  97.91 | 99.42 | 99.57 |
| news                 |   87.25 |  98.69 | 99.45 | 99.51 |
| reviews              |   56.35 |  95.47 | 98.53 | 96.13 |
| student_essays       |   72.86 |  97.21 | 99.4  | 98.78 |
| tweets               |   45.09 |  94.25 | 98.16 | 98.45 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |   49.44 |  94.8  | 98.14 | 99.58 |
| 538Tweets/lefttroll  |   29.5  |  92.46 | 97.4  | 97.29 |
| 538Tweets/righttroll |   51.88 |  95.02 | 98.34 | 98.21 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   35.26 |  93.03 | 97.42 | 93.69 |
|       2 |   47.6  |  94.59 | 98.21 | 95.24 |
|       3 |   71.91 |  97.03 | 99.28 | 97.79 |
|       4 |   62.76 |  96.17 | 98.96 | 96.89 |
|       5 |   67.32 |  96.65 | 98.58 | 96.87 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   81.4  |  98.09 | 99.63 | 99.71 |
| arxiv/astro-ph.CO        |   88.11 |  98.79 | 99.78 | 99.82 |
| arxiv/astro-ph.GA        |   96.8  |  99.67 | 99.97 | 99.97 |
| arxiv/astro-ph.HE        |   88.91 |  98.85 | 99.73 | 99.8  |
| arxiv/astro-ph.SR        |   88.78 |  98.76 | 99.78 | 99.82 |
| arxiv/cond-mat.mes-hall  |   79.13 |  97.86 | 99.66 | 99.71 |
| arxiv/cond-mat.mtrl-sci  |   84.15 |  98.38 | 99.56 | 99.69 |
| arxiv/cond-mat.stat-mech |   77.12 |  97.64 | 99.26 | 99.49 |
| arxiv/cond-mat.str-el    |   84.07 |  98.37 | 99.52 | 99.61 |
| arxiv/cs.CV              |   72.41 |  97.15 | 99.16 | 99.36 |
| arxiv/gr-qc              |   76.58 |  97.61 | 99.28 | 99.48 |
| arxiv/hep-ph             |   71.4  |  97.07 | 99.08 | 99.35 |
| arxiv/hep-th             |   72.36 |  97.17 | 99.03 | 99.25 |
| arxiv/math.AG            |   74.2  |  97.36 | 99.04 | 99.32 |
| arxiv/math.AP            |   78.83 |  97.84 | 99.51 | 99.63 |
| arxiv/math.CO            |   78.22 |  97.76 | 99.05 | 99.38 |
| arxiv/math.NT            |   69.58 |  96.87 | 98.77 | 99.18 |
| arxiv/math.PR            |   80.84 |  98.05 | 99.49 | 99.63 |
| arxiv/nucl-th            |   73.97 |  97.34 | 99.11 | 99.3  |
| arxiv/quant-ph           |   80.47 |  98    | 99.37 | 99.54 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   90.42 |  99.02 | 99.58 | 99.72 |
| real   |   78.24 |  97.77 | 99.06 | 98.69 |

| topic           |   tpAUC |   pAUC |   AUC |    AP |
|:----------------|--------:|-------:|------:|------:|
| Government News |   86.36 |  98.6  | 99.17 | 99.75 |
| Middle-east     |   97.28 |  99.72 | 99.91 | 99.99 |
| News            |   95.73 |  99.56 | 99.88 | 99.83 |
| US_News         |   86.67 |  98.63 | 99.43 | 99.89 |
| left-news       |   93.16 |  99.3  | 99.77 | 99.82 |
| politics        |   84.2  |  98.38 | 99.14 | 99.09 |
| politicsNews    |   75.1  |  97.45 | 99.02 | 98.57 |
| worldnews       |   81.19 |  98.07 | 99.11 | 98.8  |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| ABC                      |   80.88 |  98.04 | 99.1  | 97.53 |
| NBC                      |   83.01 |  98.26 | 99.28 | 97.96 |
| CNN                      |   83.95 |  98.35 | 99.46 | 98.14 |
| The Times (UK)           |   86.99 |  98.67 | 99.18 | 98.3  |
| The Daily Telegraph (UK) |   88.18 |  98.79 | 99.47 | 98.58 |
| The Sunday Times (UK)    |   90.1  |  98.98 | 99.75 | 98.95 |
| The Guardian (UK)        |   91.48 |  99.13 | 99.51 | 98.85 |
| Fox New                  |   93.42 |  99.33 | 99.87 | 99.36 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |    0    |  85.17 | 93.83 | 90.59 |
| ELLIPSE(Human)+   |   81.73 |  98.12 | 99.06 | 99.46 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |   95.99 |  99.59 | 99.87 | 99.78 |
| Ivy Panda(Human)+ |   78.85 |  97.77 | 99.49 | 97.68 |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |    6.18 |  59.38 | 70.98 |  5.57 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |    6.87 |  60.82 | 68.4  |  8.02 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   18.83 |  66.33 | 78.2  |  4.17 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   21.14 |  68.75 | 79.84 |  5.88 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   34.51 |  75.91 | 82.28 | 37.7  |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   38.67 |  78.16 | 82.47 | 52.82 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   44.86 |  77.99 | 87.33 | 30.73 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   55.95 |  83.42 | 90.87 | 46.13 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   72.45 |  90.16 | 94.4  | 46.16 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   75.15 |  90.99 | 94.32 | 38.17 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   78.73 |  92.25 | 94.86 | 75.11 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   81.32 |  93.23 | 95.67 | 79.33 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ❌       | ✅        | ✅          | ✅     | ✅               | ❌                     |
| Base      | ✅       | ❌        | ❌          | ❌     | ❌               | ✅                     |

