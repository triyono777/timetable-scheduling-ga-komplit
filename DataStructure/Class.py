class Class:
    """
    Represents a class in the scheduling system.
    
    Attributes:
        id (int): The unique identifier for the class.
        department (Department): The department offering the class.
        course (Course): The course being taught in the class.
        professors (list): The list of possible professors for the class (initially None).
        timeslots (list): The list of possible timeslots for the class (initially None).
        room (Room): The room assigned to the class (initially None).
    """
    def __init__(self, id, department, course):
        self.id = id
        self.department = department
        self.course = course
        self.professors = None
        self.timeslots = None
        self.room = None

    def get_id(self):
        return self.id

    def get_department(self):
        return self.department

    def get_course(self):
        return self.course

    def get_professor(self):
        return self.professor

    def get_timeslot(self):
        return self.timeslot

    def get_room(self):
        return self.room

    def set_professor(self, professor):
        self.professor = professor

    def set_timeslot(self, timeslot):
        self.timeslot = timeslot

    def set_room(self, room):
        self.room = room

    def __str__(self):
        return f"{self.department.get_name()}, {self.course.get_number()}, {self.room.get_number()}, {self.professor.get_id()}, {self.timeslot.get_id()}"
