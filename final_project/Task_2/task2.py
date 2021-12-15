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
import sys

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

        plot.plot(x, y, color = randomColor(), linewidth = 0.85)

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

def randomColor():
    return (random.random(), random.random(), random.random())

def geneticAlgorithm(vehicles, iterations):

    for i in range(0, iterations):

        sys.stdout.write(f'\rIteration progress: {int(i / iterations * 100) + 1}%')
        sys.stdout.flush()

        pair = random.sample(vehicles, 2)
        o1, o2 = pair[0].createOffspringVehicles(pair[1])

        o1.mutate()
        o2.mutate()

        if o1.fitness() + o2.fitness() < pair[0].fitness() + pair[1].fitness():
            vehicles.remove(pair[0])
            vehicles.append(o1)
            vehicles.remove(pair[1])
            vehicles.append(o2)

    return vehicles

def totalDistance(vehicles):
    score = 0 

    for vehicle in vehicles:
        score = score + vehicle.getRouteDistance()
    
    return score

if __name__ == "__main__":
    numVehicles, numCustomers, numDepots, depots, customers = readAndParseDataFile("p01.txt")

    plot.figure(0)
    plotPositions(customers, depots)
    vehicles = generateRandomPopulation(numVehiclesPerDepot = numVehicles, depots = depots, customers = customers)
    plot.title(f'Total traveling distance: {int(totalDistance(vehicles))}')
    plotVehicles(vehicles)

    plot.figure(1)
    plotPositions(customers, depots)
    newVehicles = geneticAlgorithm(vehicles, 100000)
    plot.title(f'Total traveling distance: {int(totalDistance(newVehicles))}')
    plotVehicles(newVehicles)

    plot.show()