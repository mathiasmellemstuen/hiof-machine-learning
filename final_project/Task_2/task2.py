# Task 2: Multiple Depots Vehicle Routing Problem (MDVRP)

# References used in task 2: 

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

def generateRandomPopulation(numVehiclesPerDepot, depots, customers):
    vehicles = []

    for depot in depots:
        for i in range(0, numVehiclesPerDepot):
            vehicle = Vehicle(depot)
            vehicles.append(vehicle)

    nextVehicle = 0
    for customer in customers:
        vehicles[nextVehicle].route.append(customer)
        nextVehicle = nextVehicle + 1 if (nextVehicle + 1) % len(vehicles) != 0 else 0 

    # for customer in customers:

    #     closestDepot = None

    #     for depot in depots:
    #         closestDepot = depot if closestDepot == None or depot.position.distance(customer.position) > closestDepot.position.distance(customer.position) else closestDepot
        
    #     # for vehicle in vehicles:
    #     #     if vehicle.homeDepot is closestDepot: 
        
    #     closestDepot.initallyAssignedCustomers.append(customer)
    
    # for depot in depots:

    #     depot.initallyAssignedCustomers.sort(key=lambda element: depot.position.distance(element.position))

    #     currentDepotVehicles = []

    #     for vehicle in vehicles: 
    #         if vehicle.homeDepot is depot: 
    #             currentDepotVehicles.append(vehicle)

    #     nextVehicle = 0

    #     for customer in depot.initallyAssignedCustomers:
    #         currentDepotVehicles[nextVehicle].route.append(customer)

    #         nextVehicle = nextVehicle + 1 if (nextVehicle + 1) % numVehiclesPerDepot != 0 else 0
            
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
        print(f'Iteration {i}/{iterations}')

        offsprings = [] 

        for i in range(0, len(vehicles)):
            for j in range(0, len(vehicles)): 
                
                vehicle1 = vehicles[i]
                vehicle2 = vehicles[j]

                if vehicle1 is vehicle2: 
                    continue
                
                if vehicle1.homeDepot is vehicle2.homeDepot:
                    continue

                offspring1, offspring2 = vehicle1.createOffspringVehicles(vehicle2)

                offspring1.mutate()
                offspring2.mutate()

                # offsprings.append(offspring1)
                # offsprings.append(offspring2)

                if offspring1.fitness() < vehicle1.fitness():
                    offsprings.append(offspring1)
                    vehicles.pop(i)
                
                if(offspring2.fitness() < vehicle2.fitness()):
                    offsprings.append(offspring2)
                    vehicles.pop(j)

        wantedNumberOfVehicles = len(vehicles)

        vehicles = vehicles + offsprings

        # allVehicles.sort(key=lambda element: element.fitness())

        # endVehicles = []
        # for i in range(0, 4):
        #     depotVehicles = []
        #     for vehicle in allVehicles:
        #         if vehicle.homeDepot.id == i:
        #             depotVehicles.append(vehicle)
            
        #     depotVehicles.sort(key=lambda element: element.fitness())
        #     depotVehicles = depotVehicles[:4]
        #     endVehicles = endVehicles + depotVehicles

        # vehicles = allVehicles[:wantedNumberOfVehicles]

    for vehicle in vehicles: 
        print(vehicle.fitness())
    
    return vehicles
if __name__ == "__main__":
    numVehicles, numCustomers, numDepots, depots, customers = readAndParseDataFile("p01.txt")

    plotPositions(customers, depots)

    vehicles = generateRandomPopulation(numVehiclesPerDepot = numVehicles, depots = depots, customers = customers)    
    vehicles = geneticAlgorithm(vehicles, 100000)

    for vehicle in vehicles:
        x = [customer.position.x for customer in vehicle.route]
        x.append(vehicle.homeDepot.position.x)
        x.insert(0, vehicle.homeDepot.position.x)
        y = [customer.position.y for customer in vehicle.route]
        y.append(vehicle.homeDepot.position.y)
        y.insert(0, vehicle.homeDepot.position.y)

        plot.plot(x, y, color = randomColor())

    plot.show()