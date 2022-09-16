# SMS Spam-Ham Detection

To test the deployed model click [here](https://sms-classifier-deploy.herokuapp.com/).<br/>
Note : It takes some time to load the heroku page. Patience is the key!!

## Overview
- The SMS Spam Collection is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged acording being ham (legitimate) or spam. 

- The SMS Spam Collection has a total of 4,827 SMS legitimate messages (86.6%) and a total of 747 (13.4%) spam messages.

## Motivation
- Nowadays there are many messages which people get on their phones. Problem arises when the messages are spam and people are not able to realise it just by reading the message.

-  These spam messages ask people to do the things which can have very ugly repercussions on them(credit card frauds,lottery frauds).

-  So, in this project I have tried to create a model which predicts if a message is spam or a ham. 

## Project Structure
- [main.py](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/main.py) : This file has the flask application which is created.

- [utils.py](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/utils.py) : This file has all the helper functions which are required to run the application.

- [constants.py](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/constants.py) : This file has all the constant variables required in developing the application.

- [templates](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/templates) : This folder has all the templates which are rendered in the application

- [readme_resources](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/readme_resources) : This folder has all the images used to create readme file.

- [requirements.txt](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier//requirements.txt) : This file has all the packages used to code and build the application.

- [SMSClassifier.ipynb](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/SMSClassifier.ipynb) : This jupyter notebook has the code for making models.

## Problem Objective
- To build a model which can classify SMS messages into Spam - Ham

## Methodology

### EDA (Exploratory Data Analysis)
- Checked for NaN values.

- Required Graphs are plotted using seaborn,matplotlib libraries.

- Checked for data imbalance.

### Data Preprocessing
- I have used regular expressions to filter the data i.e removing unwanted commas,full-stops, special characters etc.

- Removed stop words from the corpus so that we don't train our model with unnecessary features.

- I have used Lemmatization for processing the words.

- Used TfIdf Vectorizer model to transform the features.

### Feature Engineering
- Transformed the target variable into binary.

- The data was imbalanced. So balanced the dataset using Over-Sampling method. I have used 'imblearn' library for this.

![HAMvsSPAMOrg](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/readme_resources/imb_dataset.png)
![HAMvsSPAMBal](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/readme_resources/bal_dataset.png)

### Model Making

- I have prepared Naive Bayes Classifier and RandomForests Classifier models.

- I have chosen RandomForests Classifier as my final model as I got better results.

- I have tuned the hyperparameters i.e 'alpha' for NB Classifier and 'n_estimators' for RF Classifier by using GridSearchCV

- Further I have used StratifiedKFold as my cv to balance training and validation data.

### Metrics

- To check how many messages are correctly identified as spams and hams I have used confusion matrices for both models.

![CF_NB](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/readme_resources/NB_CF.png)
![CF_RF](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/readme_resources/RF_CF.png)

Correction : The image on right side is for RandomForestsClassifier instead of Naive Bayes.

- I have given importance to 'precision' score as we need to correct identify the spam message.eg : What if model detects a ham message as spam!!!The person would miss important message!!

### DATA SOURCE
- [SMS Spam-Ham Dataset](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/SMSSpamCollection)

### Notebook
- [SMS Spam-Ham Classifier](https://github.com/Pratik872/NLP/blob/main/E2EProject/SMSClassifier/SMSClassifier.ipynb)

### Built with 🛠️
- Packages : Pandas,Numpy,Seaborn,Matplotlib,NLTK,Sklearn,re(Regular Expressions),Imblearn,Flask,pickle

- Dataset : Kaggle

### Deployment
- Deployed using Heroku(PAAS)

- For deployment branch click [here](https://github.com/Pratik872/NLP/tree/deploy)

- For Web Application click [here](https://sms-classifier-deploy.herokuapp.com/)
