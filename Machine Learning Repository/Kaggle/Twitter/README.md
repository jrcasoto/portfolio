# Data Streaming and Sentiment Analysis with Twitter API (using Python, Spark Streaming NLTK) - [Source](https://inclass.kaggle.com/c/si650winter11)

### Context
This project's main objective is to use Twitter's developer account to connect via API requests and gather real-time tweets from a specific user account and create a Machine Learning model (Naive Bayes) to predict wether a tweet sentiment is positive or negative.

### Content
A dataset from University of Michigan (UMICH) was used for the Naive Bayes text classificator, which contains more than 1.5mi rows. The dataset is not available anymore in Kaggle, but you can find the .zip file within 'data' folder.

### About this file (dataset_analise_sentimento.csv)
This dataset contains over 1.5mi rows with evaluations for different tweets with an already implemented machine learning model to predict wether the message has a positive or negative sentiment. 
This dataset is structured with the following columns:
1. **ItemID**: Dataset index (auto incremental);
2. **Sentiment**: Binary classificator: **0 for negative and 1 for positive**;
3. **SentimentSource**: Source of tweet;
4. **SentimentText**: Source with evaluated text message.

### Inspiration/problem to be solved
Build a ML classification model with Natural Language Processing in order to predict **in real-time** what people are talking about a specific public person.

### Solution
For this project, I've developed both the classifier model (Naive Bayes) and used NLP techniques (specifically with nltk) to check, organize, label and construct an overview rating for Donald Trump twitter. It takes up to 500 tweets that mention him in that specific timestamp and then generates batches with its relative absolute frequencies.

You'll find the full-analysis in **Data Streaming and Sentiment Analysis with Twitter API.ipynb** notebook.

Enjoy! :smile:
