import random as rnd

from Utils.constants import MUTATION_RATE


def binary_mutation(schedule):
    """
    Performs binary mutation on a schedule by randomly changing the timeslot, room, and professor of each class.
    
    Parameters:
        schedule (Schedule): The schedule to mutate.
    
    Returns:
        Schedule: The mutated schedule.
    """
    data = schedule.data
    for cls in schedule.get_classes():
        if rnd.random() < MUTATION_RATE:
            cls.set_timeslot(data.get_timeslots()[rnd.randrange(len(data.get_timeslots()))])
            cls.set_room(data.get_rooms()[rnd.randrange(len(data.get_rooms()))])
            cls.set_professor(cls.get_course().get_professors()[rnd.randrange(len(cls.get_course().get_professors()))])
    return schedule

def swap_mutation(schedule):
    """
    Performs swap mutation on a schedule by randomly swapping the rooms of two classes.
    
    Parameters:
        schedule (Schedule): The schedule to mutate.
    
    Returns:
        Schedule: The mutated schedule.
    """
    classes_tmp = schedule.get_classes()
    i = rnd.randrange(len(classes_tmp))
    j = rnd.randrange(len(classes_tmp))
    if i != j and rnd.random() < MUTATION_RATE:
        schedule.get_classes()[i].set_room(schedule.get_classes()[j].get_room())
        schedule.get_classes()[j].set_room(classes_tmp[i].get_room())
    return schedule
