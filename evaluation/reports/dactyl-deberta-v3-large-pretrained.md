# dactyl-deberta-v3-large-pretrained - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 80.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-1b-no-finetuning |    0    |  83.34 | 93.62 | 69.6  |
| test-finetuning       |    0    |  83.37 | 94.36 | 70.05 |
| test                  |   85.12 |  98.42 | 99.62 | 99.45 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   91.81 |  99.16 | 99.74 | 99.48 |
| abstracts            |   82.82 |  98.2  | 99.51 | 99.69 |
| news                 |   76.95 |  97.64 | 98.42 | 98.88 |
| reviews              |   57.21 |  95.52 | 98.58 | 96.59 |
| student_essays       |   20.78 |  91.68 | 96    | 94.28 |
| tweets               |   48.66 |  94.42 | 98.51 | 98.85 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  51.04 | 79.23 |  1.52 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    0    |  83.34 | 93.62 | 69.6  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |    0    |  84.1  | 93.42 | 42.02 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0.01 |  83.49 | 95.37 | 32.04 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    6.1  |  85.61 | 97.58 | 46.86 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |   16.08 |  91.01 | 95.96 | 70.53 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |   41.16 |  92.78 | 98.03 | 72.45 |
| gemini-1.5-pro                                                                     |   52.86 |  94.99 | 98.46 | 91.93 |
| llama-3.2-90b                                                                      |   62.81 |  96.09 | 98.92 | 93.86 |
| gemini-1.5-flash                                                                   |   78.43 |  97.71 | 99.54 | 96.27 |
| claude-3-5-haiku-20241022                                                          |   83.48 |  98.23 | 99.69 | 97.25 |
| gpt-4o-2024-11-20                                                                  |   84.82 |  98.39 | 99.69 | 97.39 |
| llama-3.3-70b                                                                      |   86.98 |  98.61 | 99.75 | 97.77 |
| claude-3-5-sonnet-20241022                                                         |   96.43 |  99.59 | 99.95 | 99.21 |
| mistral-large-latest                                                               |   96.9  |  99.63 | 99.96 | 99.24 |
| mistral-small-latest                                                               |   97.77 |  99.72 | 99.96 | 99.37 |
| DeepSeek-V3                                                                        |   98.69 |  99.83 | 99.98 | 99.6  |
| gpt-4o-mini                                                                        |   98.72 |  99.8  | 99.98 | 99.42 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |    AUC |    AP |
|:---------------------|--------:|-------:|-------:|------:|
| RedditWritingPrompts |   99.7  |  99.97 | 100    | 99.99 |
| abstracts            |   89.73 |  98.93 |  99.73 | 99.8  |
| news                 |   99.24 |  99.92 |  99.95 | 99.96 |
| reviews              |   80.89 |  98    |  99.25 | 98.22 |
| student_essays       |   88.39 |  98.7  |  99.81 | 99.52 |
| tweets               |   64.45 |  96.23 |  98.89 | 99.05 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |   65.19 |  96.43 | 98.81 | 99.73 |
| 538Tweets/lefttroll  |   59.34 |  95.68 | 98.55 | 98.51 |
| 538Tweets/righttroll |   66.85 |  96.49 | 99.14 | 98.97 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   65.2  |  96.41 | 98.7  | 96.8  |
|       2 |   78.59 |  97.76 | 99.15 | 98.02 |
|       3 |   90.52 |  99.03 | 99.71 | 99.2  |
|       4 |   86.52 |  98.62 | 99.64 | 98.95 |
|       5 |   82.17 |  98.01 | 98.92 | 97.89 |

### Abstracts

