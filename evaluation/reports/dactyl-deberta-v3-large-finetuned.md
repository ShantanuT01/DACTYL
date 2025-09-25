# dactyl-deberta-v3-large-finetuned - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 80.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-1b-no-finetuning |   19.02 |  90.6  | 97.25 | 84.8  |
| test-finetuning       |   42.8  |  93.8  | 98.6  | 90.19 |
| test                  |   91.86 |  99.17 | 99.82 | 99.73 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   99.1  |  99.91 | 99.98 | 99.95 |
| abstracts            |   87.75 |  98.74 | 99.69 | 99.8  |
| news                 |   92.67 |  99.25 | 99.69 | 99.77 |
| reviews              |   69.02 |  96.82 | 98.83 | 97.31 |
| student_essays       |   70.91 |  97.01 | 99.37 | 98.88 |
| tweets               |   60.74 |  95.95 | 98.98 | 99.21 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |    AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|-------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  84.71 |  94.94 | 49.1  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |   14.33 |  89.42 |  97.73 | 68.51 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |   19.02 |  90.6  |  97.25 | 84.8  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |   25.69 |  90.32 |  98.35 | 54.72 |
| gemini-1.5-pro                                                                     |   74.59 |  97.38 |  99.44 | 96.03 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |   75.15 |  97.37 |  99.54 | 92.51 |
| llama-3.2-90b                                                                      |   79.12 |  97.85 |  99.51 | 96.75 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |   83.95 |  98.32 |  99.54 | 91.2  |
| claude-3-5-haiku-20241022                                                          |   87.49 |  98.72 |  99.72 | 98.13 |
| gemini-1.5-flash                                                                   |   87.82 |  98.75 |  99.72 | 98.11 |
| gpt-4o-2024-11-20                                                                  |   91.17 |  99.09 |  99.82 | 98.71 |
| llama-3.3-70b                                                                      |   93.83 |  99.37 |  99.88 | 99.08 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |   94.39 |  99.36 |  99.86 | 92.39 |
| claude-3-5-sonnet-20241022                                                         |   98.9  |  99.89 |  99.99 | 99.84 |
| mistral-large-latest                                                               |   98.91 |  99.89 |  99.98 | 99.83 |
| mistral-small-latest                                                               |   99.45 |  99.94 |  99.99 | 99.91 |
| DeepSeek-V3                                                                        |   99.62 |  99.96 | 100    | 99.94 |
| gpt-4o-mini                                                                        |   99.89 |  99.99 | 100    | 99.98 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |    AUC |     AP |
|:---------------------|--------:|-------:|-------:|-------:|
| RedditWritingPrompts |   99.75 |  99.97 |  99.99 |  99.98 |
| abstracts            |   92.65 |  99.25 |  99.8  |  99.85 |
| news                 |   99.84 |  99.98 | 100    | 100    |
| reviews              |   88.26 |  98.8  |  99.57 |  98.92 |
| student_essays       |   95.15 |  99.5  |  99.92 |  99.82 |
| tweets               |   77.26 |  97.67 |  99.41 |  99.49 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |   77.88 |  97.74 | 99.31 | 99.84 |
| 538Tweets/lefttroll  |   68.25 |  96.74 | 99.06 | 98.99 |
| 538Tweets/righttroll |   82.58 |  98.21 | 99.6  | 99.52 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   80.55 |  98.01 | 99.26 | 98.15 |
|       2 |   86.75 |  98.64 | 99.66 | 98.92 |
|       3 |   94.32 |  99.42 | 99.76 | 99.43 |
|       4 |   90.38 |  99.01 | 99.57 | 99.05 |
|       5 |   88.63 |  98.83 | 99.54 | 98.91 |

### Abstracts

