# data.py
from DataStructure.Course import Course
from DataStructure.Department import Department
from DataStructure.Professor import Professor
from DataStructure.Room import Room
from DataStructure.Timeslot import TimeSlot


class Data:
    def __init__(self):
        self.rooms = [
            Room("R1", 40),
            Room("R2", 40),
            Room("R3", 40),
            Room("R4", 40),
            Room("R5", 40),
            Room("R6", 40),
            Room("R7", 40),
            Room("R8", 40),
            Room("R9", 40),
            Room("R10", 40),
            Room("R11", 40),
            Room("R12", 40),
            Room("R13", 40),

        ]
        self.timeslots = [
                TimeSlot("T1", "Senin 08:00 - 10:30"),
                TimeSlot("T2", "Senin 10:30 - 13.00"),
                TimeSlot("T3", "Senin 13.30 - 16.00"),
                TimeSlot("T4", "Selasa 08:00 - 10:30"),
                TimeSlot("T5", "Selasa 10:30 - 13.00"),
                TimeSlot("T6", "Selasa 13.30 - 16.00"),
                TimeSlot("T7", "Rabu 08:00 - 10:30"),
                TimeSlot("T8", "Rabu 10:30 - 13.00"),
                TimeSlot("T9", "Rabu 13.30 - 16.00"),
                TimeSlot("T10", "Kamis 08:00 - 10:30"),
                TimeSlot("T11", "Kamis 10:30 - 13.00"),
                TimeSlot("T12", "Kamis 13.30 - 16.00"),
                TimeSlot("T13", "Jumat 08:00 - 10:30"),
                TimeSlot("T14", "Jumat 13.30 - 16.00"),


        ]
        self.professors = [
            Professor("P1", "Dwi Hartanti"),
            Professor("P2", "Nurchim"),
            Professor("P3", "Joni Maulindar"),
            Professor("P4", "Nibras")
        ]
        self.courses = [
            Course("C1", "DS101", [self.professors[0], self.professors[1]], 40, ["T2", "T1"], ["R12"]),
            Course("C2", "DS102", [self.professors[0], self.professors[1], self.professors[3]], 40, ["T2", "T3"], ["R13"]),
            Course("C3", "ML201", [self.professors[2], self.professors[3]], 40, ["T3", "T4"], ["R7", "R13"]),
            Course("C4", "ML202", [self.professors[2], self.professors[3]], 40, ["T3", "T4", "T5"]),
            Course("C5", "AI301", [self.professors[0], self.professors[3]], 40),
            Course("C6", "BD401", [self.professors[1], self.professors[2]], 40, ["T1", "T6"], ["R7"]),
            Course("C7", "BD402", [self.professors[1], self.professors[2]], 40),
            Course("C8", "NLP101", [self.professors[2], self.professors[3]], 40, ["T3", "T5"], ["R10"]),
            Course("C9", "CV101", [self.professors[1], self.professors[2]], 40),
            Course("C10", "DS201", [self.professors[0], self.professors[1]], 40, ["T2", "T4", "T5"], ["R13"])
        ]
        self.departments = [
            Department("Data Science", [self.courses[0], self.courses[1], self.courses[9]]),
            Department("Sistem Enterprise", [self.courses[2], self.courses[3]]),
            Department("IoT", [self.courses[4], self.courses[7], self.courses[8]]),
            Department("Sistem Cerdas", [self.courses[5], self.courses[6]])
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
