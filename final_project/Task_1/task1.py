# Task 1: Two-layer perceptron

# References used in task 1:
# - https://en.wikipedia.org/wiki/Sigmoid_function
# - Artificial Neural Network-Week6-Part1.pdf - lecture slides taken from canvas
# - Artificial Neural Network-Week6-Part2.pdf - lecture slides taken from canvas
# - StudyMaterial_BackPropagation-Neural-Networks-Highlighted-New.pdf - document taken from canvas
# - https://www.youtube.com/watch?v=UJwK6jAStmg - YouTube video on forward propagation
# - https://www.youtube.com/watch?v=5u0jaA3qAGk - YouTube video on gradient decent
# - https://www.youtube.com/watch?v=GlcnxUlrtek - YouTube video on back propagation
# - https://stackoverflow.com/questions/5283649/plot-smooth-line-with-pyplot - On how to draw smooth curved lines in pyplot

import numpy
import copy
import matplotlib.pyplot as plot
from scipy.interpolate import make_interp_spline # Using make_interp_spline for plotting curved lines in pyplot

def sigmoidFunction(value):
    """
    Sigmoid function

    Arguments
    ---------
    value: This is the x variable in the sigmoid function
    """
    return 1 / (1 + numpy.exp(-value))

def forwardPropagation(input, weights):
    """ 
    Calculates the forward propagation in the network

    Arguments
    ---------
    input: Array of input values in the network
    weights: Array of weights between every node in the network
    """

    weight0DotInput = numpy.dot(weights[0].T, input)
    weight1DotWeight0 = numpy.dot(weights[1].T, numpy.insert(weight0DotInput, 0, 1, axis = 0))

    return [sigmoidFunction(weight0DotInput), sigmoidFunction(weight1DotWeight0)]

def backPropagation(input, out, target, weights, learningRate, deltaWeights):
    """
    Calculates the back propagation in the network

    Arguments
    ---------
    input: Array of input values in the network.
    out: The output value from the forward propagation algorithm.
    target: The target value that we want to reach
    weights: Array of weights between every node in the network
    learningRate: Controls how much we adjust the weights
    deltaWeights: Current change in the weights from the previous passes of the algorithm
    """

    out0Compliment = 1 - out[0] 
    out1Compliment = 1 - out[1]

    targetDifference = target - out[1] # Difference between the target value and the current output

    # Calculating the change in weights for the second matrix
    delta1 = out[1] * out1Compliment * targetDifference 
    deltaWeights[1] = learningRate * delta1.T * numpy.insert(out[0], 0, 1, axis = 0)
    
    # Calculating the change change in weights for the first matrix
    delta0 = out[0] * out0Compliment * weights[1][1:, :] * delta1
    deltaWeights[0] = learningRate * delta0.T * input

    # Adding the change to the weight matrices
    weights[0] = weights[0] + deltaWeights[0]
    weights[1] = weights[1] + deltaWeights[1]

def integerToBits(integer):
    """
    Converts an integer to an array that is representing the integer in bits. 
    This means an integer with value 1 -> 00001 
                                     2 -> 00010
                                     3 -> 00011
    etc...

    Arguments
    ---------
    integer: The number that will be converted to an array of bits
    """

    # Converting the integer to it's representation of an array of bits
    arr = [int(i) for i in bin(integer)[2:]]

    # The array needs to be bitLength in length. Adding 0 to the beginning of the array if the length is not at the desired length. 
    bitLength = 5
    if len(arr) < bitLength:
        for i in range(0, bitLength - len(arr)):
            arr.insert(0, 0)

    return arr

def createDataset():
    """
    Creating a dataset that contains two arrays.
    The first array contains number 0 -> 16 represented in arrays of bits. 
    The second array contains information about wheter the number is odd or even in the previous array

    Returns a tuples with both of these arrays
    """

    # Creating an array of numbers between 0 - 16 represented in arrays of bits
    number = numpy.array([integerToBits(i) for i in range(0, 16)])

    # Creating a list that represents if the number if odd or even
    oddEven = numpy.array([(1 if i % 2 == 1 else 0) for i in range(0,16)])

    return number.T, oddEven

def createRandomWeights():
    """
    Creating random weight matrix. The weights are a random number between -1.0 and 1.0. 
    """
    arr = []
    arr.append(numpy.random.uniform(-1.0, 1.0, (5, 4)))
    arr.append(numpy.random.uniform(-1.0, 1.0, (5, 1)))
    return arr

def createDeltaWeights(): 
    arr = []
    arr.append(numpy.zeros((5, 4)))
    arr.append(numpy.zeros((5, 1)))
    return arr

def perceptron(input, output, weights, learningRate):
    """
    Running the neural network until the error is in an acceptible range.

    Arguments
    ---------
    input: Array of input values in the network
    output: If the elemens in the input array is odd or even
    weights: Array of weights between every node in the network
    learningRate: Controls how much we adjust the weights

    Returning the number of epochs
    """

    deltaWeights = createDeltaWeights() # Contains the change in the weights. Every value here is initially zero
    epochs = 0 # Contains number of passes of the training

    # Initially assuming that there is an error
    error = True

    # Running the algorithm as long as there exists an error
    while error:
        for i in range(0, 16):

            # Getting the current number from the input array
            currentInput = input[:,i].reshape(5, 1)

            # Running the forward propagation for each number in the input array
            forwardPropagationOutput = forwardPropagation(currentInput, weights)

            # Running back propagation with the output from the forward propagation
            backPropagation(currentInput, forwardPropagationOutput, output[i], weights, learningRate, deltaWeights)

            # Checking if there is an error after running forward and back propagation
            error = True if numpy.abs(output[i] - forwardPropagationOutput[1]) >= 0.05 else False

            # Incrementing epochs at the end of the algorithm
            epochs = epochs + 1

    return epochs

if __name__ == "__main__":

    # Creating random weights with values between -1 and 1
    weights = createRandomWeights()

    # Creating a dataset where the input is all numbers between 0 - 16 in binary. Output is containing information about if these numbers is odd or even
    input, output = createDataset()

    value = 0.05
    targetValue = 0.5
    increment = 0.05

    # For later storing the learning rate and epochs for plotting them in a graph
    xValues = []
    yValues = []

    while value <= targetValue:

        # Running the algorithm and getting the number of epochs. Using deepcopy on the weights so we don't apply the same results in the next pass of the loop.
        epochs = perceptron(input, output, copy.deepcopy(weights), value)
        print(f'Learning rate of {value} results in number of epochs of {epochs}')

        xValues.append(value)
        yValues.append(epochs)

        value = value + increment

    # Converting the arrays to numpy arrays
    xValues = numpy.array(xValues)
    yValues = numpy.array(yValues)

    # Drawing points
    plot.scatter(xValues, yValues, color = "orange")

    # Drawing a smooth line between the points
    model = make_interp_spline(xValues, yValues)
    x = numpy.linspace(xValues.min(), xValues.max(), 500)
    y = model(x)
    plot.plot(x, y, color = "red")

    plot.xlabel("Learning rate")
    plot.ylabel("Epochs")

    plot.show()