# fakespot - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 50.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |    0    |  50.83 | 67.37 |  7.5  |
| test-1b-no-finetuning |    0    |  54.49 | 74.96 | 12.32 |
| test                  |   26.71 |  81.19 | 89.98 | 87.43 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   55.85 |  88.68 | 93.9  | 90.43 |
| abstracts            |   50.95 |  87.42 | 93.35 | 95.91 |
| news                 |   73.92 |  93.31 | 96.15 | 97.26 |
| reviews              |   25.94 |  80.81 | 89.87 | 79.69 |
| student_essays       |   52.37 |  87.79 | 89.02 | 88.17 |
| tweets               |    0    |  57.73 | 82.42 | 81.04 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    0    |  48.76 | 60.96 |  1.14 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  48.81 | 47.26 |  0.35 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |    0    |  50.05 | 80.03 |  4.1  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |    0    |  51.77 | 67.01 |  1.23 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  53.84 | 55.27 |  1.32 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    0    |  54.49 | 74.96 | 12.32 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |    0    |  56.07 | 72.48 |  1.11 |
| gemini-1.5-pro                                                                     |    0    |  71.41 | 81    | 48.75 |
| llama-3.2-90b                                                                      |    2.35 |  73.65 | 86.16 | 54.77 |
| gemini-1.5-flash                                                                   |   14.14 |  77.89 | 88.07 | 62.41 |
| llama-3.3-70b                                                                      |   14.61 |  78.01 | 85.53 | 61.93 |
| claude-3-5-sonnet-20241022                                                         |   27.25 |  81.29 | 92.15 | 68.9  |
| mistral-large-latest                                                               |   37.01 |  83.84 | 93.13 | 73.62 |
| gpt-4o-2024-11-20                                                                  |   38.53 |  84.23 | 89.3  | 73.28 |
| DeepSeek-V3                                                                        |   40.48 |  84.73 | 92.57 | 74.91 |
| claude-3-5-haiku-20241022                                                          |   41.64 |  85.03 | 92.47 | 75.23 |
| mistral-small-latest                                                               |   43.59 |  85.53 | 96.53 | 79.06 |
| gpt-4o-mini                                                                        |   51.28 |  87.51 | 92.89 | 79.21 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   79.95 |  94.86 | 98.95 | 96.97 |
| abstracts            |   70.73 |  92.49 | 95.85 | 97.24 |
| news                 |   93.63 |  98.37 | 99.61 | 99.62 |
| reviews              |   44.27 |  85.61 | 94.37 | 85.63 |
| student_essays       |   78.15 |  94.4  | 94.94 | 94.46 |
| tweets               |    0    |  58.61 | 82.98 | 79.52 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |       0 |  51.79 | 67.35 | 87.91 |
| 538Tweets/lefttroll  |       0 |  59.28 | 82.52 | 74.9  |
| 538Tweets/righttroll |       0 |  60.85 | 83.95 | 76.29 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   27.87 |  81.15 | 90.61 | 78.48 |
|       2 |   45.75 |  85.95 | 94.56 | 85.84 |
|       3 |   46.71 |  86.28 | 95.89 | 87.54 |
|       4 |   50.58 |  87.27 | 95.27 | 87.8  |
|       5 |   57.6  |  89.13 | 95.46 | 89.34 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   79.7  |  94.79 | 97.55 | 98.4  |
| arxiv/astro-ph.CO        |   89.72 |  97.37 | 98.76 | 99.13 |
| arxiv/astro-ph.GA        |   86.75 |  96.59 | 98.71 | 99.12 |
| arxiv/astro-ph.HE        |   87.21 |  96.71 | 98.3  | 98.91 |
| arxiv/astro-ph.SR        |   87.27 |  96.71 | 98.72 | 99.13 |
| arxiv/cond-mat.mes-hall  |   77.7  |  94.28 | 97.54 | 98.29 |
| arxiv/cond-mat.mtrl-sci  |   76.77 |  94.06 | 97.4  | 98.29 |
| arxiv/cond-mat.stat-mech |   66.88 |  91.48 | 95.47 | 97.06 |
| arxiv/cond-mat.str-el    |   80.48 |  95    | 97.29 | 98.19 |
| arxiv/cs.CV              |   83.31 |  95.7  | 98.65 | 98.98 |
| arxiv/gr-qc              |   67.42 |  91.66 | 95.71 | 97.03 |
| arxiv/hep-ph             |   62.36 |  90.36 | 94.49 | 96.39 |
| arxiv/hep-th             |   61.62 |  90.16 | 93.9  | 95.64 |
| arxiv/math.AG            |   60.5  |  89.88 | 92.49 | 95.4  |
| arxiv/math.AP            |   59.09 |  89.53 | 91.98 | 95.06 |
| arxiv/math.CO            |   60.87 |  89.96 | 91.92 | 94.99 |
| arxiv/math.NT            |   56.06 |  88.73 | 90.84 | 94.48 |
| arxiv/math.PR            |   57.43 |  89.11 | 93.47 | 95.73 |
| arxiv/nucl-th            |   61.76 |  90.21 | 94.3  | 95.98 |
| arxiv/quant-ph           |   71.58 |  92.72 | 95.17 | 96.88 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   91.24 |  97.75 | 99.64 | 99.71 |
| real   |   95.55 |  98.86 | 99.62 | 99.42 |

