# Fake News Classifier

## Overview
- The News Collection dataset contains about 20800 news records with their titles, authors and actuals news. This dataset is present on kaggle. You can find the link to the dataset below. 

- These records have labels as 1/0 i.e real/fake. I have trained the model using 1 independent feature i.e 'title' due to low computation power of my system. You can train a multiclass classification model based on your system's computational power.

## Motivation
- Nowadays there are many news hovering on browsers,social media, etc which people don't know are real or fake.

-  Some people trust the news just by reading it and not knowing it's source and genuinity.

-  So, in this project I have tried to create a model which predicts if a particular news is genuine or fake. 

## Problem Objective
- To build a model which can classify News records into Real/Fake.

## Methodology

### Data Preprocessing
- I have used regular expressions to filter the data i.e removing unwanted commas,full-stops, special characters etc

- Removed stop words from the corpus so that we don't train our model with unnecessary features

- I have used Stemming based on computational power.

- Used Bag Of Words i.e CountVectorizer model to transform the features.

### Model Making

#### Ensemble Model:

- I have prepared a Random Forests Classifier model.

- GridSearchCV was used to tune hyperparameter 'n_estimators' i.e number of Decision Trees.

- I have used the hyperparameter with best accuracy score to make my model.

#### Neural Network Model:

- I have also prepared a LSTM RNN model. RNNs work very well with sequential data and hence they can be used for NLP used cases. LSTM RNN is used to eliminate vanishing gradient problem in RNNs.

- I have used Sequential to add layers to the model

### Metrics

- To check how many records are correctly identified as fakes and real I have used confusion matrix

- I have used accuracy score as it doesn't seem to be an imbalanced dataset.

## DATA SOURCE
- [Fake News Dataset](https://www.kaggle.com/c/fake-news/data)

## Notebook
- [Fake News Classifier Ensemble](https://github.com/Pratik872/AI-ML/blob/main/Natural%20Language%20Processing/FakeNewsClassifier/FakeNewsRandomForestsClassifier.ipynb)

- [Fake News Classifier LSTM](https://github.com/Pratik872/AI-ML/blob/main/Natural%20Language%20Processing/FakeNewsClassifier/FakeNewsClassifierLSTM.ipynb)

# Built with 🛠️
<code><img height="30" src="https://camo.githubusercontent.com/3cdf9577401a2c7dceac655bbd37fb2f3ee273a457bf1f2169c602fb80ca56f8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png"></code>

<code><img height="50" src="https://raw.githubusercontent.com/pandas-dev/pandas/761bceb77d44aa63b71dda43ca46e8fd4b9d7422/web/pandas/static/img/pandas.svg"></code>
<code><img height="50" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png"></code>
<code><img height="60" src="https://miro.medium.com/max/625/0*iL0ELUnHdGtN8bkP.png"></code>
<code><img height="50" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/tensorflow_logo_icon_170598.png"></code>
<code><img height="50" src="https://gse-it.stanford.edu/sites/default/files/image/keras.png"></code>
