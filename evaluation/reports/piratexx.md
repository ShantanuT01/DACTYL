# piratexx - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 50.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |       0 |  51.15 | 54.84 |  5.43 |
| test                  |       0 |  53.84 | 68.26 | 49.49 |
| test-1b-no-finetuning |       0 |  55.7  | 62.39 | 12.34 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |    4.72 |  72.27 | 85.13 | 71.61 |
| abstracts            |    0    |  57.92 | 82.71 | 83.95 |
| news                 |    0    |  62.22 | 75.83 | 77.36 |
| reviews              |    0    |  56.5  | 68.09 | 33.12 |
| student_essays       |    0    |  63.77 | 80.36 | 68.17 |
| tweets               |    0    |  51.7  | 39.89 | 50.53 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |       0 |  48.72 | 35.27 |  0.23 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |       0 |  48.85 | 48.47 |  0.55 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |       0 |  48.89 | 37.49 |  1.15 |
| claude-3-5-sonnet-20241022                                                         |       0 |  49.13 | 51.29 |  4.04 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |       0 |  49.24 | 69.22 |  0.77 |
| claude-3-5-haiku-20241022                                                          |       0 |  49.81 | 58.09 |  4.77 |
| gemini-1.5-flash                                                                   |       0 |  51.44 | 71.1  |  7.64 |
| gemini-1.5-pro                                                                     |       0 |  51.84 | 70.38 |  8.14 |
| gpt-4o-2024-11-20                                                                  |       0 |  53.13 | 69.25 |  8.51 |
| gpt-4o-mini                                                                        |       0 |  53.17 | 75.01 |  9.41 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |       0 |  53.38 | 77.18 |  2.79 |
| DeepSeek-V3                                                                        |       0 |  53.47 | 68.23 |  8.34 |
| mistral-large-latest                                                               |       0 |  53.85 | 69.95 |  9.25 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |       0 |  55.7  | 62.39 | 12.34 |
| mistral-small-latest                                                               |       0 |  57.1  | 76.14 | 15.45 |
| llama-3.3-70b                                                                      |       0 |  59    | 69.48 | 16.41 |
| llama-3.2-90b                                                                      |       0 |  60.26 | 71.98 | 19.07 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |       0 |  62.75 | 77.81 |  4.63 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   16.01 |  76.3  | 91.01 | 77.03 |
| abstracts            |    0    |  58    | 84.16 | 82.57 |
| news                 |    0    |  64.6  | 82.61 | 80.28 |
| reviews              |    0    |  55.52 | 66.68 | 27.46 |
| student_essays       |    0    |  66.33 | 86.31 | 72.01 |
| tweets               |    0    |  49.96 | 36.65 | 41.6  |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |       0 |  49.25 | 32.65 | 74.18 |
| 538Tweets/lefttroll  |       0 |  50    | 36.96 | 35.41 |
| 538Tweets/righttroll |       0 |  50.08 | 37.8  | 33.57 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |       0 |  53.6  | 61.44 | 22.04 |
|       2 |       0 |  55.26 | 69.9  | 29.07 |
|       3 |       0 |  57.17 | 69.89 | 32.86 |
|       4 |       0 |  55.9  | 68.66 | 28.46 |
|       5 |       0 |  55.66 | 63.33 | 26.11 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |    0.83 |  63.69 | 88.31 | 87.8  |
| arxiv/astro-ph.CO        |    2.89 |  68.5  | 91.47 | 91.45 |
| arxiv/astro-ph.GA        |   17.48 |  76.53 | 93.7  | 94.26 |
| arxiv/astro-ph.HE        |   11.65 |  74.26 | 92.46 | 92.9  |
| arxiv/astro-ph.SR        |    4.46 |  69.5  | 92.22 | 92.09 |
| arxiv/cond-mat.mes-hall  |    0    |  62.54 | 89.68 | 87.97 |
| arxiv/cond-mat.mtrl-sci  |    2.89 |  68.95 | 91.02 | 91.83 |
| arxiv/cond-mat.stat-mech |    0    |  58.15 | 83.95 | 83.05 |
| arxiv/cond-mat.str-el    |    0.89 |  67.31 | 89.47 | 88.88 |
| arxiv/cs.CV              |    0    |  58.07 | 87.55 | 84.54 |
| arxiv/gr-qc              |    0    |  56.9  | 82.87 | 80.91 |
| arxiv/hep-ph             |    0    |  56.54 | 81.23 | 80.15 |
| arxiv/hep-th             |    0    |  55.11 | 81.5  | 78.02 |
| arxiv/math.AG            |    0    |  55.38 | 78.58 | 78.36 |
| arxiv/math.AP            |    0    |  53.02 | 73.59 | 73.18 |
| arxiv/math.CO            |    0    |  52.57 | 71.37 | 69.6  |
| arxiv/math.NT            |    0    |  52.19 | 69.67 | 69.43 |
| arxiv/math.PR            |    0    |  55.91 | 77.69 | 76.97 |
| arxiv/nucl-th            |    0    |  61.32 | 85.48 | 83.74 |
| arxiv/quant-ph           |    0    |  56.65 | 81.92 | 80.14 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |    0    |  64.72 | 87    | 87.7  |
| real   |    0.12 |  68.39 | 85.74 | 76.06 |

