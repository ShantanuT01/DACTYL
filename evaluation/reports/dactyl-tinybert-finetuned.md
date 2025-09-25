# dactyl-tinybert-finetuned - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 80.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |    0    |  68.45 | 81.49 | 34.7  |
| test-1b-no-finetuning |    0    |  70.3  | 83.91 | 40.11 |
| test                  |   77.17 |  97.55 | 99.21 | 98.94 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   49.15 |  94.68 | 96.38 | 95.38 |
| abstracts            |   37.83 |  93.42 | 97.26 | 98.33 |
| news                 |   34.39 |  93.27 | 95.45 | 96.82 |
| reviews              |   42.29 |  93.77 | 97.87 | 94.93 |
| student_essays       |   13.42 |  90.8  | 93.5  | 92.63 |
| tweets               |   41.57 |  93.58 | 98.2  | 98.63 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  53.75 | 58.5  |  1.24 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |    0    |  57.32 | 61.54 |  1.74 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |    0    |  64.79 | 70.38 |  3.41 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |    0    |  68.31 | 86.91 | 18.47 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    0    |  70.3  | 83.91 | 40.11 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  76.9  | 94    | 10.81 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    1.28 |  81.83 | 96.44 | 31.17 |
| gemini-1.5-pro                                                                     |   36.52 |  93.15 | 97.53 | 88.76 |
| llama-3.2-90b                                                                      |   50.51 |  94.75 | 98.21 | 91.32 |
| gemini-1.5-flash                                                                   |   69.35 |  96.73 | 99.19 | 94.54 |
| gpt-4o-2024-11-20                                                                  |   76.48 |  97.48 | 99.21 | 95.67 |
| llama-3.3-70b                                                                      |   77.34 |  97.56 | 99.16 | 95.8  |
| claude-3-5-haiku-20241022                                                          |   79.12 |  97.75 | 99.33 | 96.11 |
| claude-3-5-sonnet-20241022                                                         |   90.36 |  98.91 | 99.71 | 97.89 |
| mistral-large-latest                                                               |   91.58 |  99.04 | 99.75 | 98.1  |
| mistral-small-latest                                                               |   91.83 |  99.05 | 99.64 | 98.03 |
| DeepSeek-V3                                                                        |   92.12 |  99.1  | 99.67 | 98.13 |
| gpt-4o-mini                                                                        |   96.39 |  99.53 | 99.92 | 98.69 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   87.24 |  98.61 | 99.62 | 99.14 |
| abstracts            |   81.32 |  97.93 | 99.27 | 99.46 |
| news                 |   87.11 |  98.68 | 99.46 | 99.52 |
| reviews              |   70.63 |  96.87 | 99.03 | 97.26 |
| student_essays       |   77    |  97.49 | 99.23 | 98.64 |
| tweets               |   63.68 |  96.12 | 98.78 | 98.97 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |   69.13 |  96.84 | 98.54 | 99.68 |
| 538Tweets/lefttroll  |   50.62 |  94.57 | 98.15 | 98.08 |
| 538Tweets/righttroll |   70.5  |  96.94 | 99.09 | 99.01 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   53.96 |  95.25 | 98.24 | 95.86 |
|       2 |   66.28 |  96.46 | 98.77 | 96.98 |
|       3 |   86.73 |  98.32 | 99.6  | 98.26 |
|       4 |   69.95 |  96.92 | 99.21 | 97.54 |
|       5 |   74.88 |  97.25 | 99.22 | 97.62 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   84.17 |  98.37 | 99.65 | 99.72 |
| arxiv/astro-ph.CO        |   88.29 |  98.13 | 99.7  | 99.71 |
| arxiv/astro-ph.GA        |   94.11 |  99.39 | 99.94 | 99.95 |
| arxiv/astro-ph.HE        |   87.16 |  98.67 | 99.42 | 99.64 |
| arxiv/astro-ph.SR        |   86.22 |  97.07 | 99.32 | 99.15 |
| arxiv/cond-mat.mes-hall  |   87.09 |  97.97 | 99.61 | 99.68 |
| arxiv/cond-mat.mtrl-sci  |   82.45 |  98.21 | 99.47 | 99.63 |
| arxiv/cond-mat.stat-mech |   78.45 |  97.78 | 98.84 | 99.27 |
| arxiv/cond-mat.str-el    |   83.77 |  98.34 | 99.35 | 99.5  |
| arxiv/cs.CV              |   78.64 |  97.8  | 99.05 | 99.36 |
| arxiv/gr-qc              |   78.62 |  97.81 | 98.88 | 99.26 |
| arxiv/hep-ph             |   73.79 |  97.31 | 98.96 | 99.26 |
| arxiv/hep-th             |   71.68 |  97.1  | 98.45 | 98.87 |
| arxiv/math.AG            |   70.91 |  97.02 | 98.85 | 99.21 |
| arxiv/math.AP            |   82.84 |  98.25 | 99.53 | 99.68 |
| arxiv/math.CO            |   80.76 |  98.02 | 98.97 | 99.31 |
| arxiv/math.NT            |   76.97 |  97.63 | 98.88 | 99.26 |
| arxiv/math.PR            |   82.87 |  98.25 | 99.39 | 99.56 |
| arxiv/nucl-th            |   78.18 |  97.77 | 99.06 | 99.33 |
| arxiv/quant-ph           |   82.25 |  98.19 | 99.18 | 99.42 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   91.35 |  99.11 | 99.57 | 99.72 |
| real   |   74.5  |  97.38 | 99.13 | 98.64 |

