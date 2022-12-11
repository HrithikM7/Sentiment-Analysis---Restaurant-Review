# Sentiment-Analysis---Restaurant-Review

<img src="Picture.jpg" width = "200" height = "200" >

## Quick Intro
Enclosed is a Jupyter Notebook which uses Natural Language Processing to perform Sentiment Analysis on a given restaurant review.

## Data Collection
The data which was used for training & testing purposes were obtained through : 
* Web Scraping : Around 10 websites were web scraped to obtain approximately 30,000 reviews given for various restaraunts throughout the world. 
* Dataset :
            * Downloaded a dataset from Kaggle.
The final dataset after combining reviews from the various sources consists of 81,000 reviews, and is present in the zip file provided.

## Problem Statement
Sentiment Analysis has to be done to predict whether a restaurant review given by a customer is Positive (or) Negative.

## Approach
* Step 1 : Web scraping was done using the Python library BeautifulSoup. 
* Step 2 : Basic EDA(i.e Exploratory Data Analysis) was done to check if the dataset is balanced AND whether it has any missing values or duplicate entries.
* Step 3 : The reviews obtained from Web scraping had HTML tags present within them. By using BeautifulSoup & Regex expressions, both HTML tags & Punctuation marks were removed from the reviews.
* Step 4 : Reviews which were not in English were removed with the help of the library LangDetect.
* Step 5 : Preprocessing : Removal of StopWords, Lemmatization, and Count Vectorization were performed in the mentioned order.
* Step 6 : Dataset was divided into 2 parts : Training(i.e 80%) & Testing(i.e 20%) with Sratify enabled to make sure that the datasets were divided properly.
* Step 7 : Several machine learning algorithms were implemented such as MultiNomialNB, Decision Tree, Random Forest, Gradient Boosting, and AdaBoosting to model and fit the data. GridSearchCV was used to perform hyperparameter tuning to get the best parameters for each algorithm used. To quantify the models, I used the metrics of accuracy_score (i.e dataset was balanced).


## Result
In this project, I implemented MultiNomialNB, Decision Tree, Random Forest, Gradient Boosting, and AdaBoosting for a Sentiment Analysis task based on Natural Language Processing. The best result that was obtained was by: MultiNomialNB w/ Accuracy Score : 0.86766

## Output Screenshots 

1. Positive Review
     <img src="Ex2 - Question.png">
     <img src="Ex2 - Prediction.png">

2. Negative Review
     <img src="Ex1 - Question.png">
     <img src="Ex1 - Prediction.png">

## Importance
The field of machine learning has seen a tremendous growth over the past few years, and is only going to grow further in the future. 
Performing sentiment analysis on restaurant reviews will benefit both the restaurant owners as well as the customers. Restaurant owners will be able to identify which aspects of the restaurant are good and which have to be worked upon. 

## Authors

Hrithik Maddirala  
[@hrithik_m245](https://www.linkedin.com/in/hrithik-maddirala/)


<img src="DSC_0037-01-01.jpeg" width="100">
