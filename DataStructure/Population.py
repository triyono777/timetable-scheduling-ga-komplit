from DataStructure.Schedule import Schedule


class Population:
    def __init__(self, size, data):
        self.size = size
        self.schedules = [Schedule(data).initialize() for _ in range(size)]

    def get_schedules(self):
        return self.schedules
