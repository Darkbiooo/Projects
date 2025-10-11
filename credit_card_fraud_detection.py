import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# loading Dataset to Pandas dataframe
credit_card_data = pd.read_csv('./creditcard.csv')
# first 5 rows of the dataset
print(credit_card_data.head())
# information of the dataset
print(credit_card_data.info())
# checking the number of the missing values in each column
print(credit_card_data.isnull().sum())
# checking the distribution of legit and fraud transactions in the dataset
print(credit_card_data['Class'].value_counts())
# separating the data for the analysis
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]
print(legit.shape)
print(fraud.shape)
# statistical measures of the data
print(legit.Amount.describe())
print(fraud.Amount.describe())
# compare the values for both of the transactions
print(credit_card_data.groupby('Class').mean())
# under-sampling
# build a sample dataset containing similar distribution of normal transactions and Fraudulent transactions
legit_sample = legit.sample(n=492)
# concatenate two dataframes
new_dataset = pd.concat([legit_sample, fraud],axis=0)
print(new_dataset['Class'].value_counts())
print(new_dataset.groupby('Class').mean())
# splitting the data into features and targets
X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']
print(X)
print(Y)
# splitting the data into training data and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)
# model training
model = LogisticRegression()
# training the Logistic Regression model with Training data
model.fit(X_train, Y_train)
# model evaluation
# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy on Training data : ', training_data_accuracy)
# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data : ', test_data_accuracy)

