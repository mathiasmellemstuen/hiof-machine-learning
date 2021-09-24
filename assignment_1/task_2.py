# Assignment 1
# Task 2
# KNN Algorithm | Iris Dataset
# Mathias Mellemstuen

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Reading the data from the iris.data file
data = pd.read_csv("iris.data", header=None)
x = data.iloc[:, 0:3]
y = data.iloc[:,4]

testSetPercentage = 0.25

trainingX, testX, trainingY, testY = train_test_split(x, y, test_size=testSetPercentage)

trainingX = trainingX.reshape(-1, 1)
trainingY = trainingY.reshape(-1, 1)

neighbours = KNeighborsClassifier()
