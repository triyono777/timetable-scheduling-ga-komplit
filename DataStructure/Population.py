from DataStructure.Schedule import Schedule


class Population:
    """
    Represents a population of schedules in the scheduling system.
    
    Attributes:
        size (int): The size of the population.
        schedules (list): The list of schedules in the population.
    """
    def __init__(self, size, data):
        self.size = size
        self.schedules = [Schedule(data).initialize() for _ in range(size)]

    def get_schedules(self):
        return self.schedules
