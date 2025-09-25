# binoculars - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 50.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |    0    |  49.08 | 43.8  |  3.61 |
| test-1b-no-finetuning |    0    |  51.6  | 57.08 |  6.14 |
| test                  |   22.49 |  77.56 | 90.3  | 86.8  |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   62.34 |  90.28 | 92.08 | 89.25 |
| abstracts            |   12.85 |  76.02 | 85.58 | 90.91 |
| news                 |   63.89 |  90.63 | 89.58 | 93.33 |
| reviews              |    0    |  57.97 | 81.64 | 46    |
| student_essays       |   63.76 |  90.71 | 92.23 | 91.39 |
| tweets               |    0    |  62.1  | 78.55 | 81.94 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  48.72 | 59.43 |  0.71 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |    0    |  48.72 | 60.27 |  0.38 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |    0    |  48.75 | 36.84 |  0.37 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |    0    |  48.84 | 46.66 |  1.4  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    0    |  49.34 | 23.79 |  0.6  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  50.71 | 51.85 |  0.51 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    0    |  51.6  | 57.08 |  6.14 |
| claude-3-5-haiku-20241022                                                          |    4.18 |  68.54 | 81.38 | 31.25 |
| claude-3-5-sonnet-20241022                                                         |    4.6  |  67.79 | 87.05 | 32.42 |
| gemini-1.5-pro                                                                     |    7.28 |  72.04 | 84.25 | 40.32 |
| gpt-4o-2024-11-20                                                                  |   20.58 |  76.51 | 89.42 | 49.93 |
| gemini-1.5-flash                                                                   |   21.44 |  77.56 | 90.27 | 52.93 |
| llama-3.3-70b                                                                      |   23.59 |  78.49 | 92.02 | 55.92 |
| mistral-large-latest                                                               |   30.3  |  79.75 | 92.86 | 55.58 |
| DeepSeek-V3                                                                        |   31.38 |  80.45 | 91.21 | 56.84 |
| llama-3.2-90b                                                                      |   32.39 |  81.33 | 93.19 | 61.62 |
| gpt-4o-mini                                                                        |   45.44 |  84.15 | 95.02 | 63.24 |
| mistral-small-latest                                                               |   51.95 |  86.55 | 96.61 | 70.11 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   90.88 |  97.6  | 99.15 | 98.06 |
| abstracts            |   28.25 |  80.67 | 91.95 | 93.98 |
| news                 |   93.06 |  98.13 | 99.25 | 99.33 |
| reviews              |    0    |  59.3  | 85.66 | 47.08 |
| student_essays       |   92.16 |  97.99 | 98.9  | 98.55 |
| tweets               |    0    |  64.02 | 83.12 | 83.25 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |    0    |  55.71 | 78.71 | 92.88 |
| 538Tweets/lefttroll  |    0    |  62.95 | 80.67 | 77.01 |
| 538Tweets/righttroll |    2.78 |  70.03 | 86.2  | 83.68 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |       0 |  60.1  | 85.76 | 48.3  |
|       2 |       0 |  64.72 | 86.19 | 54.61 |
|       3 |       0 |  60.94 | 86.38 | 50.83 |
|       4 |       0 |  58.13 | 85.99 | 45.51 |
|       5 |       0 |  54.81 | 84.2  | 40.55 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   43.59 |  85.35 | 94.22 | 95.9  |
| arxiv/astro-ph.CO        |   63.71 |  90.72 | 96.4  | 97.43 |
| arxiv/astro-ph.GA        |   75.04 |  93.59 | 97.73 | 98.37 |
| arxiv/astro-ph.HE        |   58.45 |  88.92 | 96.31 | 97.29 |
| arxiv/astro-ph.SR        |   59.6  |  89.29 | 96.14 | 97.18 |
| arxiv/cond-mat.mes-hall  |   39.37 |  84.18 | 95.97 | 96.62 |
| arxiv/cond-mat.mtrl-sci  |   61.82 |  90.26 | 96.8  | 97.71 |
| arxiv/cond-mat.stat-mech |   23.56 |  79.59 | 90.78 | 93.41 |
| arxiv/cond-mat.str-el    |   43.76 |  85.09 | 94.94 | 95.83 |
| arxiv/cs.CV              |   73.86 |  93.26 | 97.63 | 98.24 |
| arxiv/gr-qc              |   11.15 |  74.65 | 89.25 | 91.43 |
| arxiv/hep-ph             |    8.45 |  74.14 | 89.38 | 91.71 |
| arxiv/hep-th             |   17.07 |  77.94 | 89.46 | 91.67 |
| arxiv/math.AG            |    5.27 |  71.75 | 85.82 | 89.28 |
| arxiv/math.AP            |    9.01 |  74.3  | 89.35 | 91.85 |
| arxiv/math.CO            |    2.73 |  70.53 | 86.33 | 89.12 |
| arxiv/math.NT            |    2.54 |  69.73 | 83.78 | 87.7  |
| arxiv/math.PR            |    3.33 |  71.81 | 87.27 | 89.59 |
| arxiv/nucl-th            |   10.25 |  74.28 | 90.11 | 91.18 |
| arxiv/quant-ph           |   33.1  |  81.79 | 92.52 | 94.48 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   95.25 |  98.6  | 99.34 | 99.55 |
| real   |   87.96 |  96.91 | 98.98 | 98.48 |

