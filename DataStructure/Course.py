class Course:
    """
    Represents a course in the scheduling system.
    
    Attributes:
        number (str): The unique number identifier for the course.
        name (str): The name of the course.
        professors (list): The list of professors who can teach the course.
        max_number_of_students (int): The maximum number of students that can enroll in the course.
        preferred_timeslots (list): The list of preferred timeslots for the course (default is an empty list).
        preferred_rooms (list): The list of preferred rooms for the course (default is an empty list).
    """
    def __init__(self, number, name, professors, max_number_of_students, preferred_timeslots=[], preferred_rooms=[]):
        self.number = number
        self.name = name
        self.professors = professors
        self.max_number_of_students = max_number_of_students
        self.preferred_timeslots = preferred_timeslots
        self.preferred_rooms = preferred_rooms

    def get_number(self):
        return self.number

    def get_name(self):
        return self.name

    def get_professors(self):
        return self.professors

    def get_max_number_of_students(self):
        return self.max_number_of_students

    def get_preferred_timeslots(self):
        return self.preferred_timeslots

    def get_preferred_rooms(self):
        return self.preferred_rooms

    def __str__(self):
        return self.name
