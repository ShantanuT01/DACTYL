# daigt - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 50.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test                  |    0    |  69.9  | 77.05 | 73.18 |
| test-finetuning       |    0.01 |  67.88 | 86.35 | 34.84 |
| test-1b-no-finetuning |    1.41 |  70.65 | 87.22 | 44.25 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   30.62 |  81.51 | 92.17 | 84.14 |
| abstracts            |    1.06 |  70.91 | 83.12 | 88.66 |
| news                 |   60.17 |  89.54 | 96.18 | 96.89 |
| reviews              |    0    |  63.49 | 78.88 | 54.73 |
| student_essays       |   49.33 |  86.97 | 94.8  | 92.29 |
| tweets               |    0    |  54.56 | 55.14 | 62.73 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    0    |  48.85 | 64.94 |  1.27 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  49.48 | 70.79 |  0.65 |
| gemini-1.5-pro                                                                     |    0    |  60.31 | 61.84 | 23.21 |
| gemini-1.5-flash                                                                   |    0    |  62.04 | 67.54 | 26.92 |
| claude-3-5-haiku-20241022                                                          |    0    |  65.54 | 79.28 | 32.8  |
| claude-3-5-sonnet-20241022                                                         |    0    |  65.99 | 77.22 | 33.91 |
| gpt-4o-2024-11-20                                                                  |    0    |  69.73 | 77.29 | 43.22 |
| llama-3.2-90b                                                                      |    0    |  70.42 | 75.47 | 45.66 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |    0.43 |  64.7  | 92.21 | 14.43 |
| llama-3.3-70b                                                                      |    0.45 |  72.45 | 80.41 | 49.6  |
| mistral-large-latest                                                               |    0.64 |  71.77 | 79.66 | 47.4  |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    1.41 |  70.65 | 87.22 | 44.25 |
| mistral-small-latest                                                               |    6.24 |  75.1  | 78.26 | 53.97 |
| DeepSeek-V3                                                                        |   11.97 |  76.93 | 85.26 | 58.22 |
| gpt-4o-mini                                                                        |   17.96 |  78.59 | 85.26 | 60.77 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |   39.69 |  81.58 | 96.92 | 16.96 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |   69.28 |  91.15 | 98.99 | 24.03 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |   89.71 |  96.69 | 99.66 | 47.4  |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   26.51 |  80.65 | 91.17 | 81.2  |
| abstracts            |    0.07 |  70.06 | 81.17 | 85.82 |
| news                 |   65.26 |  90.92 | 96.26 | 96.7  |
| reviews              |    0    |  65.32 | 77.7  | 53.49 |
| student_essays       |   58.07 |  89.22 | 95.13 | 92.48 |
| tweets               |    0    |  52.36 | 50.1  | 53.05 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |       0 |  50.28 | 49.55 | 80.94 |
| 538Tweets/lefttroll  |       0 |  53.21 | 52.89 | 49.46 |
| 538Tweets/righttroll |       0 |  52.37 | 49.81 | 44.02 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |    0    |  66.21 | 74.65 | 51.68 |
|       2 |    0    |  63.44 | 77.91 | 50.8  |
|       3 |    0    |  64.28 | 77.19 | 51.94 |
|       4 |    0    |  65.35 | 79.17 | 55.02 |
|       5 |    1.79 |  70    | 80.18 | 60.62 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |    8.09 |  72.92 | 85.92 | 89.05 |
| arxiv/astro-ph.CO        |   11.64 |  75.11 | 89.69 | 91.85 |
| arxiv/astro-ph.GA        |   24.8  |  80.08 | 91.29 | 93.49 |
| arxiv/astro-ph.HE        |   15.4  |  76.82 | 89.2  | 91.77 |
| arxiv/astro-ph.SR        |   26.49 |  80.98 | 90.71 | 93.23 |
| arxiv/cond-mat.mes-hall  |    4.13 |  73.14 | 86.69 | 89.53 |
| arxiv/cond-mat.mtrl-sci  |    8.51 |  75.9  | 88.15 | 91.54 |
| arxiv/cond-mat.stat-mech |    0    |  67.84 | 79.7  | 84.92 |
| arxiv/cond-mat.str-el    |    0.85 |  72.03 | 84.14 | 87.31 |
| arxiv/cs.CV              |   25.22 |  80.75 | 90.72 | 93.25 |
| arxiv/gr-qc              |    1.54 |  72.46 | 83.17 | 87.19 |
| arxiv/hep-ph             |    0    |  66.14 | 77.66 | 83.02 |
| arxiv/hep-th             |    0    |  68.65 | 79.54 | 83.61 |
| arxiv/math.AG            |    0    |  62.01 | 76.03 | 80.49 |
| arxiv/math.AP            |    0    |  59.8  | 70.38 | 75.72 |
| arxiv/math.CO            |    0    |  57.79 | 69.22 | 74.05 |
| arxiv/math.NT            |    0    |  57.21 | 70.61 | 74.71 |
| arxiv/math.PR            |    0    |  63.44 | 72.68 | 78.87 |
| arxiv/nucl-th            |    0    |  69.98 | 80.99 | 84.59 |
| arxiv/quant-ph           |    4.68 |  72.53 | 83.39 | 87.57 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   58.35 |  89.1  | 95.13 | 96.71 |
| real   |   80.22 |  94.79 | 97.92 | 97.23 |