| topic           |   tpAUC |   pAUC |   AUC |    AP |
|:----------------|--------:|-------:|------:|------:|
| Government News |    0    |  57.17 | 77.93 | 89.18 |
| Middle-east     |    8.73 |  73.3  | 94.16 | 98.91 |
| News            |    9.32 |  74.52 | 90.21 | 85.12 |
| US_News         |   57.31 |  89.02 | 96.56 | 99.27 |
| left-news       |    0    |  62.87 | 85.75 | 85.45 |
| politics        |    0    |  62.31 | 85.64 | 76.65 |
| politicsNews    |    0    |  66.28 | 83.81 | 73.11 |
| worldnews       |    2.92 |  72.31 | 89.98 | 82.8  |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| The Times (UK)           |       0 |  63.94 | 81.51 | 41.54 |
| The Sunday Times (UK)    |       0 |  64.25 | 81.45 | 42.79 |
| Fox New                  |       0 |  64.33 | 81.51 | 42.82 |
| The Daily Telegraph (UK) |       0 |  64.37 | 81.42 | 42.46 |
| The Guardian (UK)        |       0 |  64.68 | 82.3  | 44.46 |
| NBC                      |       0 |  64.98 | 84.12 | 44.89 |
| CNN                      |       0 |  65.08 | 84.54 | 46.04 |
| ABC                      |       0 |  65.12 | 84    | 45.88 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |   18.46 |  77.16 | 91.08 | 85.15 |
| ELLIPSE(Human)+   |    1.85 |  67.55 | 92.46 | 92.74 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |    0    |  63.39 | 84.57 | 67.07 |
| Ivy Panda(Human)+ |    8.73 |  74.04 | 85.62 | 62.08 |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |    0    |  44.12 | 41.4  |  5.16 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |    0    |  46.08 | 35.78 |  4.9  |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |    0    |  48.2  | 46.85 |  2.73 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |    0    |  48.28 | 48.4  |  2.76 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |    0    |  49.58 | 38.92 | 10.12 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |    0    |  51.13 | 50.62 |  2.16 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |    0    |  52.44 | 54.94 |  2.33 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |    5.64 |  61.47 | 68    | 18.63 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |    7.8  |  64.4  | 71.69 |  6.83 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   23.94 |  72.28 | 79.94 | 15.3  |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   29.01 |  74.57 | 76.49 | 47.44 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   30.65 |  73.93 | 81.43 | 36.04 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ✅          | ✅     | ❌               | ❌                     |
| Base      | ❌       | ❌        | ❌          | ❌     | ✅               | ✅                     |

