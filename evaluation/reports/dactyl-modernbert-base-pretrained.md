# dactyl-modernbert-base-pretrained - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 80.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |   35.63 |  92.96 | 97.86 | 88.6  |
| test-1b-no-finetuning |   54.34 |  95.27 | 98.04 | 92.44 |
| test                  |   92.88 |  99.27 | 99.84 | 99.76 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   98.02 |  99.8  | 99.97 | 99.91 |
| abstracts            |   91.94 |  99.17 | 99.75 | 99.84 |
| news                 |   88.88 |  98.86 | 99.67 | 99.72 |
| reviews              |   73.71 |  97.29 | 99.07 | 97.83 |
| student_essays       |   83.27 |  98.28 | 99.56 | 99.27 |
| tweets               |   69.56 |  96.85 | 99.13 | 99.35 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |    AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|-------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  74.56 |  90.91 | 17.03 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    9.89 |  88.07 |  96.74 | 53.99 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |   46.03 |  93.85 |  98.67 | 71.38 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |   54.34 |  95.27 |  98.04 | 92.44 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |   65.52 |  96.32 |  99.26 | 87.56 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |   68.1  |  96.7  |  99.36 | 87.31 |
| gemini-1.5-pro                                                                     |   80.29 |  97.98 |  99.61 | 97    |
| llama-3.2-90b                                                                      |   81.18 |  98.06 |  99.46 | 97.02 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |   84.28 |  98.27 |  99.42 | 93.96 |
| gemini-1.5-flash                                                                   |   89.3  |  98.9  |  99.79 | 98.36 |
| gpt-4o-2024-11-20                                                                  |   89.6  |  98.93 |  99.77 | 98.45 |
| claude-3-5-haiku-20241022                                                          |   91.58 |  99.14 |  99.84 | 98.74 |
| llama-3.3-70b                                                                      |   94.35 |  99.42 |  99.87 | 99.12 |
| claude-3-5-sonnet-20241022                                                         |   98.3  |  99.83 |  99.98 | 99.76 |
| mistral-small-latest                                                               |   98.83 |  99.88 |  99.93 | 99.8  |
| mistral-large-latest                                                               |   98.83 |  99.88 |  99.97 | 99.79 |
| DeepSeek-V3                                                                        |   99.67 |  99.97 | 100    | 99.94 |
| gpt-4o-mini                                                                        |   99.89 |  99.99 | 100    | 99.98 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |    AUC |    AP |
|:---------------------|--------:|-------:|-------:|------:|
| RedditWritingPrompts |   99.84 |  99.98 | 100    | 99.99 |
| abstracts            |   93.63 |  99.35 |  99.82 | 99.87 |
| news                 |   99.74 |  99.97 |  99.98 | 99.98 |
| reviews              |   82.92 |  98.25 |  99.44 | 98.48 |
| student_essays       |   99.39 |  99.94 |  99.99 | 99.98 |
| tweets               |   73.72 |  97.3  |  99.26 | 99.37 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |   79.07 |  97.86 | 99.28 | 99.84 |
| 538Tweets/lefttroll  |   63.76 |  96.24 | 98.88 | 98.81 |
| 538Tweets/righttroll |   79.22 |  97.87 | 99.43 | 99.34 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   73.4  |  97.27 | 98.92 | 97.41 |
|       2 |   80.04 |  97.95 | 99.46 | 98.43 |
|       3 |   91.04 |  99.08 | 99.76 | 99.25 |
|       4 |   86.63 |  98.63 | 99.58 | 98.87 |
|       5 |   84.32 |  98.39 | 99.35 | 98.42 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   94.85 |  99.47 | 99.91 | 99.93 |
| arxiv/astro-ph.CO        |   98.04 |  99.8  | 99.98 | 99.98 |
| arxiv/astro-ph.GA        |   99.09 |  99.91 | 99.99 | 99.99 |
| arxiv/astro-ph.HE        |   96.25 |  99.61 | 99.96 | 99.97 |
| arxiv/astro-ph.SR        |   98.18 |  99.81 | 99.98 | 99.98 |
| arxiv/cond-mat.mes-hall  |   97.49 |  99.74 | 99.97 | 99.98 |
| arxiv/cond-mat.mtrl-sci  |   94.15 |  99.4  | 99.91 | 99.93 |
| arxiv/cond-mat.stat-mech |   92.73 |  99.25 | 99.75 | 99.83 |
| arxiv/cond-mat.str-el    |   94.58 |  99.44 | 99.86 | 99.88 |
| arxiv/cs.CV              |   91.29 |  99.1  | 99.85 | 99.88 |
| arxiv/gr-qc              |   91.96 |  99.18 | 99.63 | 99.74 |
| arxiv/hep-ph             |   90.64 |  99.04 | 99.49 | 99.68 |
| arxiv/hep-th             |   91.68 |  99.15 | 99.66 | 99.73 |
| arxiv/math.AG            |   92.77 |  99.26 | 99.8  | 99.85 |
| arxiv/math.AP            |   92.08 |  99.19 | 99.82 | 99.86 |
| arxiv/math.CO            |   90.62 |  99.04 | 99.68 | 99.78 |
| arxiv/math.NT            |   90.64 |  99.04 | 99.43 | 99.65 |
| arxiv/math.PR            |   93.71 |  99.36 | 99.92 | 99.93 |
| arxiv/nucl-th            |   93.64 |  99.35 | 99.75 | 99.82 |
| arxiv/quant-ph           |   93.05 |  99.29 | 99.87 | 99.89 |

