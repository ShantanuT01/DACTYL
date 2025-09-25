# desklib - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 50.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |    0    |  61.95 | 79.6  | 24.11 |
| test-1b-no-finetuning |    0.64 |  69.04 | 86.87 | 40.49 |
| test                  |   43.51 |  85.51 | 94.76 | 92.45 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   83.51 |  95.77 | 99.31 | 98.05 |
| abstracts            |   60.72 |  89.93 | 95.53 | 97.2  |
| news                 |   78.77 |  94.55 | 97.96 | 98.33 |
| reviews              |   28.21 |  81.13 | 91.61 | 80.9  |
| student_essays       |   70.34 |  92.39 | 96.75 | 95.53 |
| tweets               |    0    |  54.79 | 61.18 | 66.71 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |    0    |  52.22 | 63.73 |  2.71 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |    0    |  56.79 | 77.09 |  1.24 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  59.16 | 83.4  |  2.38 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    0.64 |  69.04 | 86.87 | 40.49 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    2.86 |  70.27 | 88.76 | 13.83 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    2.97 |  68.32 | 92.94 | 12.27 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |   13.61 |  75.7  | 91.7  | 21.72 |
| llama-3.2-90b                                                                      |   15.27 |  78.05 | 89.63 | 62.9  |
| gemini-1.5-pro                                                                     |   22.35 |  79.92 | 93.01 | 66.97 |
| llama-3.3-70b                                                                      |   31.8  |  82.47 | 92.91 | 71.13 |
| gemini-1.5-flash                                                                   |   38.71 |  84.27 | 95.18 | 75.24 |
| mistral-large-latest                                                               |   46.12 |  86.18 | 95.25 | 77.77 |
| mistral-small-latest                                                               |   50.94 |  87.42 | 96.24 | 80.67 |
| gpt-4o-2024-11-20                                                                  |   51.38 |  87.53 | 96.16 | 80.49 |
| claude-3-5-sonnet-20241022                                                         |   52.86 |  87.9  | 96.27 | 80.71 |
| DeepSeek-V3                                                                        |   53.95 |  88.19 | 94.99 | 80.87 |
| claude-3-5-haiku-20241022                                                          |   55.2  |  88.51 | 95.42 | 81.48 |
| gpt-4o-mini                                                                        |   61.68 |  90.17 | 97.36 | 85.42 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   95.26 |  98.79 | 99.84 | 99.42 |
| abstracts            |   79.23 |  94.67 | 98.1  | 98.63 |
| news                 |   95.17 |  98.76 | 99.45 | 99.54 |
| reviews              |   40.41 |  84.45 | 93.13 | 83.45 |
| student_essays       |   86.49 |  96.54 | 97.82 | 97.26 |
| tweets               |    0    |  53.15 | 57.85 | 59.04 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |       0 |  50.55 | 52.12 | 82.35 |
| 538Tweets/lefttroll  |       0 |  54.62 | 60.43 | 56.54 |
| 538Tweets/righttroll |       0 |  53.35 | 59.21 | 51.07 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   23.34 |  80.21 | 88.51 | 76.1  |
|       2 |   40.3  |  84.36 | 93.4  | 83.46 |
|       3 |   49.83 |  87.05 | 95.6  | 87.85 |
|       4 |   51.24 |  87.3  | 95.46 | 87.86 |
|       5 |   41.74 |  84.67 | 93.19 | 83.57 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   85.05 |  96.16 | 98.63 | 99.05 |
| arxiv/astro-ph.CO        |   89.19 |  97.24 | 99.4  | 99.51 |
| arxiv/astro-ph.GA        |   90.72 |  97.62 | 99.24 | 99.43 |
| arxiv/astro-ph.HE        |   90.39 |  97.52 | 98.71 | 99.19 |
| arxiv/astro-ph.SR        |   92.25 |  98    | 99.63 | 99.7  |
| arxiv/cond-mat.mes-hall  |   86.44 |  96.52 | 99.01 | 99.26 |
| arxiv/cond-mat.mtrl-sci  |   87.95 |  96.93 | 98.99 | 99.29 |
| arxiv/cond-mat.stat-mech |   78.74 |  94.53 | 97.72 | 98.49 |
| arxiv/cond-mat.str-el    |   87.43 |  96.78 | 98.29 | 98.83 |
| arxiv/cs.CV              |   87.24 |  96.71 | 98.89 | 99.17 |
| arxiv/gr-qc              |   78.41 |  94.48 | 97.64 | 98.37 |
| arxiv/hep-ph             |   75.26 |  93.67 | 97.69 | 98.35 |
| arxiv/hep-th             |   74.36 |  93.43 | 97.36 | 98.03 |
| arxiv/math.AG            |   76.2  |  93.9  | 97.31 | 98.15 |
| arxiv/math.AP            |   75.65 |  93.77 | 97.56 | 98.28 |
| arxiv/math.CO            |   70.76 |  92.48 | 97    | 97.89 |
| arxiv/math.NT            |   57.55 |  89.08 | 96.02 | 97.17 |
| arxiv/math.PR            |   75.29 |  93.68 | 97.71 | 98.32 |
| arxiv/nucl-th            |   73.14 |  93.13 | 97.7  | 98.24 |
| arxiv/quant-ph           |   80.67 |  95.06 | 97.93 | 98.55 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   97.63 |  99.39 | 99.71 | 99.81 |
| real   |   90.41 |  97.54 | 98.65 | 98.42 |

