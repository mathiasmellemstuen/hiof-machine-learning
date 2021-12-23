from position import Position

class Customer:
    def __init__(self, id, position, serviceDuration, demand):
        self.id = id
        self.position = position
        self.serviceDuration = serviceDuration
        self.demand = demand

    def __str__(self):
        return f'Customer ID {self.id}: {self.position} with service duration: {self.serviceDuration} and demand: {self.demand}'

    def __repr__(self): 
        return f'Customer {self.id}'