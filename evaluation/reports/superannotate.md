# superannotate - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 50.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |    0    |  48.96 | 36.07 |  3.06 |
| test-1b-no-finetuning |    0    |  50.96 | 47.9  |  4.54 |
| test                  |   26.17 |  77.74 | 91.84 | 86.17 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   38.3  |  80.94 | 89.47 | 79.74 |
| abstracts            |   49.94 |  86.67 | 89.74 | 94.19 |
| news                 |   44.95 |  83.5  | 85.27 | 89.79 |
| reviews              |   22.34 |  76.47 | 87.91 | 71.4  |
| student_essays       |   11.36 |  67.26 | 86.88 | 74.52 |
| tweets               |    0    |  52.41 | 50.9  | 57.91 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |    0    |  48.72 | 21.97 |  0.31 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |    0    |  48.72 | 28.86 |  0.21 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  48.94 | 40.75 |  0.48 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |    0    |  48.97 | 25.88 |  0.99 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    0    |  49.06 | 60.46 |  1.19 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  49.22 | 34.84 |  0.29 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    0    |  50.96 | 47.9  |  4.54 |
| llama-3.2-90b                                                                      |    8.12 |  71.36 | 87.01 | 35.98 |
| gemini-1.5-pro                                                                     |   12.1  |  72.52 | 90.64 | 39.26 |
| claude-3-5-sonnet-20241022                                                         |   18.11 |  74.23 | 92.05 | 41.36 |
| llama-3.3-70b                                                                      |   19.54 |  75.52 | 88.95 | 42.5  |
| gemini-1.5-flash                                                                   |   28.41 |  78.27 | 93.71 | 50.13 |
| claude-3-5-haiku-20241022                                                          |   30.68 |  79.11 | 91.19 | 49.48 |
| mistral-large-latest                                                               |   30.85 |  79.61 | 92.08 | 51.89 |
| mistral-small-latest                                                               |   33.03 |  80.21 | 92.8  | 53.31 |
| DeepSeek-V3                                                                        |   34.63 |  79.8  | 92.88 | 50.91 |
| gpt-4o-2024-11-20                                                                  |   37    |  80.95 | 94.73 | 54.6  |
| gpt-4o-mini                                                                        |   43.65 |  83.59 | 94.19 | 60.29 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   59.23 |  86.71 | 98.21 | 88.29 |
| abstracts            |   74.88 |  93.14 | 98.14 | 98.46 |
| news                 |   68.44 |  89.78 | 98.11 | 96.82 |
| reviews              |   38.5  |  81.07 | 95.32 | 78.36 |
| student_essays       |   20.3  |  70.38 | 95.22 | 80.13 |
| tweets               |    0    |  52.89 | 53.15 | 56.09 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |       0 |  54.9  | 45.86 | 81.68 |
| 538Tweets/lefttroll  |       0 |  52.28 | 58.27 | 53.02 |
| 538Tweets/righttroll |       0 |  55.47 | 52.56 | 48.34 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   43.79 |  84.03 | 93.89 | 81.54 |
|       2 |   53    |  86.72 | 95.93 | 84.98 |
|       3 |   54.78 |  87.14 | 96.97 | 86.96 |
|       4 |   30.49 |  76.75 | 96.32 | 74.78 |
|       5 |   23.7  |  74.53 | 95.23 | 71.58 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   86.86 |  96.63 | 99.16 | 99.35 |
| arxiv/astro-ph.CO        |   88.37 |  96.9  | 99.53 | 99.54 |
| arxiv/astro-ph.GA        |   81.95 |  94.73 | 99.03 | 99.1  |
| arxiv/astro-ph.HE        |   82.87 |  95.57 | 98.54 | 98.99 |
| arxiv/astro-ph.SR        |   79.69 |  92.53 | 99.08 | 98.57 |
| arxiv/cond-mat.mes-hall  |   78.17 |  93.9  | 98.48 | 98.71 |
| arxiv/cond-mat.mtrl-sci  |   80.44 |  95.01 | 98.66 | 99.02 |
| arxiv/cond-mat.stat-mech |   85.8  |  96.34 | 98.23 | 98.88 |
| arxiv/cond-mat.str-el    |   86.42 |  96.53 | 98.77 | 99.04 |
| arxiv/cs.CV              |   61.24 |  87.1  | 98.13 | 97.39 |
| arxiv/gr-qc              |   89.75 |  97.38 | 98.95 | 99.27 |
| arxiv/hep-ph             |   75.79 |  93.81 | 98.24 | 98.72 |
| arxiv/hep-th             |   85    |  96.16 | 98.15 | 98.66 |
| arxiv/math.AG            |   82.23 |  95.45 | 97.75 | 98.57 |
| arxiv/math.AP            |   83.29 |  95.73 | 98.42 | 98.96 |
| arxiv/math.CO            |   75.88 |  93.8  | 97.6  | 98.29 |
| arxiv/math.NT            |   77.05 |  94.1  | 97.88 | 98.51 |
| arxiv/math.PR            |   83.43 |  95.77 | 98.47 | 98.92 |
| arxiv/nucl-th            |   83.02 |  95.66 | 98.56 | 98.84 |
| arxiv/quant-ph           |   78.1  |  92.74 | 97.83 | 97.86 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   61.1  |  86.37 | 98.15 | 97.06 |
| real   |   72.81 |  92.51 | 97.81 | 96.3  |

