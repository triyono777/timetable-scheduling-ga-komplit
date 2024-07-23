class Room:
    """
    Represents a room in the scheduling system.
    
    Attributes:
        number (str): The room number or identifier.
        isLab (bool): The tipe lab.
    """
    def __init__(self, number, isLab = False):
        self.number = number
        self.isLab = isLab

    def get_number(self):
        return self.number

    def get_isLab(self):
        return self.isLab
