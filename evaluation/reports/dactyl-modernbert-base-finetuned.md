# dactyl-modernbert-base-finetuned - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 80.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |   35.35 |  92.92 | 97.85 | 88.53 |
| test-1b-no-finetuning |   54.17 |  95.26 | 98.04 | 92.41 |
| test                  |   92.91 |  99.27 | 99.84 | 99.76 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   98.03 |  99.8  | 99.97 | 99.91 |
| abstracts            |   91.96 |  99.18 | 99.75 | 99.84 |
| news                 |   88.78 |  98.85 | 99.67 | 99.72 |
| reviews              |   73.68 |  97.29 | 99.06 | 97.83 |
| student_essays       |   83.25 |  98.28 | 99.55 | 99.27 |
| tweets               |   69.65 |  96.86 | 99.13 | 99.35 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |    AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|-------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  74.43 |  90.91 | 16.69 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    9.69 |  88.01 |  96.72 | 53.81 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |   45.56 |  93.78 |  98.67 | 70.82 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |   54.17 |  95.26 |  98.04 | 92.41 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |   65.4  |  96.3  |  99.26 | 87.54 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |   68.04 |  96.69 |  99.36 | 87.22 |
| gemini-1.5-pro                                                                     |   80.31 |  97.98 |  99.61 | 97.01 |
| llama-3.2-90b                                                                      |   81.24 |  98.07 |  99.46 | 97.03 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |   84.23 |  98.27 |  99.41 | 93.83 |
| gemini-1.5-flash                                                                   |   89.35 |  98.91 |  99.79 | 98.37 |
| gpt-4o-2024-11-20                                                                  |   89.65 |  98.94 |  99.77 | 98.46 |
| claude-3-5-haiku-20241022                                                          |   91.56 |  99.13 |  99.84 | 98.74 |
| llama-3.3-70b                                                                      |   94.36 |  99.42 |  99.87 | 99.12 |
| claude-3-5-sonnet-20241022                                                         |   98.33 |  99.83 |  99.98 | 99.76 |
| mistral-small-latest                                                               |   98.84 |  99.88 |  99.93 | 99.8  |
| mistral-large-latest                                                               |   98.85 |  99.88 |  99.97 | 99.8  |
| DeepSeek-V3                                                                        |   99.7  |  99.97 | 100    | 99.94 |
| gpt-4o-mini                                                                        |   99.89 |  99.99 | 100    | 99.98 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |    AUC |    AP |
|:---------------------|--------:|-------:|-------:|------:|
| RedditWritingPrompts |   99.84 |  99.98 | 100    | 99.99 |
| abstracts            |   93.68 |  99.35 |  99.82 | 99.87 |
| news                 |   99.75 |  99.97 |  99.98 | 99.98 |
| reviews              |   83    |  98.25 |  99.44 | 98.49 |
| student_essays       |   99.38 |  99.94 |  99.99 | 99.98 |
| tweets               |   73.8  |  97.31 |  99.27 | 99.37 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |   79.2  |  97.87 | 99.28 | 99.84 |
| 538Tweets/lefttroll  |   63.78 |  96.24 | 98.89 | 98.82 |
| 538Tweets/righttroll |   79.35 |  97.88 | 99.44 | 99.35 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   73.5  |  97.28 | 98.92 | 97.42 |
|       2 |   80.29 |  97.98 | 99.46 | 98.44 |
|       3 |   91.17 |  99.09 | 99.77 | 99.26 |
|       4 |   86.66 |  98.63 | 99.58 | 98.87 |
|       5 |   84.27 |  98.39 | 99.36 | 98.43 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   94.81 |  99.47 | 99.91 | 99.93 |
| arxiv/astro-ph.CO        |   98.15 |  99.81 | 99.98 | 99.98 |
| arxiv/astro-ph.GA        |   99.09 |  99.91 | 99.99 | 99.99 |
| arxiv/astro-ph.HE        |   96.33 |  99.62 | 99.96 | 99.97 |
| arxiv/astro-ph.SR        |   98.25 |  99.82 | 99.98 | 99.98 |
| arxiv/cond-mat.mes-hall  |   97.56 |  99.75 | 99.98 | 99.98 |
| arxiv/cond-mat.mtrl-sci  |   94.19 |  99.41 | 99.91 | 99.93 |
| arxiv/cond-mat.stat-mech |   92.84 |  99.26 | 99.76 | 99.84 |
| arxiv/cond-mat.str-el    |   94.58 |  99.44 | 99.86 | 99.88 |
| arxiv/cs.CV              |   91.33 |  99.1  | 99.86 | 99.88 |
| arxiv/gr-qc              |   92.07 |  99.19 | 99.63 | 99.74 |
| arxiv/hep-ph             |   90.64 |  99.04 | 99.5  | 99.68 |
| arxiv/hep-th             |   91.72 |  99.15 | 99.66 | 99.74 |
| arxiv/math.AG            |   92.84 |  99.27 | 99.81 | 99.85 |
| arxiv/math.AP            |   92.23 |  99.21 | 99.82 | 99.86 |
| arxiv/math.CO            |   90.65 |  99.04 | 99.68 | 99.78 |
| arxiv/math.NT            |   90.68 |  99.04 | 99.44 | 99.65 |
| arxiv/math.PR            |   93.78 |  99.37 | 99.92 | 99.93 |
| arxiv/nucl-th            |   93.54 |  99.34 | 99.75 | 99.82 |
| arxiv/quant-ph           |   93.05 |  99.29 | 99.87 | 99.89 |

