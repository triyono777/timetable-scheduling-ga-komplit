from DataStructure.Class import Class
import random as rnd

from Utils.constants import HARD_CONSTRAINT_PENALTY, SOFT_CONSTRAINT_PENALTY


class Schedule:
    """
    Represents a schedule in the scheduling system.
    
    Attributes:
        data (object): The data used to initialize the schedule.
        classes (list): The list of classes in the schedule.
        numbOfConflicts (int): The number of conflicts in the schedule.
        fitness (float): The fitness score of the schedule.
        classNumb (int): The number of classes.
        isFitnessChanged (bool): Flag indicating if the fitness has changed.
    """
    def __init__(self, data):
        self.data = data
        self.classes = []
        self.numbOfConflicts = 0
        self.fitness = -1
        self.classNumb = 0
        self.isFitnessChanged = True

    def get_classes(self):
        self.isFitnessChanged = True
        return self.classes

    def get_numbOfConflicts(self):
        return self.numbOfConflicts

    def get_fitness(self):
        if self.isFitnessChanged:
            self.fitness = self.calculate_fitness_with_soft_constraints()
            self.isFitnessChanged = False
        return self.fitness

    def initialize(self):
        """
        Initializes the schedule with random classes, assigning random timeslots, rooms, and professors.
        
        Returns:
            Schedule: The initialized schedule with randomly assigned classes.
        """
        departments = self.data.get_departments()
        for department in departments:
            courses = department.get_courses()
            for course in courses:
                newClass = Class(self.classNumb, department, course)
                self.classNumb += 1 # Increment class number
                # Randomly assign timeslot, room and professor to the new class
                newClass.set_timeslot(self.data.get_timeslots()[rnd.randrange(len(self.data.get_timeslots()))])
                newClass.set_room(self.data.get_rooms()[rnd.randrange(len(self.data.get_rooms()))])
                newClass.set_professor(course.get_professors()[rnd.randrange(len(course.get_professors()))])
                self.classes.append(newClass)
        return self

    def calculate_fitness(self):
        # Calculate fitness based on hard constraints
        self.numOfConflicts = 0
        hard_constraint_violations = 0
        classes = self.get_classes()
        
        for i in range(0, len(classes)):
            # Check if the room capacity is less than the maximum number of students
            if classes[i].get_room().get_capacity() < classes[i].get_course().get_max_number_of_students():
                hard_constraint_violations += 1

            for j in range(i + 1, len(classes)):
                # Check for overlaps in timeslots, rooms and professors
                if classes[i].get_timeslot() == classes[j].get_timeslot() and classes[i].get_id() != \
                        classes[j].get_id():
                    if classes[i].get_room() == classes[j].get_room():
                        hard_constraint_violations += 1
                    if classes[i].get_professor() == classes[j].get_professor():
                        hard_constraint_violations += 1
                        
        # Calculate fitness score based on the number of violations
        self.numOfConflicts = hard_constraint_violations * HARD_CONSTRAINT_PENALTY
        return 1 / (1.0 * self.numOfConflicts + 1)

    def calculate_fitness_with_soft_constraints(self):
        # Calculate fitness based on hard & soft constraints
        self.numOfConflicts = 0
        hard_constraint_violations = 0
        soft_constraint_violations = 0
        classes = self.get_classes()
        
        # Hard constraints
        for i in range(0, len(classes)):
            # Check if room capacity exceeds the number of students
            if classes[i].get_room().get_capacity() < classes[i].get_course().get_max_number_of_students():
                hard_constraint_violations += 1

            for j in range(i + 1, len(classes)):
                # Check for overlaps in timeslots, rooms and professors
                if classes[i].get_timeslot() == classes[j].get_timeslot() and classes[i].get_id() != \
                        classes[j].get_id():
                    if classes[i].get_room() == classes[j].get_room():
                        hard_constraint_violations += 1
                    if classes[i].get_professor() == classes[j].get_professor():
                        hard_constraint_violations += 1
                        
        # Soft constraints
        for cls in classes:
            # Check if class timeslot matches the preferred timeslots
            preferred_timeslots = cls.get_course().get_preferred_timeslots()
            if len(preferred_timeslots) > 0:
                if cls.get_timeslot().get_id() not in preferred_timeslots:
                    soft_constraint_violations += 1
            # Check if classroom matches the preferred rooms
            preferred_rooms = cls.get_course().get_preferred_rooms()
            if len(preferred_rooms) > 0:
                if cls.get_room().get_number() not in preferred_rooms:
                    soft_constraint_violations += 1

        # Calculate fitness score based on the number of violations
        self.numbOfConflicts = hard_constraint_violations * HARD_CONSTRAINT_PENALTY + soft_constraint_violations * SOFT_CONSTRAINT_PENALTY
        return 0 - self.numbOfConflicts

    def __str__(self):
        return ', '.join([str(cls) for cls in self.classes])
