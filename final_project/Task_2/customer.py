from position import Position
import copy

class Customer:
    def __init__(self, id, position, serviceDuration, demand):
        self.id = id
        self.position = position
        self.serviceDuration = serviceDuration
        self.demand = demand

    def __str__(self):
        return f'Customer ID {self.id}: {self.position} with service duration: {self.serviceDuration} and demand: {self.demand}'

    def copy(self): 
        newCustomer = Customer(copy.copy(self.id), self.position.copy(), copy.copy(self.serviceDuration), copy.copy(self.demand))
        return newCustomer