| category                 |   tpAUC |   pAUC |    AUC |     AP |
|:-------------------------|--------:|-------:|-------:|-------:|
| arxiv/astro-ph           |   93.11 |  99.29 |  99.88 |  99.91 |
| arxiv/astro-ph.CO        |   96.76 |  99.67 |  99.96 |  99.96 |
| arxiv/astro-ph.GA        |   99.6  |  99.96 | 100    | 100    |
| arxiv/astro-ph.HE        |   95.93 |  99.58 |  99.88 |  99.92 |
| arxiv/astro-ph.SR        |   96.29 |  99.61 |  99.96 |  99.96 |
| arxiv/cond-mat.mes-hall  |   94.33 |  99.42 |  99.91 |  99.93 |
| arxiv/cond-mat.mtrl-sci  |   94.19 |  99.41 |  99.86 |  99.9  |
| arxiv/cond-mat.stat-mech |   87.42 |  98.7  |  99.76 |  99.81 |
| arxiv/cond-mat.str-el    |   90.84 |  99.06 |  99.78 |  99.82 |
| arxiv/cs.CV              |   83.25 |  98.11 |  99.68 |  99.72 |
| arxiv/gr-qc              |   89.67 |  98.94 |  99.54 |  99.69 |
| arxiv/hep-ph             |   83.41 |  98.3  |  99.47 |  99.61 |
| arxiv/hep-th             |   80.1  |  97.96 |  99.27 |  99.44 |
| arxiv/math.AG            |   85.04 |  98.47 |  99.54 |  99.68 |
| arxiv/math.AP            |   89.2  |  98.9  |  99.89 |  99.9  |
| arxiv/math.CO            |   84.15 |  98.37 |  99.56 |  99.67 |
| arxiv/math.NT            |   82.2  |  98.17 |  99.33 |  99.57 |
| arxiv/math.PR            |   89.56 |  98.94 |  99.79 |  99.84 |
| arxiv/nucl-th            |   88.11 |  98.79 |  99.7  |  99.75 |
| arxiv/quant-ph           |   90.91 |  99.07 |  99.64 |  99.75 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   99.74 |  99.97 | 99.97 | 99.99 |
| real   |   97.87 |  99.78 | 99.89 | 99.84 |

| topic           |   tpAUC |   pAUC |    AUC |     AP |
|:----------------|--------:|-------:|-------:|-------:|
| Government News |   99.72 |  99.97 | 100    | 100    |
| Middle-east     |  100    | 100    | 100    | 100    |
| News            |  100    | 100    | 100    | 100    |
| US_News         |   98.67 |  99.86 |  99.83 |  99.97 |
| left-news       |   99.95 | 100    | 100    | 100    |
| politics        |   99.96 | 100    | 100    | 100    |
| politicsNews    |   95.54 |  99.54 |  99.71 |  99.63 |
| worldnews       |  100    | 100    | 100    | 100    |

| news_outlet              |   tpAUC |   pAUC |    AUC |     AP |
|:-------------------------|--------:|-------:|-------:|-------:|
| The Daily Telegraph (UK) |   98.34 |  99.83 |  99.87 |  99.76 |
| ABC                      |   98.62 |  99.86 |  99.88 |  99.78 |
| The Times (UK)           |   98.62 |  99.86 |  99.93 |  99.81 |
| The Sunday Times (UK)    |   98.83 |  99.88 |  99.92 |  99.82 |
| The Guardian (UK)        |   99.67 |  99.97 | 100    |  99.97 |
| NBC                      |   99.94 |  99.99 | 100    |  99.99 |
| CNN                      |   99.94 |  99.99 | 100    |  99.99 |
| Fox New                  |  100    | 100    | 100    | 100    |

### Student Essays

| subset            |   tpAUC |   pAUC |    AUC |     AP |
|:------------------|--------:|-------:|-------:|-------:|
| ELLIPSE           |   20.14 |  89.63 |  96.84 |  94.41 |
| ELLIPSE(Human)+   |   93.26 |  98.91 |  99.88 |  99.89 |
| Ivy Panda (AI)    |         |        |        |        |
| Ivy Panda         |   99.98 | 100    | 100    | 100    |
| Ivy Panda(Human)+ |   93.77 |  99.36 |  99.85 |  99.34 |
| ELLIPSE (AI)      |         |        |        |        |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |    8.09 |  59.28 | 73.8  |  5.71 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |   13.98 |  65.13 | 76.36 |  9.83 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   55.61 |  84.32 | 85.67 | 70.75 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   75.14 |  91.17 | 94.28 | 47.29 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   76.33 |  91.65 | 94.4  | 82.58 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   79.72 |  92.8  | 95.46 | 54.28 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   80.57 |  93.05 | 95.97 | 76.95 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   84.64 |  94.5  | 96.86 | 80.59 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   91.06 |  96.84 | 97.93 | 89.29 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   92.36 |  97.29 | 98.12 | 92.02 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   94.18 |  97.94 | 98.68 | 88.71 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   94.43 |  98.02 | 98.47 | 93.76 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ✅       | ✅        | ❌          | ❌     | ✅               | ❌                     |
| Base      | ❌       | ❌        | ✅          | ✅     | ❌               | ✅                     |

