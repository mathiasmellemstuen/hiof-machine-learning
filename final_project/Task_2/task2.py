# Task 2: Multiple Depots Vehicle Routing Problem (MDVRP)

# References used in task 2: 

import numpy
import matplotlib.pyplot as plot
from customer import Customer 
from depot import Depot
import re

def readAndParseDataFile(file): 

    file = open("data/" + file, "r")
    lines = file.read().splitlines()

    firstLine = [int(i) for i in re.findall("\d+", lines[0])]

    numVehicles = firstLine[0]
    numCustomers = firstLine[1]
    numDepots = firstLine[2]

    lines.pop(0) # Removing the first line since we already have gathered all data form it. This simplifies the rest of the parsing

    depots = []
    customers = []
    currentDepotIndex = 0
    for line in lines:

        digits = [int(i) for i in re.findall("\d+", line)]

        if re.match("^(\d{1,}\s\d{1,})$", line):
            depots.append(Depot(digits[1], digits[0]))
            continue
        
        if re.match("^(\d{1,} {1,}\d{1,}\d{1,} {1,}\d{1,} {1,}\d{1,} {1,}\d{1,} {1,}\d{1,} {1,}\d{1,})$", line):
            depots[currentDepotIndex].position = numpy.array([digits[1], digits[2]])
            currentDepotIndex = currentDepotIndex + 1
            continue

        customers.append(Customer(digits[0], numpy.array([digits[1], digits[2]]), digits[3], digits[4]))

    return numVehicles, numCustomers, numDepots, depots, customers
    
if __name__ == "__main__": 
    numVehicles, numCustomers, numDepots, depots, customers = readAndParseDataFile("p01.txt")
    print(numVehicles)