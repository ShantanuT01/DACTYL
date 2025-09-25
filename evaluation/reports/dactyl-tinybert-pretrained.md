# dactyl-tinybert-pretrained - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 80.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |     0   |  66.78 | 82.65 | 34.26 |
| test-1b-no-finetuning |     0   |  69.22 | 85.25 | 38.88 |
| test                  |    80.2 |  97.96 | 99.41 | 99.18 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   50.47 |  94.88 | 98.47 | 96.73 |
| abstracts            |   31.88 |  92.96 | 97.38 | 98.33 |
| news                 |   31.24 |  92.93 | 96.11 | 97.08 |
| reviews              |   35.53 |  93.16 | 97.82 | 94.61 |
| student_essays       |   15.21 |  91.15 | 94.76 | 93.37 |
| tweets               |   40.55 |  93.65 | 98.08 | 98.58 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  50.67 | 58.03 |  0.83 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |    0    |  51.73 | 59.16 |  0.77 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |    0    |  64.1  | 74.98 |  3.71 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |    0    |  65.44 | 89.88 | 15.79 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    0    |  69.22 | 85.25 | 38.88 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  71.35 | 92.13 |  8.28 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |   10.51 |  86.45 | 97.64 | 45.64 |
| gemini-1.5-pro                                                                     |   43.47 |  94.02 | 98.15 | 90.64 |
| llama-3.2-90b                                                                      |   55.64 |  95.39 | 98.68 | 92.92 |
| gemini-1.5-flash                                                                   |   74.15 |  97.33 | 99.4  | 95.96 |
| llama-3.3-70b                                                                      |   77.59 |  97.69 | 99.32 | 96.51 |
| gpt-4o-2024-11-20                                                                  |   82.25 |  98.17 | 99.53 | 97.16 |
| claude-3-5-haiku-20241022                                                          |   83.09 |  98.26 | 99.52 | 97.36 |
| claude-3-5-sonnet-20241022                                                         |   91.24 |  99.1  | 99.78 | 98.58 |
| mistral-small-latest                                                               |   92.45 |  99.22 | 99.68 | 98.8  |
| mistral-large-latest                                                               |   93.24 |  99.3  | 99.78 | 98.86 |
| DeepSeek-V3                                                                        |   93.89 |  99.37 | 99.69 | 98.94 |
| gpt-4o-mini                                                                        |   97.47 |  99.74 | 99.93 | 99.55 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   88.68 |  98.84 | 99.77 | 99.34 |
| abstracts            |   83.02 |  98.24 | 99.42 | 99.58 |
| news                 |   87.73 |  98.74 | 99.56 | 99.6  |
| reviews              |   69.33 |  96.84 | 99.07 | 97.37 |
| student_essays       |   80.74 |  98.02 | 99.49 | 99.05 |
| tweets               |   65.91 |  96.48 | 98.81 | 99.03 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |   69.62 |  96.89 | 98.52 | 99.68 |
| 538Tweets/lefttroll  |   54.85 |  95.24 | 98.3  | 98.29 |
| 538Tweets/righttroll |   72.34 |  97.16 | 99.12 | 99.05 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   52.61 |  95.06 | 98.34 | 95.67 |
|       2 |   65.46 |  96.41 | 98.85 | 96.92 |
|       3 |   84.75 |  98.44 | 99.61 | 98.8  |
|       4 |   69.09 |  96.81 | 99.2  | 97.49 |
|       5 |   74.39 |  97.37 | 99.26 | 97.82 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   87.08 |  98.67 | 99.73 | 99.79 |
| arxiv/astro-ph.CO        |   91.31 |  99.12 | 99.81 | 99.85 |
| arxiv/astro-ph.GA        |   95.35 |  99.52 | 99.95 | 99.96 |
| arxiv/astro-ph.HE        |   89.78 |  98.95 | 99.63 | 99.75 |
| arxiv/astro-ph.SR        |   87.2  |  98.47 | 99.67 | 99.73 |
| arxiv/cond-mat.mes-hall  |   89.2  |  98.89 | 99.81 | 99.84 |
| arxiv/cond-mat.mtrl-sci  |   86.8  |  98.65 | 99.55 | 99.7  |
| arxiv/cond-mat.stat-mech |   80.15 |  97.96 | 99.07 | 99.4  |
| arxiv/cond-mat.str-el    |   84.34 |  98.4  | 99.36 | 99.52 |
| arxiv/cs.CV              |   80    |  97.94 | 99.22 | 99.46 |
| arxiv/gr-qc              |   81.49 |  98.11 | 98.99 | 99.34 |
| arxiv/hep-ph             |   74.28 |  97.37 | 99.08 | 99.34 |
| arxiv/hep-th             |   71.65 |  97.09 | 98.7  | 99.07 |
| arxiv/math.AG            |   74.73 |  97.41 | 99.09 | 99.36 |
| arxiv/math.AP            |   84.32 |  98.4  | 99.59 | 99.71 |
| arxiv/math.CO            |   81.02 |  98.05 | 99.21 | 99.44 |
| arxiv/math.NT            |   79.2  |  97.86 | 99.02 | 99.35 |
| arxiv/math.PR            |   84.4  |  98.41 | 99.43 | 99.61 |
| arxiv/nucl-th            |   78.96 |  97.85 | 99.34 | 99.49 |
| arxiv/quant-ph           |   82.69 |  98.23 | 99.29 | 99.5  |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   90.96 |  99.07 | 99.67 | 99.77 |
| real   |   78.07 |  97.75 | 99.24 | 98.89 |

