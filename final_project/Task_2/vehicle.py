from depot import Depot
import random
import copy

class Vehicle:
    def __init__(self, homeDepot):
        self.homeDepot = homeDepot
        self.currentLoad = 0
        self.currentDuration = 0
        self.route = []

    def getRouteDistance(self): 
        routeDistance = 0
        currentPosition = self.homeDepot.position

        for customer in self.route: 
            routeDistance += currentPosition.distance(customer.position)
            currentPosition = customer.position

        routeDistance += currentPosition.distance(self.homeDepot.position)

        return routeDistance

    def fitness(self):
        return self.getRouteDistance()
    
    def createOffspringVehicles(self, partnerVehicle):

        allCustomers = self.route + partnerVehicle.route

        offspring1 = Vehicle(self.homeDepot)
        offspring2 = Vehicle(partnerVehicle.homeDepot)

        flip = True
        for customer in allCustomers:
            if flip: 
                offspring1.route.append(customer)
            else: 
                offspring2.route.append(customer)
            
            flip = not flip

        # selfRandomCustomerIndex = random.randrange(0, len(self.route) - 1)
        # partnerRandomCustomerIndex = random.randrange(0, len(partnerVehicle.route) - 1)
        # offspring1 = self.copy()
        # offspring1.route.insert(selfRandomCustomerIndex, partnerVehicle.route[partnerRandomCustomerIndex])
        # offspring2 = partnerVehicle.copy()
        # offspring2.route.insert(partnerRandomCustomerIndex, self.route[selfRandomCustomerIndex])

        return offspring1, offspring2


    def mutate(self): # Swap mutation or scramble mutation
        
        random1 = random.randrange(0, len(self.route) - 1)
        random2 = random.randrange(0, len(self.route) - 1)

        while len(self.route) > 1 and random1 == random2:
            random2 = random.randrange(0, len(self.route) - 1)
        
        if random1 == random2: 
            print("Error: The number of points in the route is <= 1")
            return
        
        # Swap mutation
        random1Value = self.route[random1]
        self.route[random1] = self.route[random2]
        self.route[random2] = random1Value

    def copy(self):
        vehicleCopy = Vehicle(self.homeDepot)
        vehicleCopy.currentLoad = copy.copy(self.currentLoad)
        vehicleCopy.currentDuration = copy.copy(self.currentDuration)
        vehicleCopy.route = []

        for customer in self.route: 
            vehicleCopy.route.append(customer.copy())

        return vehicleCopy