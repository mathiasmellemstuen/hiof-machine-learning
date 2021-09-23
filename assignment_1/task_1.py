# Assignment 1
# Mathias Mellemstuen
# Task 1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

from sklearn import linear_model
from sklearn.model_selection import train_test_split

# Reading data from truckdata file
data = pd.read_csv("truckdata.txt")

# Splitting the datasets two columns into two variables, x and y. 
# X: Predictor
# Y: Response
x = data.iloc[:,0]
y = data.iloc[:,1]

# Splitting the dataset into a training set and a test set. 
testSetPercentage = 0.2
trainingX, testX, trainingY, testY = train_test_split(x, y, test_size=testSetPercentage)

linearRegression = linear_model.LinearRegression()
linearRegression.fit([trainingX], [trainingY])

m = linearRegression.coef_
b = linearRegression.intercept_

#y = m * x + b

plot.scatter(trainingX, trainingY)

line = m * [trainingX] + b
#plot.scatter(x, y)
plot.show()
