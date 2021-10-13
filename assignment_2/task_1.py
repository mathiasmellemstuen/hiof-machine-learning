# Assignment 2
# Task 1
# Artificial Neural Network 
# Mathias Mellemstuen

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def createAndRunMLPClassifier(testSize, hiddenLayerSize, maxIterations): 
    """
    This function do the following: 
    1. Loading the digits data
    2. Splitting the data into train and test data
    3. Creating the MLPClassifier object
    4. Using the trainingdata with the fit function
    5. Prediction with the test data
    6. Printing a score of accuracy of the prediction
    """

    # Loading data
    X, y = load_digits(return_X_y=True)

    # Splitting the data into a train set and test set
    trainX, testX, trainY, testY = train_test_split(X, y, test_size=testSize)
    
    # Instantiating the MLPClassifier object
    clf = MLPClassifier(random_state=1, max_iter=maxIterations, hidden_layer_sizes=hiddenLayerSize)
    
    # Using the training data
    clf.fit(trainX, trainY)

    # Predicting the values of the test data
    clf.predict_proba(testX)
    
    # Predicting how accurate the model is and printing it
    modelScore = clf.score(testX, testY)
    print(f"The mean accuracy of the test data and labels is {round(modelScore, 4) * 100}%")


if __name__ == "__main__":
    # Running the code with some different parameters for observation the difference
    createAndRunMLPClassifier(testSize = 0.3, hiddenLayerSize = (100,50), maxIterations = 40000)
    createAndRunMLPClassifier(testSize = 0.7, hiddenLayerSize = (100,50), maxIterations = 40000)
    createAndRunMLPClassifier(testSize = 0.3, hiddenLayerSize = (1,), maxIterations = 40000)
    createAndRunMLPClassifier(testSize = 0.3, hiddenLayerSize = (100, 200, 50, 50), maxIterations = 40000)