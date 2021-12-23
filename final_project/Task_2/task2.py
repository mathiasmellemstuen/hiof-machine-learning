# Task 2: Multiple Depots Vehicle Routing Problem (MDVRP)

# References used in task 2: 
# - W_10 C Ripon.pdf - lecture slides taken from canvas
# - https://www.sciencedirect.com/science/article/pii/S0952197607000887?casa_token=SPuwxrQ7L4IAAAAA:RzI11st8D7ewvhHRwIiQ3EIwqNufJQZWXdIyxnAfrb-yqBK1qAiagNagBIu0XdpPhF25V35XDDw - A hybrid genetic algorithm for the multi-depot vehicle routing problem

import matplotlib.pyplot as plot
from customer import Customer 
from depot import Depot
from position import Position
from vehicle import Vehicle
import re
import random

def getDigits(line):
    """
    Returns a list with all the digits in the string / line

    Arguments
    ---------
    Line: This is the string or line we want to extract all the numbers from
    """
    return [int(i) for i in re.findall("\d+", line)]

def readAndParseSolutionFile(file): 
    """
    This function reads a solution file and returns the length of the solution in the solution file


    Arguments
    ---------
    file: The name of the solution file (example: p01.txt)
    """
    file = open("solutions/" + file, "r")
    lines = file.read().splitlines()

    return float(lines[0])

def readAndParseDataFile(file): 
    
    """
    This function reads and parse a data file. This function will then return the number of vehicles, number of customers, number of depots, depots and customers from the file.

    Arguments
    ---------
    file: The name of the data file (example: p01.txt)
    """

    file = open("data/" + file, "r")
    lines = file.read().splitlines()

    firstLine = getDigits(lines[0]) 

    numVehicles = firstLine[0]
    numCustomers = firstLine[1]
    numDepots = firstLine[2]

    depots = []
    customers = []
    depotIndex = 0

    for line in lines[1:numDepots + 1]:
        digits = getDigits(line) 
        depots.append(Depot(0, digits[1], digits[0]))
    
    for line in lines[len(lines)-numDepots:]:
        digits = getDigits(line) 
        depots[depotIndex].position = Position(digits[1], digits[2])
        depots[depotIndex].id = depotIndex
        depotIndex = depotIndex + 1

    for line in lines[numDepots + 1:-numDepots]:
        digits = getDigits(line) 
        customers.append(Customer(id = digits[0], position = Position(digits[1], digits[2]), serviceDuration = digits[3], demand = digits[4]))
    
    return numVehicles, numCustomers, numDepots, depots, customers

def plotPositions(customers, depots):
    """
    This function plots customers and depots in a scatter plot. The customers will appear as filled circles and the depots will appear as filled polygons.

    Arguments
    ---------
    customers: A list of all the customers to plot. List of Customer objects. 
    depots: A list of all the depots to plot. List of Depot objects.
    """

    xValues = [customer.position.x for customer in customers]
    yValues = [customer.position.y for customer in customers]

    plot.scatter(xValues, yValues)

    xValues = [depot.position.x for depot in depots]
    yValues = [depot.position.y for depot in depots]

    plot.scatter(xValues, yValues, marker="p")

def plotVehicles(vehicles):
    """
    This function plots the vehicle routes between the depots and customers. Each route will be plotted with a random color. 

    Arguments
    ---------
    vehicles: A list of Vehicle objects. All the vehicles with routes to plot. 
    """

    for vehicle in vehicles:
        x = [customer.position.x for customer in vehicle.route]
        x.append(vehicle.homeDepot.position.x)
        x.insert(0, vehicle.homeDepot.position.x)
        y = [customer.position.y for customer in vehicle.route]
        y.append(vehicle.homeDepot.position.y)
        y.insert(0, vehicle.homeDepot.position.y)

        plot.plot(x, y, color = randomColor(), linewidth = 0.85)

def getNextClosestCustomer(depot, takenCustomers, customers): 
    """
    This function is used to initally distribute customers between depots, to then distribute the customers further to the depot vehicles.
    It calculates and return which customer that is closest to the depot that is not already taken by any other depots.

    Arguments
    ---------
    depot: The depot we are finding the closest customer to
    takenCustomers: A list of already taken customers
    customers: A list of all customers 
    """
    closest = None

    for customer in customers: 
        taken = False
        for takenCustomer in takenCustomers:
            if takenCustomer is customer: 
                taken = True

        if taken == False: 
            closest = customer
            break
    
    for customer in customers: 
        if depot.position.distance(customer.position) < depot.position.distance(closest.position) and customer is not closest:

            taken = False

            for takenCustomer in takenCustomers:
                if takenCustomer is customer:
                    taken = True

            if taken == False: 
                closest = customer
        
    takenCustomers.append(closest)
    return closest

