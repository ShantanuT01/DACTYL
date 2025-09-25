# e5lora - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 50.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |       0 |  50.27 | 47.95 |  4.17 |
| test-1b-no-finetuning |       0 |  51.32 | 60.82 |  6.13 |
| test                  |       0 |  61.66 | 79.38 | 70.32 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |    0.18 |  68.8  | 83.18 | 67.68 |
| abstracts            |   10.07 |  75.79 | 86.5  | 91.14 |
| news                 |   45.41 |  85.99 | 91.33 | 93.39 |
| reviews              |    0    |  57.76 | 79.24 | 43.87 |
| student_essays       |   12.17 |  74.34 | 89.66 | 82.84 |
| tweets               |    0    |  52.7  | 70.47 | 70.1  |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |    0    |  48.72 | 31.47 |  1.06 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    0    |  48.72 | 39.49 |  0.72 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  48.72 | 50.46 |  0.38 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |    0    |  49.4  | 53.99 |  0.34 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |    0    |  49.77 | 66.86 |  0.79 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    0    |  51.32 | 60.82 |  6.13 |
| gemini-1.5-pro                                                                     |    0    |  57.88 | 77.49 | 18.83 |
| claude-3-5-sonnet-20241022                                                         |    0    |  58.04 | 73.32 | 18.33 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  58.53 | 83.16 |  3.13 |
| gpt-4o-2024-11-20                                                                  |    0    |  60.16 | 80.06 | 24.08 |
| claude-3-5-haiku-20241022                                                          |    0    |  60.98 | 75.42 | 24.1  |
| DeepSeek-V3                                                                        |    0    |  61.14 | 81.41 | 26.37 |
| gemini-1.5-flash                                                                   |    0    |  61.42 | 83.25 | 26.91 |
| llama-3.2-90b                                                                      |    0    |  62.42 | 74.25 | 27.59 |
| llama-3.3-70b                                                                      |    0    |  62.5  | 73.28 | 27.81 |
| mistral-large-latest                                                               |    0    |  63.03 | 80.63 | 28.74 |
| mistral-small-latest                                                               |    0    |  63.57 | 88.97 | 32.19 |
| gpt-4o-mini                                                                        |    1.71 |  67.16 | 85.07 | 37.7  |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |    4.34 |  71.78 | 86.32 | 70.6  |
| abstracts            |   25.64 |  80.43 | 93.09 | 94.38 |
| news                 |   69.06 |  92.06 | 97.22 | 97.37 |
| reviews              |    0    |  59.04 | 83.33 | 45.08 |
| student_essays       |   25.34 |  78.49 | 94.03 | 87.02 |
| tweets               |    0    |  52.67 | 70.63 | 66.5  |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |       0 |  51.56 | 68.65 | 88.29 |
| 538Tweets/lefttroll  |       0 |  51.89 | 68.27 | 57.18 |
| 538Tweets/righttroll |       0 |  54.94 | 74.04 | 63.63 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |       0 |  60.91 | 83.18 | 47.94 |
|       2 |       0 |  62.78 | 85.63 | 52.29 |
|       3 |       0 |  60.53 | 85.39 | 49.27 |
|       4 |       0 |  58.26 | 83.32 | 43.99 |
|       5 |       0 |  57.63 | 80.49 | 40.09 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   26.7  |  81.08 | 93.5  | 95.05 |
| arxiv/astro-ph.CO        |   45.03 |  85.93 | 95.81 | 96.67 |
| arxiv/astro-ph.GA        |   33.6  |  82.87 | 95.12 | 96.08 |
| arxiv/astro-ph.HE        |   43.9  |  85.24 | 95.2  | 96.35 |
| arxiv/astro-ph.SR        |   43.38 |  85.04 | 95.59 | 96.39 |
| arxiv/cond-mat.mes-hall  |   51.11 |  87.46 | 95.81 | 96.79 |
| arxiv/cond-mat.mtrl-sci  |   39.83 |  84.64 | 95.8  | 96.78 |
| arxiv/cond-mat.stat-mech |   39.2  |  84.19 | 93.81 | 95.53 |
| arxiv/cond-mat.str-el    |   37.2  |  83.31 | 94.87 | 95.66 |
| arxiv/cs.CV              |   63.37 |  89.52 | 97.23 | 96.98 |
| arxiv/gr-qc              |   25.95 |  80.7  | 92.45 | 94.02 |
| arxiv/hep-ph             |   17.65 |  76.21 | 92.13 | 93.39 |
| arxiv/hep-th             |   27.08 |  81.13 | 91.74 | 93.22 |
| arxiv/math.AG            |   11.12 |  76.34 | 90.05 | 92.39 |
| arxiv/math.AP            |   24.67 |  80.19 | 92.17 | 93.95 |
| arxiv/math.CO            |   21.79 |  79.26 | 92.94 | 94.24 |
| arxiv/math.NT            |    6.32 |  74.42 | 87.26 | 90.31 |
| arxiv/math.PR            |   20.86 |  79.71 | 92.46 | 93.95 |
| arxiv/nucl-th            |   37.54 |  83.56 | 93.09 | 94.43 |
| arxiv/quant-ph           |   48.07 |  86.72 | 95.65 | 96.68 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   66.18 |  91.31 | 97.63 | 98.18 |
| real   |   71.91 |  92.8  | 96.53 | 95.63 |

