# Task 2: Multiple Depots Vehicle Routing Problem (MDVRP)

# References used in task 2: 

from audioop import cross
from tabnanny import check
import numpy
import matplotlib.pyplot as plot
from customer import Customer 
from depot import Depot
from position import Position
from vehicle import Vehicle
import re
import random

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
            depots[currentDepotIndex].position = Position(digits[1], digits[2])
            depots[currentDepotIndex].id = currentDepotIndex
            currentDepotIndex = currentDepotIndex + 1
            continue

        customers.append(Customer(id = digits[0], position = Position(digits[1], digits[2]), serviceDuration = digits[3], demand = digits[4]))

    return numVehicles, numCustomers, numDepots, depots, customers

def plotPositions(customers, depots):
    xValues = [customer.position.x for customer in customers]
    yValues = [customer.position.y for customer in customers]

    plot.scatter(xValues, yValues)

    xValues = [depot.position.x for depot in depots]
    yValues = [depot.position.y for depot in depots]

    plot.scatter(xValues, yValues, marker="p")

def plotVehicles(vehicles): 
    for vehicle in vehicles:
        x = [customer.position.x for customer in vehicle.route]
        x.append(vehicle.homeDepot.position.x)
        x.insert(0, vehicle.homeDepot.position.x)
        y = [customer.position.y for customer in vehicle.route]
        y.append(vehicle.homeDepot.position.y)
        y.insert(0, vehicle.homeDepot.position.y)

        plot.plot(x, y, color = randomColor())

def testVehicles(vehicles): 
    print("Simular customer test")
    for vehicle1 in vehicles: 
        for vehicle2 in vehicles: 
            if vehicle1 is vehicle2: 
                continue
            
            for customer1 in vehicle1.route: 
                for customer2 in vehicle2.route:
                    if customer1 is customer2:
                        print("ERROR")

def getNextClosestCustomer(depot, takenCustomers, customers): 

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
    vehicles = []

    for depot in depots:
        for i in range(0, numVehiclesPerDepot):
            vehicle = Vehicle(depot)
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

def fitness(vehicle): 
    pass

def crossover(parent1, parent2): 
    pass

def selectNewPopulation(offspring, oldPopulation): 
    pass

# t = 0
# Generate random population
# Evaluate the fitness of each invidual in the population
# loop:
#   Select parents based on fitness
#   Apply crossover to create offstring from the selected parents
#   Apply mutation to offspring
#   Evaluate fitness of offspring
#   Select new population based on current offspring and parents 
#   Checking if values is satifactory, if so, break.


def randomColor():
    return (random.random(), random.random(), random.random())

def geneticAlgorithm(vehicles, iterations):

    for i in range(0, iterations):
        # print(f'Iteration {i}/{iterations}')

        doneVehicles = []
        offsprings = []
        while len(vehicles) - len(doneVehicles) > 1:
            
            pair = random.sample(vehicles, 2)

            offspring1, offspring2 = pair[0].createOffspringVehicles(vehicles[1])
            
            if offspring1.fitness() < pair[0].fitness():
                # offsprings.append((pair[0], offspring1))
                pair[0] = offspring1
            

            if offspring2.fitness() < pair[1].fitness():
                # offsprings.append((pair[1], offspring2))
                pair[1] = offspring2

            doneVehicles.append(pair[0])
            doneVehicles.append(pair[1])

        # print("Before")
        # testVehicles(vehicles)

        # for offspring in offsprings: 
        #     for i in range(0, len(vehicles)): 
        #         if vehicles[i] is offspring[0]: 
        #             vehicles[i] = offspring[1]

        print("After")
        testVehicles(vehicles)
    return vehicles

def checkForSimularVehicles(group1, group2): 
    for vehicle1 in group1: 
        for vehicle2 in group2: 
            if vehicle1.fitness() == vehicle2.fitness(): 
                print("The same!")

if __name__ == "__main__":
    numVehicles, numCustomers, numDepots, depots, customers = readAndParseDataFile("p01.txt")

    plot.figure(0)
    plotPositions(customers, depots)
    vehicles = generateRandomPopulation(numVehiclesPerDepot = numVehicles, depots = depots, customers = customers)    
    plotVehicles(vehicles)
    plot.figure(1)
    plotPositions(customers, depots)
    newVehicles = geneticAlgorithm(vehicles, 100)
    plotVehicles(newVehicles)

    checkForSimularVehicles(vehicles, newVehicles)
    plot.show()