### News

| real   |   tpAUC |   pAUC |   AUC |     AP |
|:-------|--------:|-------:|------:|-------:|
| fake   |   99.94 |  99.99 | 100   | 100    |
| real   |   99.16 |  99.91 |  99.9 |  99.92 |

| topic           |   tpAUC |   pAUC |    AUC |     AP |
|:----------------|--------:|-------:|-------:|-------:|
| Government News |  100    | 100    | 100    | 100    |
| Middle-east     |  100    | 100    | 100    | 100    |
| News            |  100    | 100    | 100    | 100    |
| US_News         |  100    | 100    | 100    | 100    |
| left-news       |  100    | 100    | 100    | 100    |
| politics        |   99.65 |  99.96 | 100    |  99.99 |
| politicsNews    |   98.86 |  99.88 |  99.81 |  99.85 |
| worldnews       |   99.26 |  99.92 |  99.99 |  99.98 |

| news_outlet              |   tpAUC |   pAUC |    AUC |     AP |
|:-------------------------|--------:|-------:|-------:|-------:|
| The Daily Telegraph (UK) |   98.86 |  99.88 |  99.82 |  99.8  |
| ABC                      |   99.5  |  99.95 |  99.99 |  99.95 |
| The Times (UK)           |   99.77 |  99.98 | 100    |  99.98 |
| The Sunday Times (UK)    |   99.85 |  99.98 | 100    |  99.99 |
| Fox New                  |   99.99 | 100    | 100    | 100    |
| CNN                      |  100    | 100    | 100    | 100    |
| NBC                      |  100    | 100    | 100    | 100    |
| The Guardian (UK)        |  100    | 100    | 100    | 100    |

### Student Essays

| subset            |   tpAUC |   pAUC |    AUC |     AP |
|:------------------|--------:|-------:|-------:|-------:|
| ELLIPSE           |   96.58 |  99.65 |  99.93 |  99.86 |
| ELLIPSE(Human)+   |   99.95 |  99.99 | 100    | 100    |
| Ivy Panda (AI)    |         |        |        |        |
| Ivy Panda         |   99.98 | 100    | 100    | 100    |
| Ivy Panda(Human)+ |   97.63 |  99.76 |  99.96 |  99.79 |
| ELLIPSE (AI)      |         |        |        |        |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   80.03 |  92.94 | 95.14 | 69    |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   84.69 |  94.6  | 96.88 | 86.35 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |   85.01 |  94.67 | 97.15 | 71.53 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |   87.98 |  95.75 | 97.16 | 86.07 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   91.86 |  97.12 | 98.19 | 91.99 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   94.16 |  97.94 | 98.59 | 94.73 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   95.44 |  98.39 | 99.06 | 94.51 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   95.52 |  98.42 | 98.86 | 90.55 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   97.14 |  98.99 | 99.32 | 98.1  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   97.18 |  99.01 | 99.32 | 97.77 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   98.06 |  99.31 | 99.65 | 96.12 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   99.68 |  99.89 | 99.94 | 98.27 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ❌          | ❌     | ✅               | ❌                     |
| Base      | ❌       | ❌        | ✅          | ✅     | ❌               | ✅                     |