| topic           |   tpAUC |   pAUC |   AUC |    AP |
|:----------------|--------:|-------:|------:|------:|
| Government News |   75.09 |  90.25 | 98.05 | 98.39 |
| Middle-east     |   83.98 |  95.84 | 99.35 | 99.89 |
| News            |   34.02 |  76.15 | 97.57 | 90.25 |
| US_News         |   92.02 |  97.93 | 99.77 | 99.95 |
| left-news       |   75.78 |  91.85 | 98.98 | 98.44 |
| politics        |   87.05 |  96.69 | 99.36 | 99.06 |
| politicsNews    |   77.18 |  93.94 | 97.78 | 96.74 |
| worldnews       |   71.34 |  91.77 | 98.02 | 96.15 |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| The Times (UK)           |   64.87 |  88.74 | 97.83 | 80.96 |
| The Daily Telegraph (UK) |   65.26 |  88.82 | 97.76 | 80.73 |
| The Guardian (UK)        |   65.78 |  88.9  | 97.64 | 80.56 |
| The Sunday Times (UK)    |   65.84 |  88.95 | 98.15 | 81.39 |
| ABC                      |   69.82 |  90.32 | 97.88 | 83.12 |
| Fox New                  |   70.9  |  90.38 | 98.46 | 83.31 |
| NBC                      |   72.19 |  90.87 | 98.61 | 84.18 |
| CNN                      |   73.21 |  91.26 | 98.54 | 84.85 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |   54.52 |  87.73 | 94.28 | 91.16 |
| ELLIPSE(Human)+   |   95.71 |  98.53 | 99.82 | 99.78 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |   16.38 |  68.19 | 96.58 | 80.26 |
| Ivy Panda(Human)+ |    0    |  55.41 | 86.79 | 33.35 |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |       0 |  41.25 |  9.28 |  3.56 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |       0 |  42.25 | 37.72 |  1.42 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |       0 |  43.22 | 35.78 |  2.1  |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |       0 |  43.7  | 20.09 |  3.94 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |       0 |  44.79 | 37.94 |  5.88 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |       0 |  44.83 | 39.05 |  1.09 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |       0 |  44.94 | 34.45 |  6.47 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |       0 |  46.8  | 45.08 |  1.9  |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |       0 |  47.94 | 39.06 |  6.77 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |       0 |  49.52 | 46.21 |  3.3  |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |       0 |  53.44 | 55.22 |  2.56 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |       0 |  54.36 | 52.59 | 13.31 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ✅     | ✅               | ✅                     |
| Base      | ❌       | ❌        | ❌          | ❌     | ❌               | ❌                     |

