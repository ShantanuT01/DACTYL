# mage - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 50.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |       0 |  49.97 | 60.73 |  5.56 |
| test-1b-no-finetuning |       0 |  50.58 | 68.72 |  7.12 |
| test                  |       0 |  56.43 | 77.03 | 61.52 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |    4.39 |  73.14 | 83.63 | 71.96 |
| abstracts            |    1.48 |  70.8  | 84.84 | 89.31 |
| news                 |    0    |  56.37 | 84.27 | 80.3  |
| reviews              |    0    |  60.74 | 76.78 | 47.45 |
| student_essays       |    0    |  52.57 | 79.81 | 54.66 |
| tweets               |    0    |  51.01 | 50.59 | 54.89 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |       0 |  48.72 | 57.72 |  0.44 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |       0 |  48.73 | 47.04 |  0.28 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |       0 |  48.85 | 72.06 |  1.6  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |       0 |  48.91 | 44.01 |  1.29 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |       0 |  50.58 | 68.72 |  7.12 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |       0 |  51.36 | 79.61 |  1.43 |
| claude-3-5-haiku-20241022                                                          |       0 |  53.11 | 66.7  |  8.81 |
| claude-3-5-sonnet-20241022                                                         |       0 |  53.48 | 66.6  |  8.61 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |       0 |  54.74 | 79.71 |  2.19 |
| gemini-1.5-pro                                                                     |       0 |  54.96 | 75.17 | 11.66 |
| gpt-4o-2024-11-20                                                                  |       0 |  55.71 | 76.99 | 13.18 |
| llama-3.3-70b                                                                      |       0 |  56.69 | 77.01 | 15.23 |
| gemini-1.5-flash                                                                   |       0 |  56.89 | 79.71 | 14.93 |
| llama-3.2-90b                                                                      |       0 |  57.18 | 75.05 | 14.43 |
| DeepSeek-V3                                                                        |       0 |  57.2  | 83.26 | 17.71 |
| mistral-large-latest                                                               |       0 |  57.7  | 76.59 | 15.09 |
| mistral-small-latest                                                               |       0 |  58.75 | 85.44 | 20.06 |
| gpt-4o-mini                                                                        |       0 |  59.04 | 84.83 | 20.92 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   14.91 |  76.75 | 86.91 | 75.58 |
| abstracts            |    6.45 |  73.46 | 87.14 | 89.85 |
| news                 |    0    |  57.5  | 89.89 | 82.37 |
| reviews              |    0    |  61.8  | 76.79 | 45.73 |
| student_essays       |    0    |  52.95 | 83.9  | 54.68 |
| tweets               |    0    |  50.59 | 48.64 | 48.83 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |       0 |  50.6  | 62.24 | 86.29 |
| 538Tweets/lefttroll  |       0 |  51.1  | 55.18 | 46.96 |
| 538Tweets/righttroll |       0 |  50.81 | 45.78 | 38.79 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |       0 |  60.52 | 73.81 | 42.26 |
|       2 |       0 |  63.75 | 77.92 | 49.88 |
|       3 |       0 |  62.07 | 77.77 | 47.34 |
|       4 |       0 |  60.19 | 77.69 | 43.15 |
|       5 |       0 |  62.64 | 77.21 | 47.47 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   20.92 |  79.62 | 90.78 | 93.19 |
| arxiv/astro-ph.CO        |   37.58 |  83.74 | 93.96 | 95.26 |
| arxiv/astro-ph.GA        |   41.54 |  84.66 | 93.78 | 95.34 |
| arxiv/astro-ph.HE        |   34.33 |  82.89 | 93.52 | 95.06 |
| arxiv/astro-ph.SR        |   26.64 |  80.81 | 94    | 95.01 |
| arxiv/cond-mat.mes-hall  |   16.25 |  78.16 | 90.7  | 92.85 |
| arxiv/cond-mat.mtrl-sci  |   16.78 |  77.11 | 91.1  | 93.09 |
| arxiv/cond-mat.stat-mech |    0    |  69.41 | 82.26 | 86.96 |
| arxiv/cond-mat.str-el    |    2.38 |  72.01 | 85.51 | 88.11 |
| arxiv/cs.CV              |   40.45 |  83.21 | 94.74 | 95.47 |
| arxiv/gr-qc              |   11.45 |  75.43 | 85.79 | 89.49 |
| arxiv/hep-ph             |    0    |  67.17 | 82.43 | 85.86 |
| arxiv/hep-th             |    3.19 |  72.63 | 81.86 | 86.01 |
| arxiv/math.AG            |    1.43 |  69.85 | 82.66 | 86.98 |
| arxiv/math.AP            |    0    |  65.27 | 81.52 | 84.6  |
| arxiv/math.CO            |    0    |  65.7  | 80.18 | 84.11 |
| arxiv/math.NT            |    0    |  66.44 | 80.7  | 85.22 |
| arxiv/math.PR            |    0.2  |  68.6  | 81.9  | 85.9  |
| arxiv/nucl-th            |    2.21 |  71.81 | 84.45 | 87.44 |
| arxiv/quant-ph           |    8.2  |  74.11 | 88.74 | 90.94 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   22.47 |  72.53 | 95.15 | 93.92 |
| real   |    0    |  53.99 | 84.83 | 60.86 |

