# Assignment 1
# Task 1
# Linear Regression | Food Truck
# Mathias Mellemstuen

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# Reading data from truckdata file
data = pd.read_csv("truckdata.txt", header=None)

# Splitting the datasets two columns into two variables, x and y. 
x = data.iloc[:,0]
y = data.iloc[:,1]

x = x.to_numpy()
y = y.to_numpy()

# Splitting the dataset into a training set and a test set. 
testSetPercentage = 0.2
trainingX, testX, trainingY, testY = train_test_split(x, y, test_size=testSetPercentage)
trainingX = trainingX.reshape(-1, 1)
trainingY = trainingY.reshape(-1, 1)

# Running linear regression on the dataset
linearRegression = linear_model.LinearRegression()
linearRegression.fit(trainingX, trainingY)

m = linearRegression.coef_
b = linearRegression.intercept_

y = m * trainingX + b

# Plotting the line
plot.plot([min(trainingX), max(trainingX)], [min(y), max(y)], linewidth=2, color='orange')

# Showing training data (in blue) and test data (in green)
plot.scatter(trainingX, trainingY, color = 'blue')
plot.scatter(testX, testY, color = 'red')

# Displaying legend text
plot.legend(["Regression function", "Training data", "Test data"])

# Showing the matplotlib window
plot.title("Linear regression: Truck data")
plot.show()