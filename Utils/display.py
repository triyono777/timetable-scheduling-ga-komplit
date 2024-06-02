# display.py
import prettytable as pt
from data import Data

class DisplaySchedule:
    def __init__(self, data):
        self.data = data

    def print_available_data(self):
        print("All Available Data")
        self.print_department()
        self.print_course()
        self.print_room()
        self.print_professor()
        self.print_timeslot()

    def print_department(self):
        departments_table = pt.PrettyTable(['Department', 'Courses'])
        for department in self.data.get_departments():
            courses = ', '.join([course.get_name() for course in department.get_courses()])
            departments_table.add_row([department.get_name(), courses])
        print(departments_table)

    def print_course(self):
        courses_table = pt.PrettyTable(['Course Number', 'Course Name', 'Max Students', 'Professors'])
        for course in self.data.get_courses():
            professors = ', '.join([professor.get_name() for professor in course.get_professors()])
            courses_table.add_row([course.get_number(), course.get_name(), course.get_max_number_of_students(), professors])
        print(courses_table)

    def print_professor(self):
        professors_table = pt.PrettyTable(['professor ID', 'professor Name'])
        for professor in self.data.get_professors():
            professors_table.add_row([professor.get_id(), professor.get_name()])
        print(professors_table)

    def print_room(self):
        rooms_table = pt.PrettyTable(['Room Number', 'Seating Capacity'])
        for room in self.data.get_rooms():
            rooms_table.add_row([room.get_number(), room.get_seating()])
        print(rooms_table)

    def print_timeslot(self):
        timeslot_table = pt.PrettyTable(['TimeSlot ID', 'TimeSlot'])
        for timeslot in self.data.get_timeslots():
            timeslot_table.add_row([timeslot.get_id(), timeslot.get_time()])
        print(timeslot_table)

    def print_generation(self, population):
        generation_table = pt.PrettyTable(['Schedule #', 'Fitness', '# of Conflicts'])
        schedules = population.get_schedules()
        for i, schedule in enumerate(schedules):
            generation_table.add_row([i, round(schedule.get_fitness(), 3), schedule.get_numbOfConflicts()])
        print(generation_table)

    def print_schedule_as_table(self, schedule):
        classes_table = pt.PrettyTable(['Class #', 'Department', 'Course', 'Room', 'Professor', 'TimeSlot'])
        for cls in schedule.get_classes():
            classes_table.add_row([cls.get_id(), cls.get_department().get_name(), cls.get_course().get_name(),
                                   cls.get_room().get_number(), cls.get_professor().get_name(), cls.get_timeslot().get_time()])
        print(classes_table)
