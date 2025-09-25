# dactyl-bert-tiny-finetuned - DACTYL Results

Unless otherwise specified, TPAUC is 5.0% FPR and 80.0% TPR.

## Overall

| dataset               |   tpAUC |   pAUC |   AUC |    AP |
|:----------------------|--------:|-------:|------:|------:|
| test-finetuning       |    0    |  70.22 | 86.71 | 39.95 |
| test-1b-no-finetuning |    0    |  71.35 | 87.69 | 43.5  |
| test                  |   70.52 |  96.97 | 99.11 | 98.77 |
### Domain Performance

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   52.14 |  95.05 | 98.79 | 97.19 |
| abstracts            |   64.92 |  96.33 | 98.83 | 99.25 |
| news                 |   36.98 |  93.53 | 96.65 | 97.45 |
| reviews              |    5.48 |  89.29 | 95.78 | 90.4  |
| student_essays       |    6.13 |  89.73 | 94.78 | 92.87 |
| tweets               |    5.7  |  88.9  | 96.79 | 97.48 |

### Model Performance

| model                                                                              |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       |    0    |  51.89 | 62.16 |  1.02 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              |    0    |  52.63 | 86.15 |  1.67 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 |    0    |  57.91 | 77.64 |  2.24 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing |    0    |  61.98 | 80.6  |  2.43 |
| meta-llama/Llama-3.2-1B-Instruct                                                   |    0    |  71.35 | 87.69 | 43.5  |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               |    0    |  72.8  | 94.91 | 20    |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            |    5.24 |  85.77 | 95.58 | 47.29 |
| gemini-1.5-pro                                                                     |   19.06 |  90.97 | 96.97 | 85.66 |
| llama-3.2-90b                                                                      |   36.66 |  93.32 | 97.82 | 89.56 |
| gemini-1.5-flash                                                                   |   57.29 |  95.57 | 98.99 | 93.37 |
| gpt-4o-2024-11-20                                                                  |   69.57 |  96.85 | 99.01 | 95.01 |
| llama-3.3-70b                                                                      |   69.94 |  96.89 | 99.23 | 95.25 |
| claude-3-5-haiku-20241022                                                          |   78.06 |  97.74 | 99.38 | 96.48 |
| mistral-large-latest                                                               |   87.15 |  98.68 | 99.69 | 97.94 |
| claude-3-5-sonnet-20241022                                                         |   88.33 |  98.8  | 99.72 | 98.11 |
| mistral-small-latest                                                               |   91.53 |  99.13 | 99.75 | 98.68 |
| DeepSeek-V3                                                                        |   91.65 |  99.14 | 99.74 | 98.62 |
| gpt-4o-mini                                                                        |   95.36 |  99.52 | 99.91 | 99.26 |

## Nonadversarial Results

### Domain

| domain               |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| RedditWritingPrompts |   87.55 |  98.72 | 99.79 | 99.34 |
| abstracts            |   78.89 |  97.83 | 99.33 | 99.52 |
| news                 |   84.49 |  98.41 | 99.33 | 99.4  |
| reviews              |   56.95 |  95.52 | 98.4  | 96.04 |
| student_essays       |   67.82 |  96.67 | 99.34 | 98.59 |
| tweets               |   43.35 |  94.05 | 98.06 | 98.39 |

### Tweets

| category             |   tpAUC |   pAUC |   AUC |    AP |
|:---------------------|--------:|-------:|------:|------:|
| 538Tweets/fearmonger |   46.78 |  94.47 | 98.12 | 99.58 |
| 538Tweets/lefttroll  |   28.95 |  92.41 | 97.36 | 97.25 |
| 538Tweets/righttroll |   50.64 |  94.86 | 98.2  | 98.12 |

### Reviews

|   stars |   tpAUC |   pAUC |   AUC |    AP |
|--------:|--------:|-------:|------:|------:|
|       1 |   35.29 |  93.1  | 97.13 | 93.57 |
|       2 |   48.47 |  94.69 | 97.93 | 95.02 |
|       3 |   72.27 |  97.02 | 99.37 | 97.84 |
|       4 |   64.12 |  96.3  | 98.88 | 96.84 |
|       5 |   65.6  |  96.47 | 98.47 | 96.75 |

### Abstracts

| category                 |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| arxiv/astro-ph           |   79.13 |  97.86 | 99.5  | 99.63 |
| arxiv/astro-ph.CO        |   89.75 |  98.95 | 99.77 | 99.81 |
| arxiv/astro-ph.GA        |   96.58 |  99.65 | 99.96 | 99.96 |
| arxiv/astro-ph.HE        |   89.38 |  98.9  | 99.64 | 99.75 |
| arxiv/astro-ph.SR        |   86.82 |  98.6  | 99.74 | 99.79 |
| arxiv/cond-mat.mes-hall  |   79.45 |  97.89 | 99.65 | 99.72 |
| arxiv/cond-mat.mtrl-sci  |   80.75 |  98.03 | 99.52 | 99.65 |
| arxiv/cond-mat.stat-mech |   73.75 |  97.29 | 99.11 | 99.39 |
| arxiv/cond-mat.str-el    |   84.04 |  98.37 | 99.41 | 99.55 |
| arxiv/cs.CV              |   70.35 |  96.91 | 99.13 | 99.34 |
| arxiv/gr-qc              |   76.8  |  97.63 | 99.16 | 99.41 |
| arxiv/hep-ph             |   69.43 |  96.87 | 98.99 | 99.28 |
| arxiv/hep-th             |   72.49 |  97.18 | 98.7  | 99.07 |
| arxiv/math.AG            |   71.78 |  97.11 | 98.9  | 99.26 |
| arxiv/math.AP            |   78.41 |  97.8  | 99.52 | 99.63 |
| arxiv/math.CO            |   77.16 |  97.65 | 98.86 | 99.29 |
| arxiv/math.NT            |   69.62 |  96.88 | 98.49 | 99.06 |
| arxiv/math.PR            |   81.16 |  98.08 | 99.47 | 99.61 |
| arxiv/nucl-th            |   74.34 |  97.37 | 99.14 | 99.32 |
| arxiv/quant-ph           |   79.09 |  97.86 | 99.26 | 99.47 |

