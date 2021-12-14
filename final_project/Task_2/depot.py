class Depot: 
    def __init__(self, id = 0, maximumLoad = 0, maximumRouteDuration = 0, position = None):
        self.id = id
        self.initallyAssignedCustomers = []
        self.maximumLoad = 0
        self.maximumRouteDuration = 0
        self.position = position