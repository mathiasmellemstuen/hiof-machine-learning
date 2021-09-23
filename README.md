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