### News

| real   |   tpAUC |   pAUC |   AUC |    AP |
|:-------|--------:|-------:|------:|------:|
| fake   |   89.07 |  98.88 | 99.46 | 99.64 |
| real   |   72.62 |  97.19 | 98.95 | 98.48 |

| topic           |   tpAUC |   pAUC |   AUC |    AP |
|:----------------|--------:|-------:|------:|------:|
| Government News |   86.22 |  98.58 | 98.86 | 99.66 |
| Middle-east     |   96.04 |  99.59 | 99.84 | 99.98 |
| News            |   91.16 |  99.1  | 99.64 | 99.55 |
| US_News         |   85.33 |  98.5  | 99.46 | 99.89 |
| left-news       |   92.91 |  99.27 | 99.77 | 99.82 |
| politics        |   84.05 |  98.37 | 99.17 | 99.12 |
| politicsNews    |   69.85 |  96.91 | 98.9  | 98.37 |
| worldnews       |   75.8  |  97.52 | 99.01 | 98.6  |

| news_outlet              |   tpAUC |   pAUC |   AUC |    AP |
|:-------------------------|--------:|-------:|------:|------:|
| ABC                      |   76.49 |  97.59 | 99.12 | 97.31 |
| NBC                      |   79.91 |  97.94 | 99.05 | 97.47 |
| CNN                      |   80.92 |  98.04 | 99.27 | 97.79 |
| The Times (UK)           |   85.32 |  98.49 | 99.05 | 97.97 |
| The Sunday Times (UK)    |   86.62 |  98.63 | 99.53 | 98.43 |
| The Daily Telegraph (UK) |   87.59 |  98.73 | 99.46 | 98.48 |
| The Guardian (UK)        |   87.67 |  98.73 | 99.36 | 98.5  |
| Fox New                  |   91.41 |  99.12 | 99.8  | 99.14 |

### Student Essays

| subset            |   tpAUC |   pAUC |   AUC |    AP |
|:------------------|--------:|-------:|------:|------:|
| ELLIPSE           |    0    |  84.44 | 93.81 | 90.4  |
| ELLIPSE(Human)+   |   66.2  |  96.53 | 98.75 | 99.23 |
| Ivy Panda (AI)    |         |        |       |       |
| Ivy Panda         |   94.54 |  99.44 | 99.9  | 99.77 |
| Ivy Panda(Human)+ |   73.14 |  97.22 | 99.34 | 97.1  |
| ELLIPSE (AI)      |         |        |       |       |

## Adversarial Results

TPAUC is 30.0% FPR and 40.0% TPR.

| model                                                                              | domain               |   tpAUC |   pAUC |   AUC |    AP |
|:-----------------------------------------------------------------------------------|:---------------------|--------:|-------:|------:|------:|
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-student_essays-testing       | student_essays       |    2.95 |  57.22 | 68.11 |  4.99 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | student_essays       |    7.56 |  60.96 | 71.35 |  7.14 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-reviews-testing              | reviews              |   27.78 |  70.57 | 80.86 |  4.68 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | reviews              |   28.37 |  72.13 | 81.9  |  6.76 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-news-testing                 | news                 |   30.32 |  74.25 | 79.78 | 32.79 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | news                 |   42.56 |  79.47 | 84.02 | 51.6  |
| meta-llama/Llama-3.2-1B-Instruct                                                   | tweets               |   49.45 |  79.77 | 88.38 | 32.14 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-tweets-testing               | tweets               |   58.07 |  84.09 | 91.12 | 46.72 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-RedditWritingPrompts-testing | RedditWritingPrompts |   68.74 |  88.6  | 92.8  | 31.86 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | RedditWritingPrompts |   69.77 |  89.16 | 93.72 | 42.94 |
| USERNAME/fine-tuned-Llama-3.2-1B-Instruct-apollo-mini-abstracts-testing            | abstracts            |   82.77 |  93.78 | 95.94 | 81.41 |
| meta-llama/Llama-3.2-1B-Instruct                                                   | abstracts            |   83.64 |  94.14 | 96.14 | 83.98 |

| Type      | tweets   | reviews   | abstracts   | news   | student_essays   | RedditWritingPrompts   |
|:----------|:---------|:----------|:------------|:-------|:-----------------|:-----------------------|
| Finetuned | ❌       | ✅        | ✅          | ✅     | ✅               | ✅                     |
| Base      | ✅       | ❌        | ❌          | ❌     | ❌               | ❌                     |

