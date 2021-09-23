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

#Is the task to implementing KNN manually? 
