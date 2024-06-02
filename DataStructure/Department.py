class Department:
    """
    Represents a department in the scheduling system.
    
    Attributes:
        name (str): The name of the department.
        courses (list): The list of courses offered by the department.
    """
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def get_name(self):
        return self.name

    def get_courses(self):
        return self.courses
