import math
import copy

class Position: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other): 
        return math.sqrt(abs(other.x - self.x)**2 + abs(other.y - self.y)**2)
    
    def __str__(self): 
        return f'Position: x: {self.x} y: {self.y}'

    def copy(self): 
        return Position(copy.copy(self.x), copy.copy(self.y))