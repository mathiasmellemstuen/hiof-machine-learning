class Depot: 
    def __init__(self, id = 0, maximumLoad = 0, maximumRouteDuration = 0, position = None):
        self.id = id
        self.maximumLoad = maximumLoad 
        self.maximumRouteDuration = maximumRouteDuration
        self.position = position

    def __str__(self):
        return f'Depot ID: {self.id}, maximum load: {self.maximumLoad} maximum route duration: {self.maximumRouteDuration} position: {self.position}'