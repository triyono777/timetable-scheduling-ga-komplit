class Room:
    """
    Represents a room in the scheduling system.
    
    Attributes:
        number (str): The room number or identifier.
        capacity (int): The seating capacity of the room.
    """
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

    def get_number(self):
        return self.number

    def get_capacity(self):
        return self.capacity
