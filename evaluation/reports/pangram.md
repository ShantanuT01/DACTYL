# pangram - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 50.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |   10.68 |  74.99 | 86.61 | 52.4  |
| test-1b-no-finetuning |   34.92 |  82.78 | 92.2  | 68.87 |
| test                  |   76.23 |  93.89 | 97.31 | 96.78 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   94.57 |  98.61 | 99.38 | 98.96 |
| abstracts            |   89.58 |  97.33 | 98.39 | 99.11 |
| news                 |   94.59 |  98.61 | 99.42 | 99.53 |
| reviews              |   55.7  |  88.64 | 95.06 | 89.73 |
| student_essays       |   75.89 |  93.82 | 95.34 | 94.8  |
| tweets               |    0.01 |  68.56 | 80.12 | 85.22 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  54.03 | 68.92 |  1.02 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  61.07 | 63.1  |  6.03 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    0    |  64.08 | 85.75 |  8.51 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |   34.92 |  82.78 | 92.2  | 68.87 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |   41.18 |  84.4  | 93.01 | 32.52 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |   43.05 |  84.69 | 95.86 | 55.94 |
| gemini-1.5-pro                                                                     |   59.39 |  89.58 | 96.54 | 83.66 |
| llama-3.2-90b                                                                      |   63.76 |  90.7  | 96.54 | 85.21 |
| llama-3.3-70b                                                                      |   64.87 |  90.98 | 94.88 | 85.09 |
| claude-3-5-haiku-20241022                                                          |   68.75 |  91.98 | 93.43 | 86.34 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |   71.83 |  92.48 | 97.62 | 54.9  |
| gemini-1.5-flash                                                                   |   74.98 |  93.57 | 98.29 | 90.29 |
| mistral-large-latest                                                               |   75.51 |  93.71 | 97.25 | 89.92 |
| gpt-4o-2024-11-20                                                                  |   78.13 |  94.38 | 98    | 91.31 |
| claude-3-5-sonnet-20241022                                                         |   83.16 |  95.67 | 98.39 | 93.22 |
| gpt-4o-mini                                                                        |   86.75 |  96.59 | 98.7  | 94.57 |
| mistral-small-latest                                                               |   89.63 |  97.33 | 99.04 | 95.63 |
| DeepSeek-V3                                                                        |   93.58 |  98.34 | 99.32 | 97.33 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   99.6  |  99.9  | 99.96 | 99.92 |
| abstracts            |   94.39 |  98.56 | 99.36 | 99.57 |
| news                 |   97.92 |  99.47 | 99.82 | 99.82 |
| reviews              |   75.1  |  93.61 | 97.9  | 94.41 |
| student_essays       |   89.84 |  97.39 | 98.04 | 97.66 |
| tweets               |    1    |  70.15 | 80.88 | 84.43 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |    0    |  59.88 | 73.52 | 92.28 |
| 538Tweets/lefttroll  |    0.69 |  71.51 | 80.16 | 81.58 |
| 538Tweets/righttroll |    6.07 |  73.17 | 82.82 | 82.95 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   61.79 |  90.2  | 96.46 | 90.86 |
|       2 |   72.54 |  92.96 | 97.81 | 94.01 |
|       3 |   75.86 |  93.81 | 98.42 | 95.14 |
|       4 |   81.87 |  95.35 | 98.36 | 95.77 |
|       5 |   83.56 |  95.78 | 98.56 | 96.38 |

### Abstracts

