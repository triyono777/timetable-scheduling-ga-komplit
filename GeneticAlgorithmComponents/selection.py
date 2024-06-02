import random as rnd
from DataStructure.Population import Population
from Utils.constants import TOURNAMENT_SELECTION_SIZE, POPULATION_SIZE

def tournament_selection(population):
    """
    Selects a schedule from the population using tournament selection.
    
    Parameters:
        population (Population): The population from which to select a schedule.
    
    Returns:
        Schedule: The schedule with the highest fitness from the tournament selection.
    """
    tournament_pop = Population(0, population.get_schedules()[0].data)
    for _ in range(TOURNAMENT_SELECTION_SIZE):
        tournament_pop.get_schedules().append(population.get_schedules()[rnd.randrange(POPULATION_SIZE)])
    tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    return tournament_pop.get_schedules()[0]

def ranking_selection(population):
    """
    Selects a schedule from the population using ranking selection.
    
    Parameters:
        population (Population): The population from which to select a schedule.
    
    Returns:
        Schedule: The selected schedule based on ranking selection.
    """
    ranked_schedules = sorted(population.get_schedules(), key=lambda x: x.get_fitness(), reverse=True)
    rank_sum = sum(range(1, POPULATION_SIZE + 1))
    pick = rnd.uniform(0, rank_sum)
    current = 0

    # Select a schedule based on the random pick
    for i, schedule in enumerate(ranked_schedules):
        current += (POPULATION_SIZE - i)
        if current > pick:
            return schedule