| topic           |   tpAUC |   pAUC |    AUC |     AP |
|:----------------|--------:|-------:|-------:|-------:|
| Government News |   78.18 |  94.41 |  98.9  |  99.63 |
| Middle-east     |   97.62 |  99.39 |  99.83 |  99.97 |
| News            |  100    | 100    | 100    | 100    |
| US_News         |   98.67 |  99.66 |  99.95 |  99.99 |
| left-news       |   92.65 |  98.14 |  99.79 |  99.8  |
| politics        |   85.1  |  96.2  |  99.54 |  99.31 |
| politicsNews    |   97.21 |  99.29 |  99.78 |  99.63 |
| worldnews       |   93.65 |  98.37 |  99.4  |  99.16 |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| Fox New                  |   91.57 |  97.84 | 99.78 | 97.97 |
| ABC                      |   91.72 |  97.87 | 99.37 | 97.8  |
| NBC                      |   92.99 |  98.2  | 99.52 | 98.12 |
| The Daily Telegraph (UK) |   93.55 |  98.34 | 99.55 | 98.26 |
| The Times (UK)           |   93.96 |  98.45 | 99.37 | 98.23 |
| CNN                      |   94.07 |  98.48 | 99.76 | 98.51 |
| The Guardian (UK)        |   94.83 |  98.67 | 99.7  | 98.61 |
| The Sunday Times (UK)    |   96.35 |  99.06 | 99.86 | 99.12 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |   48.69 |  86.83 | 92.24 | 90.06 |
| ELLIPSE(Human)+   |   99.81 |  99.95 | 99.99 | 99.99 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |   98.31 |  99.57 | 99.87 | 99.79 |
| Ivy Panda(Human)+ |    8.08 |  76.17 | 74.37 | 61.5  |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |    0    |  52.06 | 51.94 |  3.27 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |    0    |  52.84 | 56.75 |  1.89 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |    0.23 |  56.24 | 60.96 |  5.56 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |    5.25 |  61.91 | 66.56 |  5.98 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |    7.89 |  63.29 | 65.71 |  4.64 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   12.75 |  64.23 | 72.74 | 19.89 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   14.72 |  62.9  | 78.45 | 16.72 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   16.04 |  67.68 | 73.42 |  6.72 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   20.14 |  67.48 | 80.2  | 21.89 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   28.38 |  73.65 | 72.67 | 30.65 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   38.45 |  77.19 | 81.49 | 33.68 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   44.04 |  79.47 | 86.45 | 49.42 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ✅     | ✅               | ❌                     |
| Base      | ❌       | ❌        | ❌          | ❌     | ❌               | ✅                     |