| topic           |   tpAUC |   pAUC |   AUC |    AP |
|:----------------|--------:|-------:|------:|------:|
| Government News |   84.23 |  98.38 | 99.07 | 99.71 |
| Middle-east     |   97.28 |  99.72 | 99.96 | 99.99 |
| News            |   97.42 |  99.74 | 99.82 | 99.82 |
| US_News         |   93    |  99.28 | 99.43 | 99.89 |
| left-news       |   93.6  |  99.35 | 99.71 | 99.8  |
| politics        |   87.92 |  98.77 | 99.29 | 99.39 |
| politicsNews    |   77.27 |  97.67 | 99.34 | 98.87 |
| worldnews       |   71.57 |  97.08 | 98.97 | 98.51 |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| ABC                      |   78.78 |  97.82 | 98.98 | 97.37 |
| NBC                      |   83.07 |  98.26 | 98.86 | 97.79 |
| The Times (UK)           |   85.81 |  98.54 | 99.37 | 98.31 |
| The Daily Telegraph (UK) |   87.76 |  98.74 | 99.51 | 98.55 |
| CNN                      |   88.39 |  98.81 | 99.68 | 98.68 |
| The Sunday Times (UK)    |   88.45 |  98.82 | 99.71 | 98.8  |
| The Guardian (UK)        |   90.94 |  99.07 | 99.69 | 98.99 |
| Fox New                  |   93.64 |  99.35 | 99.84 | 99.36 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |    4.97 |  86.72 | 95.39 | 92.19 |
| ELLIPSE(Human)+   |   84.54 |  97.72 | 99.2  | 99.37 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |   93.81 |  99.37 | 99.72 | 99.61 |
| Ivy Panda(Human)+ |   60.14 |  95.84 | 98.55 | 95.66 |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |    3.21 |  59.65 | 60.07 |  5.31 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |    5.97 |  62.12 | 63.97 | 10.99 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   13.96 |  67.26 | 68.77 | 23.72 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   35.01 |  76.52 | 78.01 | 44.88 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   39.47 |  78.32 | 76.15 | 28.12 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   46.44 |  80.39 | 84.87 | 48.43 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   50.68 |  82.38 | 80.94 | 38.76 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   52.59 |  82.78 | 87.59 | 55.37 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   66.1  |  87.72 | 90.9  | 27.96 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   67.65 |  88.26 | 92.18 | 27.46 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   74.05 |  90.54 | 94    | 65.72 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   80.69 |  92.99 | 95.94 | 72.91 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ❌       | ❌        | ✅          | ✅     | ✅               | ✅                     |
| Base      | ✅       | ✅        | ❌          | ❌     | ❌               | ❌                     |