| category                 |   tpAUC |   pAUC |    AUC |     AP |
|:-------------------------|--------:|-------:|-------:|-------:|
| arxiv/astro-ph           |   95.68 |  99.56 |  99.86 |  99.9  |
| arxiv/astro-ph.CO        |   97.67 |  99.76 |  99.96 |  99.97 |
| arxiv/astro-ph.GA        |   99.56 |  99.95 | 100    | 100    |
| arxiv/astro-ph.HE        |   97.93 |  99.79 |  99.9  |  99.93 |
| arxiv/astro-ph.SR        |   98.67 |  99.86 |  99.99 |  99.99 |
| arxiv/cond-mat.mes-hall  |   96.07 |  99.6  |  99.95 |  99.96 |
| arxiv/cond-mat.mtrl-sci  |   95.1  |  99.5  |  99.89 |  99.92 |
| arxiv/cond-mat.stat-mech |   92.01 |  99.17 |  99.85 |  99.88 |
| arxiv/cond-mat.str-el    |   93.94 |  99.38 |  99.55 |  99.7  |
| arxiv/cs.CV              |   93.15 |  99.29 |  99.89 |  99.9  |
| arxiv/gr-qc              |   90.95 |  99.07 |  99.59 |  99.72 |
| arxiv/hep-ph             |   86.06 |  98.57 |  99.52 |  99.67 |
| arxiv/hep-th             |   87.47 |  98.72 |  99.56 |  99.65 |
| arxiv/math.AG            |   84.81 |  98.44 |  99.58 |  99.71 |
| arxiv/math.AP            |   92.27 |  99.21 |  99.9  |  99.91 |
| arxiv/math.CO            |   87.6  |  98.72 |  99.75 |  99.8  |
| arxiv/math.NT            |   85.64 |  98.52 |  99.4  |  99.6  |
| arxiv/math.PR            |   94.4  |  99.43 |  99.91 |  99.92 |
| arxiv/nucl-th            |   90.1  |  98.99 |  99.79 |  99.81 |
| arxiv/quant-ph           |   91.75 |  99.16 |  99.74 |  99.81 |

### News

| real   |   tpAUC |   pAUC |   AUC |     AP |
|:-------|--------:|-------:|------:|-------:|
| fake   |   99.96 | 100    |   100 | 100    |
| real   |   99.63 |  99.96 |   100 |  99.99 |

| topic           |   tpAUC |   pAUC |    AUC |     AP |
|:----------------|--------:|-------:|-------:|-------:|
| Government News |   99.86 |  99.99 | 100    | 100    |
| Middle-east     |  100    | 100    | 100    | 100    |
| News            |  100    | 100    | 100    | 100    |
| US_News         |  100    | 100    | 100    | 100    |
| left-news       |   99.9  |  99.99 | 100    | 100    |
| politics        |   99.96 | 100    | 100    | 100    |
| politicsNews    |   98.8  |  99.88 |  99.99 |  99.97 |
| worldnews       |  100    | 100    | 100    | 100    |

| news_outlet              |   tpAUC |   pAUC |    AUC |     AP |
|:-------------------------|--------:|-------:|-------:|-------:|
| The Sunday Times (UK)    |   99.21 |  99.92 |  99.99 |  99.94 |
| The Times (UK)           |   99.72 |  99.97 | 100    |  99.97 |
| ABC                      |   99.9  |  99.99 | 100    |  99.99 |
| The Daily Telegraph (UK) |   99.93 |  99.99 | 100    |  99.99 |
| The Guardian (UK)        |   99.96 | 100    | 100    | 100    |
| CNN                      |  100    | 100    | 100    | 100    |
| Fox New                  |  100    | 100    | 100    | 100    |
| NBC                      |  100    | 100    | 100    | 100    |

### Student Essays

| subset            |   tpAUC |   pAUC |    AUC |     AP |
|:------------------|--------:|-------:|-------:|-------:|
| ELLIPSE           |   63.99 |  96.27 |  98.8  |  98.06 |
| ELLIPSE(Human)+   |   99.38 |  99.94 |  99.99 |  99.99 |
| Ivy Panda (AI)    |         |        |        |        |
| Ivy Panda         |   99.93 |  99.99 | 100    | 100    |
| Ivy Panda(Human)+ |   91.48 |  99.11 |  99.89 |  99.21 |
| ELLIPSE (AI)      |         |        |        |        |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   72.97 |  90.46 | 93.81 | 65.95 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |   75.05 |  91.06 | 94.44 | 54.38 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   80.25 |  93.03 | 95.7  | 69.86 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   83.04 |  94    | 96.61 | 82.92 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   83.81 |  94.28 | 96.53 | 84.36 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   85.01 |  94.71 | 96.05 | 87.91 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |   90.27 |  96.52 | 98.18 | 72.71 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   94.21 |  97.94 | 98.82 | 94.16 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   96.71 |  98.83 | 99.35 | 96.41 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   99.09 |  99.68 | 99.84 | 98.51 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   99.8  |  99.93 | 99.96 | 99.73 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   99.85 |  99.95 | 99.97 | 99.06 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ❌       | ✅        | ❌          | ❌     | ❌               | ❌                     |
| Base      | ✅       | ❌        | ✅          | ✅     | ✅               | ✅                     |

