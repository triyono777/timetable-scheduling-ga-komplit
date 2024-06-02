from DataStructure.Class import Class
import random as rnd

from Utils.constants import HARD_CONSTRAINT_PENALTY, SOFT_CONSTRAINT_PENALTY


class Schedule:
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
        departments = self.data.get_departments()
        for department in departments:
            courses = department.get_courses()
            for course in courses:
                newClass = Class(self.classNumb, department, course)
                self.classNumb += 1
                newClass.set_timeslot(self.data.get_timeslots()[rnd.randrange(len(self.data.get_timeslots()))])
                newClass.set_room(self.data.get_rooms()[rnd.randrange(len(self.data.get_rooms()))])
                newClass.set_professor(course.get_professors()[rnd.randrange(len(course.get_professors()))])
                self.classes.append(newClass)
        return self

    def calculate_fitness(self):
        self.numOfConflicts = 0
        hard_constraint_violations = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if classes[i].get_room().get_capacity() < classes[i].get_course().get_max_number_of_students():
                hard_constraint_violations += 1

            for j in range(i + 1, len(classes)):

                if classes[i].get_timeslot() == classes[j].get_timeslot() and classes[i].get_id() != \
                        classes[j].get_id():
                    if classes[i].get_room() == classes[j].get_room():
                        hard_constraint_violations += 1
                    if classes[i].get_professor() == classes[j].get_professor():
                        hard_constraint_violations += 1

        self.numOfConflicts = hard_constraint_violations * HARD_CONSTRAINT_PENALTY
        return 1 / (1.0 * self.numOfConflicts + 1)

    def calculate_fitness_with_soft_constraints(self):
        self.numOfConflicts = 0
        hard_constraint_violations = 0
        soft_constraint_violations = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if classes[i].get_room().get_capacity() < classes[i].get_course().get_max_number_of_students():
                hard_constraint_violations += 1

            for j in range(i + 1, len(classes)):

                if classes[i].get_timeslot() == classes[j].get_timeslot() and classes[i].get_id() != \
                        classes[j].get_id():
                    if classes[i].get_room() == classes[j].get_room():
                        hard_constraint_violations += 1
                    if classes[i].get_professor() == classes[j].get_professor():
                        hard_constraint_violations += 1

        for cls in classes:
            preferred_timeslots = cls.get_course().get_preferred_timeslots()
            if len(preferred_timeslots) > 0:
                if cls.get_timeslot().get_id() not in preferred_timeslots:
                    soft_constraint_violations += 1
            preferred_rooms = cls.get_course().get_preferred_rooms()
            if len(preferred_rooms) > 0:
                if cls.get_room().get_number() not in preferred_rooms:
                    soft_constraint_violations += 1

        self.numbOfConflicts = hard_constraint_violations * HARD_CONSTRAINT_PENALTY + soft_constraint_violations * SOFT_CONSTRAINT_PENALTY
        return 0 - self.numbOfConflicts

    def __str__(self):
        return ', '.join([str(cls) for cls in self.classes])
