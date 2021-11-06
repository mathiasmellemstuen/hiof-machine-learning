# HIOF Machine learning course

## Contents of repository
- All assignments given in the machine learning course. 
- Exam project

## Assignment 1

Group Allowed: This exercise can be done alone or a group of at most 2 students.

 

Materials to Submit:

Coding: Complete coding in a state that it can be run to produce the result. If you work in a group, the same coding should be uploaded individually for each member of the group.

Report: A report of max. 3 pages (A4, 11 font, 1.5 line width, Times New Roman) describing every function, library and procedure. Don’t mention any program segment, flow-chart or pseudocode. If you work in a group, each member of the group must upload individual report written by his/her own. Group members are not allowed to upload the same report for the group.

 

Programing Language: Python. You are allowed to use library of your own choice.

### Part 1 - Foodtruck

In this part of this exercise, you will implement simple linear regression to predict profits for a food truck*. Suppose you are the CEO of a restaurant franchise and are considering different cities for opening a new outlet. The chain already has trucks in various cities and you have data for profits and populations from the cities. You'd like to figure out what the expected profit of a new food truck might be given only the population of the city that it would be placed in. You would like to use this data to help you select which city to expand. You need to start examining the data  Download data(uploaded with this assignment) by implementing the following operations:

Import all the required libraries (for example, pandas, numpy, matplotlib, etc)

You can use pandas to load the data into a data frame (or any other tool of yor choice to load the dataset from the file).

By visualizing the dataset, you can manually find any relationship between the data. This can be done by plotting the data points in a scatter plot.

The first column in the dataset is “X”(independent variable) and the next column is “Y” (dependent variable)

Split 80% of the data to the training set while 20% of the data to test set.

Now  implement simple linear regression using any library function of your choice.

Finally plot the linear model along with the data to visually see how well it fits.


### Part 2 - KNN Algorithm

Your task is to implement KNN algorithm using Iris dataset: Target attribute class:{Iris Setosa, Iris Versicolour, Iris Virginica}. ( https://archive.ics.uci.edu/ml/datasets/Iris (Links to an external site.) )

To implement KNN you have to

Split data into a train and a test split (75% and 25% respectively).

Implement a function that returns top K Nearest Neighbors for a given query (data point).

Measure the quality of your prediction.

*The problem has been taken from Andrew NG’s lecture.

## Assignment 2

In this assignment, you will implement an Artificial Neural Network with the help of Sklearn library provided class “MLPClassifier” to classify numeric digits (0-9)

Import all the required libraries (for example, pandas, numpy, matplotlib, etc)

Use datasets.load_digits() function from Sklearn library

See : https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

Split 70% of the data to the training set while 30% of the data to test set

Use the methods/functions in MLPClassifier class to classify MNIST numeral dataset

Try with different number of hidden layers and number of nodes in each of those hidden layers

Flip the train and test set and observe the difference in performance


Write a short report based on your observations with respect to number of nodes and number of hidden layers and your obtained accuracy on test set

Group Allowed: This exercise can be done alone or a group of at most 2 students.

## Assignment 3

### Materials to Submit
- Coding: Complete coding in a state that it can be run to produce the result. If you work in a group, the same coding should be uploaded individually for each member of the group.
- Report: The report (at most 3 A4 size page in 10 size font)must contain yourresponseto the points (i–v)as mentioned above. The responses must be based on your implementation and achievedresults.


### More
- Submission: Put everything in a zip folder named using the following convention: FirstName_LastName.zip and upload in canvas.
- Programing Language: Python. You are allowed to use any library of your own choice.
- Group Allowed: This exercise can be done alone or a group of at most 2 students.
- Deadline: November 19, 2021 at 23:59.

### The overall assignment
Use the ALS dataset(look at the data.zip). This casestudy examines the patterns, symmetries, associations  and  causality in a rare but devastating disease, amyotrophic lateral sclerosis (ALS). A major clinically relevant question in this  biomedical study is: What patient phenotypes can be automatically and reliably identified and used to predict the change of the ALSFRS slope over time?

### Part 1
Load and prepare the data.
### Part 2
Perform summary and preliminary visualization.
### Part 3
Normalize the data, and analyzethe result of normalization.
### Part 4
This part if for k-means clustering
1. Train a k-meansmodel on the data, select kusing any of themethodsdescribed during the lectures.
2. Determine the clustering, anddescribe the clusters in terms of all variables used in the clustering.
### Part 5 
Repeat the exercise with more andfewer clusters, and analyzeif the new solutions are better than the original solution!