| topic           |   tpAUC |   pAUC |   AUC |    AP |
|:----------------|--------:|-------:|------:|------:|
| Government News |   79.26 |  97.86 | 99.09 | 99.72 |
| Middle-east     |   96.29 |  99.62 | 99.93 | 99.99 |
| News            |   98.21 |  99.82 | 99.96 | 99.94 |
| US_News         |   94.33 |  99.42 | 99.8  | 99.96 |
| left-news       |   90.52 |  99.03 | 99.75 | 99.79 |
| politics        |   85.44 |  98.51 | 99.23 | 99.24 |
| politicsNews    |   80.3  |  97.98 | 99.15 | 98.95 |
| worldnews       |   76.02 |  97.54 | 99.31 | 98.87 |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| ABC                      |   79.74 |  97.92 | 99.24 | 97.53 |
| NBC                      |   81.64 |  98.12 | 99.25 | 97.91 |
| The Times (UK)           |   87.86 |  98.75 | 99.42 | 98.52 |
| CNN                      |   88.2  |  98.79 | 99.78 | 98.84 |
| The Daily Telegraph (UK) |   88.4  |  98.81 | 99.51 | 98.59 |
| The Sunday Times (UK)    |   90.05 |  98.98 | 99.8  | 99    |
| The Guardian (UK)        |   91.31 |  99.11 | 99.58 | 99.04 |
| Fox New                  |   94.64 |  99.45 | 99.9  | 99.48 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |    7.56 |  87.95 | 95.37 | 92.84 |
| ELLIPSE(Human)+   |   88.32 |  98.8  | 99.39 | 99.66 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |   96.17 |  99.61 | 99.87 | 99.79 |
| Ivy Panda(Human)+ |   74.78 |  97.38 | 99.35 | 97.37 |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |    2.57 |  58.05 | 66.36 |  5.12 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |    7.6  |  62.91 | 71.12 | 11.07 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   15.08 |  66.72 | 72.62 | 19.45 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   33.85 |  75.96 | 81.69 | 42.92 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   39.78 |  77.3  | 84.92 | 39.77 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   47.16 |  80.55 | 87.47 | 48.8  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   58.95 |  85.2  | 90.52 | 31.77 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   60.64 |  85.8  | 91.01 | 25.31 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   62.16 |  86.32 | 90.82 | 25.6  |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   62.49 |  86.52 | 92.12 | 36.64 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   68.62 |  88.57 | 92.83 | 61.9  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   78.9  |  92.38 | 95.3  | 72.97 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ❌       | ✅        | ✅          | ✅     | ✅               | ✅                     |
| Base      | ✅       | ❌        | ❌          | ❌     | ❌               | ❌                     |

