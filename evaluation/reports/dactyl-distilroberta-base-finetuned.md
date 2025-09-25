# dactyl-distilroberta-base-finetuned - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 80.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |    2.87 |  87.89 | 94.29 | 77.96 |
| test-1b-no-finetuning |   33.68 |  93.05 | 96.1  | 88.49 |
| test                  |   92.5  |  99.2  | 99.77 | 99.7  |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   96.22 |  99.61 | 99.66 | 99.61 |
| abstracts            |   87.66 |  98.47 | 99.52 | 99.71 |
| news                 |   82.33 |  98.19 | 98.66 | 99.1  |
| reviews              |   69.1  |  96.81 | 98.63 | 97.25 |
| student_essays       |   70.4  |  96.96 | 98.52 | 98.17 |
| tweets               |   67.03 |  96.48 | 98.91 | 99.21 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  61.17 | 80.64 |  3.77 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  83.5  | 93.59 | 38.58 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |    0    |  84.75 | 90.22 | 54.66 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |   31.03 |  91.74 | 97.67 | 59.44 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |   33.68 |  93.05 | 96.1  | 88.49 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |   38.43 |  92.57 | 96.52 | 38.53 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |   75.31 |  97.13 | 98.6  | 87.52 |
| gemini-1.5-pro                                                                     |   77.14 |  97.64 | 99.4  | 96.48 |
| llama-3.2-90b                                                                      |   83.17 |  98.24 | 99.29 | 97.17 |
| gemini-1.5-flash                                                                   |   87.94 |  98.75 | 99.72 | 98.07 |
| claude-3-5-haiku-20241022                                                          |   89.92 |  98.93 | 99.65 | 98.28 |
| gpt-4o-2024-11-20                                                                  |   90.35 |  98.97 | 99.73 | 98.35 |
| llama-3.3-70b                                                                      |   95.4  |  99.49 | 99.81 | 99.06 |
| claude-3-5-sonnet-20241022                                                         |   98.2  |  99.76 | 99.93 | 99.46 |
| mistral-large-latest                                                               |   98.43 |  99.81 | 99.97 | 99.58 |
| mistral-small-latest                                                               |   98.63 |  99.82 | 99.97 | 99.62 |
| DeepSeek-V3                                                                        |   99.2  |  99.9  | 99.99 | 99.78 |
| gpt-4o-mini                                                                        |   99.23 |  99.86 | 99.99 | 99.62 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |    AUC |     AP |
|:---------------------|--------:|-------:|-------:|-------:|
| RedditWritingPrompts |   99.93 |  99.99 | 100    | 100    |
| abstracts            |   91.66 |  98.91 |  99.73 |  99.79 |
| news                 |   99.82 |  99.98 |  99.99 |  99.99 |
| reviews              |   83.89 |  98.35 |  99.44 |  98.58 |
| student_essays       |   99.28 |  99.93 |  99.99 |  99.97 |
| tweets               |   76.18 |  97.46 |  99.22 |  99.36 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |   82.44 |  98.2  | 99.26 | 99.84 |
| 538Tweets/lefttroll  |   67.8  |  96.42 | 98.89 | 98.86 |
| 538Tweets/righttroll |   80.49 |  98    | 99.39 | 99.34 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   73.62 |  97.26 | 99.01 | 97.61 |
|       2 |   81.68 |  98.12 | 99.26 | 98.32 |
|       3 |   90.62 |  99.04 | 99.79 | 99.27 |
|       4 |   88.13 |  98.78 | 99.62 | 98.94 |
|       5 |   84.82 |  98.44 | 99.52 | 98.65 |

### Abstracts