| category                 |   tpAUC |   pAUC |    AUC |     AP |
|:-------------------------|--------:|-------:|-------:|-------:|
| arxiv/astro-ph           |   98    |  99.49 |  99.86 |  99.89 |
| arxiv/astro-ph.CO        |   98.92 |  99.73 |  99.95 |  99.95 |
| arxiv/astro-ph.GA        |   99.16 |  99.78 |  99.94 |  99.95 |
| arxiv/astro-ph.HE        |   98.04 |  99.5  |  99.65 |  99.78 |
| arxiv/astro-ph.SR        |  100    | 100    | 100    | 100    |
| arxiv/cond-mat.mes-hall  |   97.5  |  99.36 |  99.61 |  99.77 |
| arxiv/cond-mat.mtrl-sci  |   97.64 |  99.4  |  99.65 |  99.79 |
| arxiv/cond-mat.stat-mech |   89.94 |  97.41 |  98.74 |  99.18 |
| arxiv/cond-mat.str-el    |   96.88 |  99.2  |  99.82 |  99.85 |
| arxiv/cs.CV              |   96.49 |  99.1  |  99.66 |  99.76 |
| arxiv/gr-qc              |   93.79 |  98.41 |  98.74 |  99.24 |
| arxiv/hep-ph             |   91.79 |  97.9  |  99.14 |  99.42 |
| arxiv/hep-th             |   89.19 |  97.23 |  98.93 |  99.18 |
| arxiv/math.AG            |   90.83 |  97.65 |  99.07 |  99.37 |
| arxiv/math.AP            |   92.64 |  98.12 |  99.16 |  99.45 |
| arxiv/math.CO            |   88.15 |  96.96 |  98.7  |  99.1  |
| arxiv/math.NT            |   90.15 |  97.47 |  98.49 |  99.08 |
| arxiv/math.PR            |   92.07 |  97.97 |  99.04 |  99.35 |
| arxiv/nucl-th            |   93.21 |  98.26 |  99.16 |  99.44 |
| arxiv/quant-ph           |   90.92 |  97.68 |  98.92 |  99.26 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   99.11 |  99.77 | 99.97 | 99.98 |
| real   |   94.81 |  98.67 | 99.28 | 99.04 |

| topic           |   tpAUC |   pAUC |    AUC |     AP |
|:----------------|--------:|-------:|-------:|-------:|
| Government News |   96.19 |  99.02 |  99.85 |  99.95 |
| Middle-east     |   98.81 |  99.69 |  99.96 |  99.99 |
| News            |  100    | 100    | 100    | 100    |
| US_News         |   99.6  |  99.9  |  99.99 | 100    |
| left-news       |   99.98 | 100    | 100    | 100    |
| politics        |   99.52 |  99.88 |  99.98 |  99.97 |
| politicsNews    |   97.19 |  99.28 |  99.58 |  99.47 |
| worldnews       |   92.5  |  98.07 |  99.21 |  98.84 |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| ABC                      |   96.96 |  99.22 | 99.78 | 99.12 |
| The Times (UK)           |   97.3  |  99.31 | 99.75 | 99.14 |
| The Guardian (UK)        |   97.43 |  99.34 | 99.77 | 99.21 |
| The Daily Telegraph (UK) |   97.8  |  99.44 | 99.8  | 99.36 |
| NBC                      |   98.08 |  99.51 | 99.86 | 99.44 |
| The Sunday Times (UK)    |   98.18 |  99.53 | 99.83 | 99.45 |
| CNN                      |   98.67 |  99.66 | 99.9  | 99.62 |
| Fox New                  |   98.96 |  99.73 | 99.91 | 99.67 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |     AP |
|:------------------|--------:|-------:|------:|-------:|
| ELLIPSE           |   70.28 |  92.37 | 95.28 |  94.14 |
| ELLIPSE(Human)+   |   99.94 |  99.98 | 99.99 | 100    |
| Ivy Panda (AI)    |         |        |       |        |
| Ivy Panda         |   99.93 |  99.98 | 99.98 |  99.98 |
| Ivy Panda(Human)+ |   54.49 |  88.33 | 90.41 |  82.88 |
| ELLIPSE (AI)      |         |        |       |        |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |    7.75 |  61.56 | 66.25 | 14.86 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   16.3  |  66.74 | 72.19 |  4.51 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |   18.65 |  70.64 | 71.93 | 30.96 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   46.92 |  80.53 | 85.71 | 47.73 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   50.54 |  81.94 | 86.68 | 25.92 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |   62.36 |  86.7  | 89.08 | 66.13 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   77.42 |  92.03 | 92.69 | 85.68 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   81.57 |  93.49 | 93.36 | 88.38 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   82.22 |  93.72 | 95.39 | 79.29 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   82.7  |  93.9  | 95.67 | 87.42 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   88.38 |  95.9  | 97.03 | 85.31 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   95.1  |  98.27 | 98.67 | 95.11 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ❌     | ✅               | ❌                     |
| Base      | ❌       | ❌        | ❌          | ✅     | ❌               | ✅                     |

