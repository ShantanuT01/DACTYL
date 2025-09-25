# dactyl-distilroberta-base-pretrained - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 80.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |   21.91 |  90.95 | 97.07 | 85.08 |
| test-1b-no-finetuning |   43.89 |  94.13 | 97.18 | 90.5  |
| test                  |   92.06 |  99.18 | 99.78 | 99.7  |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   97.1  |  99.7  | 99.81 | 99.77 |
| abstracts            |   88.5  |  98.8  | 99.62 | 99.77 |
| news                 |   83.51 |  98.31 | 99.25 | 99.44 |
| reviews              |   70.27 |  96.93 | 98.88 | 97.5  |
| student_essays       |   74.49 |  97.38 | 99.06 | 98.74 |
| tweets               |   66.37 |  96.54 | 99.04 | 99.28 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  74.8  | 90.49 | 13.4  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  84.98 | 95.98 | 44.1  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |   13.89 |  90.3  | 96.68 | 70.03 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |   38.79 |  93.32 | 98.43 | 79.19 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |   43.89 |  94.13 | 97.18 | 90.5  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |   66.05 |  96.33 | 98.82 | 89.5  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |   70.27 |  96.84 | 98.99 | 81.05 |
| gemini-1.5-pro                                                                     |   75.29 |  97.45 | 99.36 | 96.24 |
| llama-3.2-90b                                                                      |   79.56 |  97.89 | 99.18 | 96.75 |
| gemini-1.5-flash                                                                   |   88.45 |  98.81 | 99.75 | 98.19 |
| claude-3-5-haiku-20241022                                                          |   88.61 |  98.82 | 99.76 | 98.28 |
| gpt-4o-2024-11-20                                                                  |   90.03 |  98.97 | 99.77 | 98.47 |
| llama-3.3-70b                                                                      |   95.54 |  99.54 | 99.85 | 99.24 |
| claude-3-5-sonnet-20241022                                                         |   98.57 |  99.85 | 99.96 | 99.74 |
| mistral-large-latest                                                               |   98.77 |  99.87 | 99.97 | 99.77 |
| mistral-small-latest                                                               |   99    |  99.89 | 99.95 | 99.81 |
| DeepSeek-V3                                                                        |   99.28 |  99.92 | 99.99 | 99.87 |
| gpt-4o-mini                                                                        |   99.65 |  99.96 | 99.99 | 99.92 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |    AUC |    AP |
|:---------------------|--------:|-------:|-------:|------:|
| RedditWritingPrompts |   99.83 |  99.98 | 100    | 99.99 |
| abstracts            |   92.99 |  99.27 |  99.77 | 99.84 |
| news                 |   99.83 |  99.98 |  99.98 | 99.99 |
| reviews              |   82.4  |  98.18 |  99.34 | 98.38 |
| student_essays       |   98.87 |  99.88 |  99.98 | 99.95 |
| tweets               |   74.27 |  97.36 |  99.28 | 99.38 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |   81.5  |  98.11 | 99.36 | 99.86 |
| 538Tweets/lefttroll  |   64.07 |  96.29 | 98.95 | 98.88 |
| 538Tweets/righttroll |   79.62 |  97.91 | 99.44 | 99.35 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   69.42 |  96.8  | 98.85 | 97.09 |
|       2 |   79.14 |  97.85 | 99.17 | 98.07 |
|       3 |   91.99 |  99.18 | 99.73 | 99.26 |
|       4 |   85.04 |  98.47 | 99.5  | 98.72 |
|       5 |   85.66 |  98.53 | 99.38 | 98.6  |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   94.85 |  99.47 | 99.84 | 99.89 |
| arxiv/astro-ph.CO        |   94.69 |  99.46 | 99.89 | 99.91 |
| arxiv/astro-ph.GA        |   99.35 |  99.93 | 99.99 | 99.99 |
| arxiv/astro-ph.HE        |   97.45 |  99.74 | 99.97 | 99.98 |
| arxiv/astro-ph.SR        |   95.24 |  99.35 | 99.94 | 99.93 |
| arxiv/cond-mat.mes-hall  |   97.35 |  99.73 | 99.96 | 99.97 |
| arxiv/cond-mat.mtrl-sci  |   94.23 |  99.41 | 99.78 | 99.87 |
| arxiv/cond-mat.stat-mech |   91.1  |  99.08 | 99.76 | 99.82 |
| arxiv/cond-mat.str-el    |   92.32 |  99.21 | 99.82 | 99.84 |
| arxiv/cs.CV              |   90.59 |  99.03 | 99.77 | 99.82 |
| arxiv/gr-qc              |   92.11 |  99.19 | 99.68 | 99.79 |
| arxiv/hep-ph             |   92.39 |  99.22 | 99.48 | 99.7  |
| arxiv/hep-th             |   90.81 |  99.06 | 99.59 | 99.72 |
| arxiv/math.AG            |   93.67 |  99.35 | 99.77 | 99.84 |
| arxiv/math.AP            |   90.11 |  98.99 | 99.8  | 99.84 |
| arxiv/math.CO            |   91.09 |  99.08 | 99.74 | 99.82 |
| arxiv/math.NT            |   89.7  |  98.94 | 99.19 | 99.54 |
| arxiv/math.PR            |   91.93 |  99.18 | 99.89 | 99.9  |
| arxiv/nucl-th            |   92.63 |  99.25 | 99.65 | 99.75 |
| arxiv/quant-ph           |   90.84 |  99.06 | 99.73 | 99.81 |