| topic           |   tpAUC |   pAUC |   AUC |    AP |
|:----------------|--------:|-------:|------:|------:|
| Government News |   70.97 |  92.53 | 94.19 | 98.22 |
| Middle-east     |   80.06 |  94.87 | 96.74 | 99.53 |
| News            |   52.41 |  87.75 | 94.19 | 93.27 |
| US_News         |   83.78 |  95.83 | 98.71 | 99.74 |
| left-news       |   67.08 |  91.59 | 96.1  | 97.24 |
| politics        |   63.74 |  90.26 | 96.64 | 96.19 |
| politicsNews    |   92.96 |  98.2  | 99.25 | 99    |
| worldnews       |   67.52 |  91.37 | 96.19 | 95.18 |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| The Sunday Times (UK)    |   60.61 |  89.73 | 96.05 | 87.32 |
| The Daily Telegraph (UK) |   62.51 |  90.22 | 96.08 | 88.28 |
| The Times (UK)           |   63.45 |  90.45 | 95.93 | 88.3  |
| Fox New                  |   64.29 |  90.67 | 95.89 | 88.77 |
| The Guardian (UK)        |   65.87 |  91.07 | 95.95 | 88.71 |
| NBC                      |   66.24 |  91.17 | 96.72 | 89.47 |
| ABC                      |   69.43 |  91.96 | 96.69 | 90.08 |
| CNN                      |   69.69 |  92.08 | 96.77 | 90.37 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |   46.91 |  86.34 | 93.9  | 90.94 |
| ELLIPSE(Human)+   |   78.32 |  94.43 | 98.43 | 98.96 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |   64.55 |  90.89 | 96.33 | 93.98 |
| Ivy Panda(Human)+ |   28.76 |  81.6  | 88.46 | 73.82 |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   33.54 |  72.33 | 83.64 |  4.87 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   36.3  |  76.76 | 81.53 | 43.87 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   43.37 |  79.32 | 84.13 | 46.77 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   44.5  |  77.14 | 87.07 |  6.63 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   63.82 |  86.68 | 92.59 | 58.85 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |   67.93 |  88.37 | 92.26 | 45.62 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |   70.87 |  89.1  | 93.76 | 34.75 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   72.54 |  89.65 | 92.73 | 54.24 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   76.42 |  91.63 | 95.06 | 77.12 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   83.84 |  94.09 | 96.59 | 47.43 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   94.09 |  97.64 | 98.79 | 50.37 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   94.51 |  97.6  | 98.78 | 72.35 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ❌     | ❌               | ❌                     |
| Base      | ❌       | ❌        | ❌          | ✅     | ✅               | ✅                     |