| topic           |   tpAUC |   pAUC |   AUC |    AP |
|:----------------|--------:|-------:|------:|------:|
| Government News |    0    |  56.55 | 90.06 | 94.27 |
| Middle-east     |   35.47 |  75.65 | 97    | 99.16 |
| News            |   32.42 |  76.23 | 95.63 | 89.05 |
| US_News         |   50.86 |  85.45 | 97.34 | 99.26 |
| left-news       |   24.49 |  74.84 | 95.08 | 93.85 |
| politics        |   20.46 |  72.37 | 95.52 | 89.84 |
| politicsNews    |    0    |  52.08 | 79.99 | 50.57 |
| worldnews       |    4.51 |  61.94 | 90.34 | 76.82 |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| Fox New                  |       0 |  56.17 | 88.94 | 35.73 |
| The Guardian (UK)        |       0 |  57.13 | 89.37 | 37.56 |
| The Daily Telegraph (UK) |       0 |  57.33 | 89.48 | 37.48 |
| ABC                      |       0 |  57.38 | 90.56 | 38.8  |
| The Times (UK)           |       0 |  57.73 | 89.95 | 38.39 |
| CNN                      |       0 |  57.93 | 90.58 | 39.28 |
| The Sunday Times (UK)    |       0 |  58.13 | 89.77 | 38.6  |
| NBC                      |       0 |  58.18 | 90.46 | 39.44 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |   22.04 |  73.38 | 91.24 | 81.58 |
| ELLIPSE(Human)+   |   37.42 |  78.24 | 96.93 | 96.27 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |    0    |  52.34 | 82.91 | 50.97 |
| Ivy Panda(Human)+ |    0    |  51.7  | 73.96 | 18.93 |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |    0    |  48.67 | 53.2  |  6.77 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |    0    |  51.78 | 53.47 |  7.57 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |    0    |  51.89 | 56.91 |  3.57 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |    0    |  52.19 | 57.71 |  3.63 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |    0.08 |  55.63 | 62.71 | 14.09 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |    0.69 |  55.95 | 60.65 | 11.57 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |    1.47 |  59.39 | 61.88 | 16.21 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |    2.64 |  59.01 | 66.31 |  3.87 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |    2.74 |  59.03 | 64.84 |  4.12 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |    9.73 |  63.14 | 71.8  |  3.34 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   28.34 |  72.97 | 81.69 | 35.68 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   30.83 |  73.07 | 81.55 |  7.41 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ✅     | ❌               | ✅                     |
| Base      | ❌       | ❌        | ❌          | ❌     | ✅               | ❌                     |

