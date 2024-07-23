class Course:
    """
    Represents a course in the scheduling system.
    
    Attributes:
        number (str): The unique number identifier for the course.
        name (str): The name of the course.
        professors (list): The list of professors who can teach the course.
        needLab (bool): course need lab or not.
        preferred_timeslots (list): The list of preferred timeslots for the course (default is an empty list).
        preferred_rooms (list): The list of preferred rooms for the course (default is an empty list).
    """
    def __init__(self, number, name, professors, needLab, preferred_timeslots=[], preferred_rooms=[]):
        self.number = number
        self.name = name
        self.professors = professors
        self.needLab = needLab
        self.preferred_timeslots = preferred_timeslots
        self.preferred_rooms = preferred_rooms

    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

    def get_professors(self):
        return self.professors

    def get_needLab(self):
        return self.needLab

    def get_preferred_timeslots(self):
        return self.preferred_timeslots

    def get_preferred_rooms(self):
        return self.preferred_rooms

    def __str__(self):
        return self.name