### News

| real   |   tpAUC |   pAUC |   AUC |     AP |
|:-------|--------:|-------:|------:|-------:|
| fake   |   99.94 |  99.99 | 100   | 100    |
| real   |   99.15 |  99.91 |  99.9 |  99.92 |

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
| ABC                      |   99.49 |  99.95 |  99.99 |  99.95 |
| The Times (UK)           |   99.78 |  99.98 | 100    |  99.98 |
| The Sunday Times (UK)    |   99.85 |  99.98 | 100    |  99.99 |
| Fox New                  |   99.97 | 100    | 100    | 100    |
| CNN                      |  100    | 100    | 100    | 100    |
| NBC                      |  100    | 100    | 100    | 100    |
| The Guardian (UK)        |  100    | 100    | 100    | 100    |

### Student Essays

| subset            |   tpAUC |   pAUC |    AUC |     AP |
|:------------------|--------:|-------:|-------:|-------:|
| ELLIPSE           |   96.6  |  99.65 |  99.93 |  99.86 |
| ELLIPSE(Human)+   |   99.95 |  99.99 | 100    | 100    |
| Ivy Panda (AI)    |         |        |        |        |
| Ivy Panda         |   99.98 | 100    | 100    | 100    |
| Ivy Panda(Human)+ |   97.67 |  99.76 |  99.96 |  99.79 |
| ELLIPSE (AI)      |         |        |        |        |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   80.24 |  93.02 | 95.2  | 69.27 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   84.85 |  94.65 | 96.94 | 86.5  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |   85.06 |  94.69 | 97.15 | 71.57 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |   88.02 |  95.77 | 97.19 | 86.09 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   91.83 |  97.11 | 98.18 | 91.97 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   94.14 |  97.93 | 98.58 | 94.71 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   95.48 |  98.4  | 99.08 | 94.56 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   95.65 |  98.46 | 98.89 | 90.64 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   97.14 |  98.99 | 99.32 | 98.1  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   97.2  |  99.01 | 99.33 | 97.79 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   98.05 |  99.31 | 99.65 | 96.1  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   99.69 |  99.89 | 99.94 | 98.3  |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ❌          | ❌     | ✅               | ❌                     |
| Base      | ❌       | ❌        | ✅          | ✅     | ❌               | ✅                     |

