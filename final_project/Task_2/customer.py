from turtle import position
import numpy
import pandas

class Customer:
    def __init__(self, id, position, serviceDuration, demand):
        self.id = id
        self.position = position
        self.serviceDuration = serviceDuration
        self.demand = demand
    
    def __str__(self):
        return f'Customer ID {self.id}: Position x: {self.position[0]} and y: {self.position[1]} with service duration: {self.serviceDuration} and demand: {self.demand}'