def generateRandomPopulation(numVehiclesPerDepot, depots, customers):
    """
    This is for initiating the genetic algorithm. This function is distributing customers to vehicles to generate a initial solution that will later be improved by the genetic algorithm.

    Arguments
    ---------
    numVehiclesPerDepot: The maximum number of vehicles allowed per depot
    depots: A list of all depots
    customers: A list of all customers
    """

    vehicles = []

    for depot in depots:
        for i in range(0, numVehiclesPerDepot):
            vehicle = Vehicle(depot, i)
            vehicles.append(vehicle)

    nextVehicle = 0

    takenCustomers = []

    while len(takenCustomers) != len(customers):

        nextClosestCustomer = getNextClosestCustomer(vehicles[nextVehicle].homeDepot, takenCustomers, customers)

        if nextClosestCustomer == None:
            break

        vehicles[nextVehicle].route.append(nextClosestCustomer)
        nextVehicle = nextVehicle + 1 if (nextVehicle + 1) % len(vehicles) != 0 else 0
            
    return vehicles

def randomColor():
    """
    Generating a random color
    """
    return (random.random(), random.random(), random.random())

def geneticAlgorithm(vehicles, iterations):
    """
    Running the genetic algorithm to improve the vehicle route.

    Arguments
    ---------
    vehicles: All the vehicles to improve with the genetic algorithm
    itearations: The number of passes to run the algorithm. 
    """
    for i in range(0, iterations):

        pair = tournament(vehicles)
        o1, o2 = pair[0].createOffspringVehicles(pair[1])

        o1.mutate()
        o2.mutate()

        if o1.fitness() + o2.fitness() > pair[0].fitness() + pair[1].fitness():
            vehicles.remove(pair[0])
            vehicles.append(o1)
            vehicles.remove(pair[1])
            vehicles.append(o2)

    return vehicles

def tournament(vehicles, probability = 0.8):
    """
    Selecting the two best vehicles based on their fitness function. The function has a probability to select a random vehicle

    Arguments
    ---------
    vehicles: A list of Vehicle objects.
    probability: The porbability for selecting the two best vehicles. This is 0.8 by standard. That indicates that it is 0.2 (1 - 0,8) in probability for selecting two random vehicles instead of the best vehicles.
    """
    vehicles.sort(key = lambda vehicle: vehicle.fitness(), reverse=True)

    max = 100 
    rand = random.randint(0, max)

    if rand < max*probability:
        return [vehicles[0], vehicles[1]]
    
    return random.sample(vehicles, 2)

def totalDistance(vehicles):
    """
    Calculate the total distance of all the vehicles routes combined

    Arguments
    ---------
    vehicles: A list of Vehicle objects. 
    """

    score = 0 

    for vehicle in vehicles:
        score = score + vehicle.getRouteDistance()
    
    return score

def printResult(vehicles):
    """
    Printing the result of a solution on the format given in the task. This will first print the total distance of the solution and then print all the vehicles data and routes

    Arguments
    ---------
    vehicles: A list of Vehicle objects. 
    """
    print("")
    print("-----RESULT-----")
    print(int(totalDistance(vehicles)))

    vehicles.sort(key=lambda vehicle: vehicle.homeDepot.id)
    for vehicle in vehicles:
        print(vehicle)

def runAllFiles():
    """
    This function is running the genetic algorithm on all the files and then prints the result for each one of them. It is iterating the genetic algorithm for each file 100 000 times. 
    """
    for i in range(1, 24):
        fileString = f'{"p0" if i < 10 else "p"}{i}.txt'
        solutionLength = readAndParseSolutionFile(fileString)
        numVehicles, numCustomers, numDepots, depots, customers = readAndParseDataFile(fileString)

        vehicles = generateRandomPopulation(numVehiclesPerDepot = numVehicles, depots = depots, customers = customers)
        vehiclesDistance = totalDistance(vehicles)

        newVehicles = geneticAlgorithm(vehicles, 100000)

        print(f'{fileString} | Inital random distance {int(vehiclesDistance):<7} | My result {int(totalDistance(newVehicles)):<7} | solution distance {solutionLength:<7} | passed {"yes" if totalDistance(newVehicles) < (solutionLength * 1.15) else "no"}')

def runFirstFileWithPlot(): 
    """
    This function is running the first file (p01.txt) and plotting the result from both before and after the genetic algorithm. It is iterating the genetic algorithm 100 000 times.
    """
    numVehicles, numCustomers, numDepots, depots, customers = readAndParseDataFile("p01.txt")

    plot.figure(0)
    plotPositions(customers, depots)
    vehicles = generateRandomPopulation(numVehiclesPerDepot = numVehicles, depots = depots, customers = customers)
    
    plot.title(f'Total traveling distance: {int(totalDistance(vehicles))}')
    plotVehicles(vehicles)

    plot.figure(1)
    plotPositions(customers, depots)
    newVehicles = geneticAlgorithm(vehicles, 100000)

    printResult(newVehicles)
    plot.title(f'Total traveling distance: {int(totalDistance(newVehicles))}')
    plotVehicles(newVehicles)
    
    plot.show()

if __name__ == "__main__":
    runFirstFileWithPlot()
    # runAllFiles()