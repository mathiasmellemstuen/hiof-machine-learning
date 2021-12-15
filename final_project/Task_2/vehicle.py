from depot import Depot
import random
import copy

class Vehicle:
    def __init__(self, homeDepot):
        self.homeDepot = homeDepot
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
        random.shuffle(allCustomers)
        
        offspring1 = Vehicle(self.homeDepot.copy())
        offspring2 = Vehicle(partnerVehicle.homeDepot.copy())

        length = int(len(allCustomers))

        for customer in allCustomers[:length//2]:
            offspring1.route.append(customer.copy())
        
        for customer in allCustomers[length//2:]:
            offspring2.route.append(customer.copy())

        return offspring1, offspring2


    def mutate(self): # Swap mutation or scramble mutation

        # Swap mutation
        pair = random.sample(self.route, 2)
        pair[0], pair[1] = pair[1], pair[0]


    def __str__(self):
        return f'Belonging to depot {self.homeDepot.id} with a route of {len(self.route)} customers'