| category                 |   tpAUC |   pAUC |    AUC |     AP |
|:-------------------------|--------:|-------:|-------:|-------:|
| arxiv/astro-ph           |   91.63 |  99.02 |  99.87 |  99.88 |
| arxiv/astro-ph.CO        |   88.69 |  97.83 |  99.78 |  99.73 |
| arxiv/astro-ph.GA        |   99.89 |  99.99 | 100    | 100    |
| arxiv/astro-ph.HE        |   98    |  99.79 |  99.98 |  99.98 |
| arxiv/astro-ph.SR        |   95.03 |  98.71 |  99.87 |  99.83 |
| arxiv/cond-mat.mes-hall  |   97.24 |  99.72 |  99.96 |  99.97 |
| arxiv/cond-mat.mtrl-sci  |   82.81 |  95.78 |  99.44 |  99.37 |
| arxiv/cond-mat.stat-mech |   92.35 |  99.21 |  99.79 |  99.84 |
| arxiv/cond-mat.str-el    |   93.2  |  99.3  |  99.84 |  99.86 |
| arxiv/cs.CV              |   90.89 |  99.06 |  99.84 |  99.86 |
| arxiv/gr-qc              |   91.35 |  99.12 |  99.82 |  99.85 |
| arxiv/hep-ph             |   92.77 |  99.26 |  99.45 |  99.69 |
| arxiv/hep-th             |   92.39 |  99.22 |  99.46 |  99.67 |
| arxiv/math.AG            |   92.92 |  99.27 |  99.73 |  99.82 |
| arxiv/math.AP            |   90.49 |  99.03 |  99.84 |  99.87 |
| arxiv/math.CO            |   92.98 |  99.28 |  99.72 |  99.82 |
| arxiv/math.NT            |   86.86 |  98.43 |  99.22 |  99.52 |
| arxiv/math.PR            |   88.91 |  98.85 |  99.85 |  99.86 |
| arxiv/nucl-th            |   92.49 |  99.23 |  99.53 |  99.71 |
| arxiv/quant-ph           |   87.55 |  98.17 |  99.54 |  99.65 |

### News

| real   |   tpAUC |   pAUC |    AUC |     AP |
|:-------|--------:|-------:|-------:|-------:|
| fake   |   99.96 | 100    | 100    | 100    |
| real   |   99.43 |  99.94 |  99.97 |  99.96 |

| topic           |   tpAUC |   pAUC |    AUC |     AP |
|:----------------|--------:|-------:|-------:|-------:|
| Government News |  100    | 100    | 100    | 100    |
| Middle-east     |  100    | 100    | 100    | 100    |
| News            |  100    | 100    | 100    | 100    |
| US_News         |  100    | 100    | 100    | 100    |
| left-news       |  100    | 100    | 100    | 100    |
| politics        |   99.54 |  99.95 | 100    |  99.99 |
| politicsNews    |   98.86 |  99.88 |  99.93 |  99.9  |
| worldnews       |  100    | 100    | 100    | 100    |

| news_outlet              |   tpAUC |   pAUC |    AUC |     AP |
|:-------------------------|--------:|-------:|-------:|-------:|
| The Daily Telegraph (UK) |   98.86 |  99.88 |  99.96 |  99.85 |
| Fox New                  |   99.67 |  99.97 | 100    |  99.97 |
| NBC                      |  100    | 100    | 100    | 100    |
| ABC                      |  100    | 100    | 100    | 100    |
| The Guardian (UK)        |  100    | 100    | 100    | 100    |
| The Sunday Times (UK)    |  100    | 100    | 100    | 100    |
| The Times (UK)           |  100    | 100    | 100    | 100    |
| CNN                      |  100    | 100    | 100    | 100    |

### Student Essays

| subset            |   tpAUC |   pAUC |    AUC |     AP |
|:------------------|--------:|-------:|-------:|-------:|
| ELLIPSE           |   98.25 |  99.82 |  99.96 |  99.93 |
| ELLIPSE(Human)+   |   99.66 |  99.97 | 100    | 100    |
| Ivy Panda (AI)    |         |        |        |        |
| Ivy Panda         |   99.59 |  99.96 | 100    |  99.99 |
| Ivy Panda(Human)+ |   98.19 |  99.81 |  99.97 |  99.83 |
| ELLIPSE (AI)      |         |        |        |        |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |   56.14 |  84.28 | 87.26 | 43.08 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   67.51 |  88.5  | 90.84 | 56.46 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   70.17 |  89.47 | 90.51 | 80.41 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   77.17 |  91.94 | 92.11 | 84    |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |   78.17 |  92.29 | 93.64 | 78.43 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   84.57 |  94.4  | 96.28 | 81.22 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   90.82 |  96.76 | 97.43 | 85.54 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   91.3  |  96.93 | 98.11 | 92.36 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   93.32 |  97.64 | 97.48 | 94.09 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   94.56 |  97.98 | 98.38 | 91.26 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   95.28 |  98.33 | 98.08 | 93.41 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   95.28 |  98.34 | 98.39 | 96.64 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ❌     | ✅               | ❌                     |
| Base      | ❌       | ❌        | ❌          | ✅     | ❌               | ✅                     |