| topic           |   tpAUC |   pAUC |   AUC |    AP |
|:----------------|--------:|-------:|------:|------:|
| Government News |   66.88 |  91.47 | 97.14 | 99.04 |
| Middle-east     |   40.38 |  84.51 | 96.79 | 99.46 |
| News            |   46.84 |  86.37 | 96.13 | 93.98 |
| US_News         |   70.08 |  92.3  | 97.41 | 99.47 |
| left-news       |   84.11 |  95.96 | 98.61 | 98.96 |
| politics        |   69.16 |  92.12 | 97.94 | 97.41 |
| politicsNews    |   74.06 |  93.37 | 98.11 | 96.95 |
| worldnews       |   69.94 |  92.29 | 95.28 | 94.57 |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| The Sunday Times (UK)    |   61.6  |  90.15 | 96.99 | 88.87 |
| The Daily Telegraph (UK) |   64.97 |  91.01 | 97.19 | 89.94 |
| The Times (UK)           |   66.21 |  91.33 | 97.08 | 90.18 |
| The Guardian (UK)        |   68.18 |  91.84 | 97.03 | 90.54 |
| NBC                      |   72.08 |  92.84 | 97.54 | 91.79 |
| Fox New                  |   72.88 |  93.04 | 97.09 | 91.54 |
| ABC                      |   73.04 |  93.08 | 97.08 | 91.6  |
| CNN                      |   73.49 |  93.2  | 97.72 | 92.26 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |    0.92 |  68.11 | 85.38 | 74.45 |
| ELLIPSE(Human)+   |    2.54 |  65.13 | 93.23 | 92.26 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |   43.86 |  84.9  | 96.98 | 92.5  |
| Ivy Panda(Human)+ |   21.02 |  79.33 | 86.91 | 70.92 |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |    0    |  43.19 | 39.4  |  6.82 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |    0    |  48.41 | 50.5  |  1.43 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |    0    |  49.1  | 51.14 |  6.94 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |    0.08 |  54.41 | 61.13 | 13.63 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |    0.44 |  55.23 | 63.06 |  2.2  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |    1.25 |  56.01 | 63.82 |  4.42 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |    1.89 |  59.32 | 66.77 | 16.41 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |    2.05 |  57.49 | 65.39 |  3.53 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |    3.67 |  59.16 | 66.36 |  4.38 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |    3.99 |  58.46 | 62.31 | 12.42 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |    5.46 |  60.86 | 67.34 |  6.15 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   21.95 |  68.76 | 76.94 | 22.13 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ✅     | ✅               | ✅                     |
| Base      | ❌       | ❌        | ❌          | ❌     | ❌               | ❌                     |