### News

| real   |   tpAUC |   pAUC |    AUC |     AP |
|:-------|--------:|-------:|-------:|-------:|
| fake   |   99.94 |  99.99 | 100    | 100    |
| real   |   99.43 |  99.94 |  99.91 |  99.93 |

| topic           |   tpAUC |   pAUC |    AUC |     AP |
|:----------------|--------:|-------:|-------:|-------:|
| Government News |  100    | 100    | 100    | 100    |
| Middle-east     |  100    | 100    | 100    | 100    |
| News            |  100    | 100    | 100    | 100    |
| US_News         |  100    | 100    | 100    | 100    |
| left-news       |  100    | 100    | 100    | 100    |
| politics        |   99.47 |  99.95 |  99.99 |  99.99 |
| politicsNews    |   98.86 |  99.88 |  99.82 |  99.85 |
| worldnews       |  100    | 100    | 100    | 100    |

| news_outlet              |   tpAUC |   pAUC |    AUC |     AP |
|:-------------------------|--------:|-------:|-------:|-------:|
| The Daily Telegraph (UK) |   98.86 |  99.88 |  99.84 |  99.8  |
| Fox New                  |   99.74 |  99.97 | 100    |  99.98 |
| ABC                      |  100    | 100    | 100    | 100    |
| CNN                      |  100    | 100    | 100    | 100    |
| NBC                      |  100    | 100    | 100    | 100    |
| The Guardian (UK)        |  100    | 100    | 100    | 100    |
| The Sunday Times (UK)    |  100    | 100    | 100    | 100    |
| The Times (UK)           |  100    | 100    | 100    | 100    |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |   95.83 |  99.57 | 99.87 | 99.78 |
| ELLIPSE(Human)+   |   99.55 |  99.95 | 99.98 | 99.99 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |   99.55 |  99.95 | 99.99 | 99.98 |
| Ivy Panda(Human)+ |   97.14 |  99.71 | 99.95 | 99.72 |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |   72.68 |  90.23 | 92.73 | 54.66 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   75.34 |  91.3  | 92.73 | 81.07 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   76.28 |  91.61 | 94.17 | 61.78 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |   84.62 |  94.57 | 95.31 | 81.52 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   87.46 |  95.56 | 97.25 | 88.47 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   89.61 |  96.33 | 97.78 | 89.69 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   91.82 |  97.11 | 98.23 | 92.33 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   93.98 |  97.87 | 98.54 | 87.33 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   94.56 |  98.07 | 98.75 | 94.33 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   95.2  |  98.31 | 97.87 | 94.87 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   95.33 |  98.35 | 98.83 | 96.8  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   98.51 |  99.48 | 99.73 | 97.05 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ❌     | ✅               | ❌                     |
| Base      | ❌       | ❌        | ❌          | ✅     | ❌               | ✅                     |

