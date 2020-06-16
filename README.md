![](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/blob/master/Assets/banner.png)

## About the repository
This repository goal is to host my set of experiments done during the Tweet Sentiment Extraction Kaggle competition, the tasks were basically extracted from a tweet the span of words that better represent the complete tweet, this could be solved by different solutions, but what mostly worked for the community and me, was to frame it as a QA problem (question answering), where the system has a context and a question then outputs the answer, in this case, the question was the tweet sentiment, and the context was the tweet, probably this was just a fancy way of embedding the sentiment on the tweet itself through many context transformer layers.

### Published Kaggle kernels:
  - [Tweet Sentiment Extraction - EDA and baseline](https://www.kaggle.com/dimitreoliveira/tweet-sentiment-extraction-eda-and-baseline/notebook)

### What you will find
- Datasets [[link]](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/tree/master/Datasets)
- Documentation [[link]](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/tree/master/Documentation)
  - Evaluation [[link]](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/tree/master/Model%20backlog/Evaluation)
  - Inference [[link]](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/tree/master/Model%20backlog/Inference)
  - Train [[link]](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/tree/master/Model%20backlog/Train)
- Models [[link]](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/tree/master/Model%20backlog)
- Scripts [[link]](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/tree/master/Scripts)

### Tweet Sentiment Extraction
#### Extract support phrases for sentiment labels

Kaggle competition: https://www.kaggle.com/c/tweet-sentiment-extraction

### Overview

"My ridiculous dog is amazing." [sentiment: positive]

With all of the tweets circulating every second it is hard to tell whether the sentiment behind a specific tweet will impact a company, or a person's, brand for being viral (positive), or devastate profit because it strikes a negative tone. Capturing sentiment in language is important in these times where decisions and reactions are created and updated in seconds. But, which words actually lead to the sentiment description? In this competition you will need to pick out the part of the tweet (word or phrase) that reflects the sentiment.

Help build your skills in this important area with this broad dataset of tweets. Work on your technique to grab a top spot in this competition. What words in tweets support a positive, negative, or neutral sentiment? How can you help make that determination using machine learning tools?

In this competition we've extracted support phrases from [Figure Eight's Data for Everyone platform](https://www.figure-eight.com/data-for-everyone/). The dataset is titled Sentiment Analysis: Emotion in Text tweets with existing sentiment labels, used here under creative commons attribution 4.0. international licence. Your objective in this competition is to construct a model that can do the same - look at the labeled sentiment for a given tweet and figure out what word or phrase best supports it.

Disclaimer: The dataset for this competition contains text that may be considered profane, vulgar, or offensive.
