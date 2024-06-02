class TimeSlot:
    """
    Represents a time slot in the scheduling system.
    
    Attributes:
        id (int): The unique identifier for the time slot.
        time (str): The specific time of the time slot.
    """
    def __init__(self, id, time):
        self.id = id
        self.time = time

    def get_id(self):
        return self.id

    def get_time(self):
        return self.time
