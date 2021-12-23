from depot import Depot
import random

class Vehicle:
    def __init__(self, homeDepot, id):
        self.homeDepot = homeDepot
        self.id = id
        self.route = []

    def getRouteDistance(self): 
        routeDistance = 0
        currentPosition = self.homeDepot.position

        for customer in self.route: 
            routeDistance += currentPosition.distance(customer.position)
            currentPosition = customer.position

        routeDistance += currentPosition.distance(self.homeDepot.position)

        return routeDistance

    def getRouteCarryingLoad(self): 
        currentLoad = 0

        for customer in self.route: 
            currentLoad += customer.demand
        
        return currentLoad

    def fitness(self):
        
        distancePenalty = -1000 if self.homeDepot.maximumRouteDuration != 0 and self.getRouteDistance() > self.homeDepot.maximumRouteDuration else 0
        loadPenalty = -1000 if self.homeDepot.maximumLoad != 0 and self.getRouteCarryingLoad() > self.homeDepot.maximumLoad else 0

        fitness = len(self.route) / self.getRouteDistance()

        return fitness + distancePenalty + loadPenalty

    def createOffspringVehicles(self, partnerVehicle):
        
        allCustomers = list(self.route) + list(partnerVehicle.route)
        random.shuffle(allCustomers)
        
        offspring1 = Vehicle(self.homeDepot, self.id)
        offspring2 = Vehicle(partnerVehicle.homeDepot, partnerVehicle.id)

        length = int(len(allCustomers))

        for customer in allCustomers[:length//2]:
            offspring1.route.append(customer)
        
        for customer in allCustomers[length//2:]:
            offspring2.route.append(customer)

        return offspring1, offspring2

    def mutate(self, probability = 0.8): 
        
        max = 100 
        rand = random.randint(0, max)

        if rand > max*probability:
            return

        # Swap mutation
        if len(self.route) >= 2: 
            nr1 = random.randint(0, len(self.route) - 1)
            nr2 = random.randint(0, len(self.route) - 1)
            self.route[nr1], self.route[nr2] = self.route[nr2], self.route[nr1]
    
    def createRouteString(self):
        routeString = "0"

        for customer in self.route: 
            routeString += f' {customer.id}'
        routeString += " 0"

        return routeString

    def __str__(self):
        return f'{self.homeDepot.id} {self.id} {int(self.getRouteDistance())} {self.getRouteCarryingLoad()} {self.createRouteString()}'

    def __repr__(self): 
        return f'{self.homeDepot.id} {self.id} {int(self.getRouteDistance())} {self.getRouteCarryingLoad()} {self.createRouteString()}'