| topic           |   tpAUC |   pAUC |   AUC |    AP |
|:----------------|--------:|-------:|------:|------:|
| Government News |   94.15 |  98.49 | 99.09 | 99.72 |
| Middle-east     |   97.62 |  99.39 | 99.45 | 99.92 |
| News            |   98.55 |  99.63 | 99.96 | 99.93 |
| US_News         |   99.07 |  99.76 | 99.86 | 99.97 |
| left-news       |   98.98 |  99.74 | 99.97 | 99.97 |
| politics        |   98.05 |  99.5  | 99.92 | 99.88 |
| politicsNews    |   90.32 |  97.52 | 98.89 | 98.62 |
| worldnews       |   92.22 |  98    | 98.96 | 98.62 |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| Fox New                  |   94.45 |  98.58 | 99.46 | 98.53 |
| The Guardian (UK)        |   94.59 |  98.61 | 99.35 | 98.4  |
| ABC                      |   94.67 |  98.63 | 99.4  | 98.43 |
| The Times (UK)           |   94.98 |  98.71 | 99.48 | 98.54 |
| The Daily Telegraph (UK) |   95.07 |  98.73 | 99.24 | 98.46 |
| NBC                      |   95.51 |  98.85 | 99.46 | 98.69 |
| CNN                      |   95.62 |  98.88 | 99.6  | 98.81 |
| The Sunday Times (UK)    |   96.51 |  99.1  | 99.63 | 99.05 |

### Student Essays

| subset            |   tpAUC |   pAUC |    AUC |     AP |
|:------------------|--------:|-------:|-------:|-------:|
| ELLIPSE           |   61.51 |  90.12 |  95.07 |  93.27 |
| ELLIPSE(Human)+   |   99.88 |  99.97 | 100    | 100    |
| Ivy Panda (AI)    |         |        |        |        |
| Ivy Panda         |   99.43 |  99.85 |  99.97 |  99.94 |
| Ivy Panda(Human)+ |   40.16 |  84.64 |  89.26 |  78.41 |
| ELLIPSE (AI)      |         |        |        |        |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   12.4  |  65.34 | 73.62 | 24.58 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   20.03 |  69.64 | 79.66 |  7.67 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   30.79 |  74.3  | 78.99 | 35.55 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   34.86 |  76.15 | 79.95 | 41.41 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   44.44 |  79.65 | 86.94 | 18.03 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   53.07 |  83.03 | 89.14 | 52.51 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   53.75 |  83.48 | 89.12 | 61.65 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   56.87 |  84.53 | 90.29 | 57.27 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |   57    |  83.99 | 90.81 | 28.95 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |   60.63 |  85.79 | 90.98 | 41.68 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   81.05 |  93.13 | 95.9  | 46.78 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   83.87 |  93.98 | 96.93 | 38.21 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ❌     | ✅               | ❌                     |
| Base      | ❌       | ❌        | ❌          | ✅     | ❌               | ✅                     |

