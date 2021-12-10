import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
import sys

trainingData = pd.read_csv("ALS_TrainingData_2223.csv")

# Removing unwanted data from the file
trainingData = trainingData.drop("ID", axis=1)

testingData = pd.read_csv("ALS_TestingData_78.csv")
testingData = testingData.drop("ID", axis=1)

print(trainingData.shape)
def calculateKMeans(data, numberOfClusters, scatterResult):
    # Removing the mean and scaling to unit variance
    scaler = StandardScaler() 
    dataScaled = scaler.fit_transform(data)


    # Normalizing the data
    dataNormalized = normalize(dataScaled)

    # Reducing the dimention of the data
    pca = PCA(n_components = 2) 
    dataPricipal = pca.fit_transform(dataNormalized)
    dataPricipal = pd.DataFrame(dataPricipal)
    dataPricipal.columns = ["N1", "N2"]

    kmeans = KMeans(n_clusters = numberOfClusters)
    prediction = kmeans.fit_predict(dataPricipal)

    if scatterResult:
        plot.figure(figsize = (8, 8))
        plot.title(f'A scatter plot of the data clustered using the KMeans algorithm with {numberOfClusters} clusters')
        plot.scatter(dataPricipal["N1"], dataPricipal["N2"], c = prediction, cmap ='rainbow')

    return kmeans.score(dataPricipal)

def plotIterationOfScores(minClusters, maxClusters):
    print(f'Starting test where we are iterating from {minClusters} to {maxClusters} as the number of clusters in the kmeans algorithm. Then plotting it\'s score')
    global trainingData
    scores = []

    for i in range(minClusters, maxClusters): 
        scores.append(calculateKMeans(trainingData, i, False))
        progressPercentage = (i / (maxClusters - minClusters)) * 100 - minClusters

        sys.stdout.write(f'\rIteration progress: {int(progressPercentage)}%')
        sys.stdout.flush()

    plot.title(f'A plot of a iteration of the numbers of clusters between {minClusters} and {maxClusters}')
    plot.plot(scores)

plotIterationOfScores(1, 100)

# 20 så bra ut

calculateKMeans(trainingData, 10, True)

plot.show()
# plot.figure(figsize = (6, 6))
# plot.scatter(dataPricipal["N1"], dataPricipal["N2"])
# plot.show()
# plot.figure(figsize=(8, 8))
# plot.title("Visualization of the data")
# dendrogram = shc.dendrogram(shc.linkage(dataPricipal, method="ward"))
# plot.show()