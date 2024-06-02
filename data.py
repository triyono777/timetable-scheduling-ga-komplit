# data.py
from DataStructure.Course import Course
from DataStructure.Department import Department
from DataStructure.Professor import Professor
from DataStructure.Room import Room
from DataStructure.Timeslot import TimeSlot


class Data:
    def __init__(self):
        self.rooms = [
            Room("R120", 25),
            Room("RAA1", 45),
            Room("R8", 35),
            Room("R14", 50)
        ]
        self.timeslots = [
            TimeSlot("T1", "Monday_Wednesday_Friday 09:00 - 10:00"),
            TimeSlot("T2", "Monday_Wednesday_Friday 10:00 - 11:00"),
            TimeSlot("T3", "Tuesday_Thursday 09:00 - 10:30"),
            TimeSlot("T4", "Tuesday_Thursday 10:30 - 12:00"),
            TimeSlot("T5", "Monday_Wednesday_Friday 11:00 - 12:00"),
            TimeSlot("T6", "Tuesday_Thursday 12:00 - 13:30")
        ]
        self.professors = [
            Professor("P1", "Prof. Maria Batrakova"),
            Professor("P2", "Prof. Diogo Pires"),
            Professor("P3", "Prof. Manuel Gonçalves"),
            Professor("P4", "Prof. Majd Al Ajlani")
        ]
        self.courses = [
            Course("C1", "DS101", [self.professors[0], self.professors[1]], 25, ["T2", "T1"], ["R120"]),
            Course("C2", "DS102", [self.professors[0], self.professors[1], self.professors[3]], 35, ["T2", "T3"], ["R144"]),
            Course("C3", "ML201", [self.professors[2], self.professors[3]], 45, ["T3", "T4"], ["R7", "R144"]),
            Course("C4", "ML202", [self.professors[2], self.professors[3]], 30, ["T3", "T4", "T5"]),
            Course("C5", "AI301", [self.professors[0], self.professors[3]], 40),
            Course("C6", "BD401", [self.professors[1], self.professors[2]], 45, ["T1", "T6"], ["R7"]),
            Course("C7", "BD402", [self.professors[1], self.professors[2]], 45),
            Course("C8", "NLP101", [self.professors[2], self.professors[3]], 35, ["T3", "T5"], ["R100"]),
            Course("C9", "CV101", [self.professors[1], self.professors[2]], 35),
            Course("C10", "DS201", [self.professors[0], self.professors[1]], 35, ["T2", "T4", "T5"], ["R144"])
        ]
        self.departments = [
            Department("Data Science", [self.courses[0], self.courses[1], self.courses[9]]),
            Department("Machine Learning", [self.courses[2], self.courses[3]]),
            Department("Artificial Intelligence", [self.courses[4], self.courses[7], self.courses[8]]),
            Department("Big Data", [self.courses[5], self.courses[6]])
        ]

        self.number_of_classes = sum(len(department.get_courses()) for department in self.departments)

    def get_rooms(self): 
        return self.rooms
    
    def get_professors(self): 
        return self.professors
    
    def get_courses(self): 
        return self.courses
    
    def get_departments(self): 
        return self.departments
    
    def get_timeslots(self): 
        return self.timeslots
    
    def get_number_of_classes(self): 
        return self.number_of_classes
