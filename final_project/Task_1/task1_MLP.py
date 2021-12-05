import numpy

X = [1, 1, 1, 1]

weights1 = numpy.random.randn(4, 4)
weights2 = numpy.random.randn(4, 1)

def sigmoidFunction(value):
    return 1/(1 + numpy.exp(-value))

def forwardPropagation(X): 
    return sigmoidFunction(numpy.dot(sigmoidFunction(numpy.dot(X, weights1)), weights2))

def costFunction(value): 
    pass 

if __name__ == "__main__":
    print(forwardPropagation(X))