| topic           |   tpAUC |   pAUC |    AUC |     AP |
|:----------------|--------:|-------:|-------:|-------:|
| Government News |   88.18 |  97.05 |  98.73 |  99.62 |
| Middle-east     |   95.73 |  98.9  |  98.87 |  99.84 |
| News            |   99.23 |  99.8  |  99.98 |  99.96 |
| US_News         |  100    | 100    | 100    | 100    |
| left-news       |   94.16 |  98.5  |  99.19 |  99.51 |
| politics        |   95.38 |  98.14 |  99.82 |  99.34 |
| politicsNews    |   89.33 |  97.28 |  99.32 |  98.8  |
| worldnews       |   88.03 |  96.92 |  98.8  |  98.39 |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| The Sunday Times (UK)    |   91.76 |  97.79 | 99.1  | 97.07 |
| The Times (UK)           |   92.28 |  97.93 | 99.14 | 97.21 |
| The Daily Telegraph (UK) |   92.39 |  97.94 | 99.28 | 97.33 |
| NBC                      |   92.93 |  98.1  | 99.38 | 97.6  |
| ABC                      |   93.63 |  98.27 | 99.19 | 97.5  |
| The Guardian (UK)        |   93.64 |  98.28 | 99.2  | 97.53 |
| CNN                      |   93.73 |  98.3  | 99.26 | 97.7  |
| Fox New                  |   94.17 |  98.42 | 99.42 | 97.87 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |   65.72 |  91.2  | 95.71 | 94.13 |
| ELLIPSE(Human)+   |   99.47 |  99.86 | 99.85 | 99.93 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |   99.51 |  99.87 | 99.85 | 99.86 |
| Ivy Panda(Human)+ |   67.54 |  91.68 | 95.63 | 89.45 |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |    0    |  44.77 | 33.68 |  4.69 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |    0    |  46.64 | 43.39 |  7.51 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |    0    |  46.97 | 38.85 |  6.09 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |    0    |  47.38 | 39.12 |  5.39 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |    0    |  49.14 | 52.5  |  1.47 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |    0    |  49.8  | 48.22 |  2.23 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |    0    |  50.52 | 55.01 |  3.23 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |    0    |  51.43 | 58.11 |  2.3  |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |    0    |  54.16 | 56.12 |  4.54 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |    0.22 |  55.84 | 57.64 | 13.05 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |    5.27 |  59.94 | 66.5  |  2.78 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |    8.15 |  62.91 | 68.06 | 17.47 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ✅     | ✅               | ❌                     |
| Base      | ❌       | ❌        | ❌          | ❌     | ❌               | ✅                     |

