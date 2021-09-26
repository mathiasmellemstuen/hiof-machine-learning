# Assignment 1
# Task 2
# KNN Algorithm | Iris Dataset
# Mathias Mellemstuen

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

# Reading the data from the iris.data file
data = pd.read_csv("iris.data", header=None)
x = data.iloc[:, 0:3]
y = data.iloc[:,4]

testSetPercentage = 0.25

trainingX, testX, trainingY, testY = train_test_split(x, y, test_size=testSetPercentage)

neighbours = KNeighborsClassifier()
neighbours.fit(trainingX, trainingY)

# Predicting how accurate the model is
predictionY = neighbours.predict(testX)

accuracy = round(100 * metrics.accuracy_score(testY, predictionY), 2) 
print(f"The accuracy of the model is: {accuracy}%")
