class Professor:
    """
    Represents a professor in the scheduling system.
    
    Attributes:
        id (int): The unique identifier for the professor.
        name (str): The name of the professor.
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name
