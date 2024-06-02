from DataStructure.Schedule import Schedule
import random as rnd

def single_point_crossover(schedule1, schedule2):
    """
    Performs single-point crossover on two schedules.
    
    Parameters:
        schedule1 (Schedule): The first parent schedule.
        schedule2 (Schedule): The second parent schedule.
    
    Returns:
        Schedule: A new schedule created by crossing over the two parent schedules.
    """
    data = schedule1.data
    crossover_schedule = Schedule(data).initialize()
    parent1_classes = schedule1.get_classes()
    parent2_classes = schedule2.get_classes()

    crossover_point = rnd.randint(0, len(schedule1.get_classes()))

    for cls_id in range(len(parent1_classes)):
        if cls_id < crossover_point:
            crossover_schedule.get_classes()[cls_id].set_room(parent2_classes[cls_id].get_room())
            crossover_schedule.get_classes()[cls_id].set_timeslot(parent2_classes[cls_id].get_timeslot())
            crossover_schedule.get_classes()[cls_id].set_professor(parent2_classes[cls_id].get_professor())
        else:
            crossover_schedule.get_classes()[cls_id].set_room(parent1_classes[cls_id].get_room())
            crossover_schedule.get_classes()[cls_id].set_timeslot(parent1_classes[cls_id].get_timeslot())
            crossover_schedule.get_classes()[cls_id].set_professor(parent1_classes[cls_id].get_professor())

    return crossover_schedule


def cycle_crossover(schedule1, schedule2):
    """
    Performs cycle crossover on two schedules.
    
    Parameters:
        schedule1 (Schedule): The first parent schedule.
        schedule2 (Schedule): The second parent schedule.
    
    Returns:
        Schedule: A new schedule created by crossing over the two parent schedules using cycles.
    """
    data = schedule1.data
    crossover_schedule = Schedule(data).initialize()
    parent1_classes = schedule1.get_classes()
    parent2_classes = schedule2.get_classes()
    size = len(parent1_classes)

    child_classes = [None] * size

    visited = [False] * size
    cycle_num = 0

    while None in child_classes:

        index = visited.index(False)

        cycle_indices = []
        while True:
            cycle_indices.append(index)
            visited[index] = True

            next_class_id = parent2_classes[index].get_id() if cycle_num % 2 == 0 else parent1_classes[index].get_id()
            index = next(i for i, cls in enumerate(parent1_classes if cycle_num % 2 == 0 else parent2_classes) if
                         cls.get_id() == next_class_id)

            if index in cycle_indices:
                break

        for i in cycle_indices:
            if cycle_num % 2 == 0:
                child_classes[i] = parent1_classes[i]
                crossover_schedule.get_classes()[i].set_room(parent1_classes[i].get_room())
                crossover_schedule.get_classes()[i].set_timeslot(parent1_classes[i].get_timeslot())
                crossover_schedule.get_classes()[i].set_professor(parent1_classes[i].get_professor())
            else:
                child_classes[i] = parent2_classes[i]
                crossover_schedule.get_classes()[i].set_room(parent2_classes[i].get_room())
                crossover_schedule.get_classes()[i].set_timeslot(parent2_classes[i].get_timeslot())
                crossover_schedule.get_classes()[i].set_professor(parent2_classes[i].get_professor())

        cycle_num += 1

    return crossover_schedule


def uniform_crossover(schedule1, schedule2):
     """
    Performs uniform crossover on two schedules.
    
    Parameters:
        schedule1 (Schedule): The first parent schedule.
        schedule2 (Schedule): The second parent schedule.
    
    Returns:
        Schedule: A new schedule created by randomly selecting class details from either parent.
    """
    data = schedule1.data
    crossover_schedule = Schedule(data).initialize()
    parent1_classes = schedule1.get_classes()
    parent2_classes = schedule2.get_classes()

    for cls_id in range(len(parent1_classes)):
        if rnd.random() < 0.5:
            crossover_schedule.get_classes()[cls_id].set_room(parent1_classes[cls_id].get_room())
            crossover_schedule.get_classes()[cls_id].set_timeslot(parent1_classes[cls_id].get_timeslot())
            crossover_schedule.get_classes()[cls_id].set_professor(parent1_classes[cls_id].get_professor())
        else:
            crossover_schedule.get_classes()[cls_id].set_room(parent2_classes[cls_id].get_room())
            crossover_schedule.get_classes()[cls_id].set_timeslot(parent2_classes[cls_id].get_timeslot())
            crossover_schedule.get_classes()[cls_id].set_professor(parent2_classes[cls_id].get_professor())

    return crossover_schedule
