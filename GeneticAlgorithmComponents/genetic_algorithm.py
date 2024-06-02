# genetic_algorithm.py
import random as rnd

from DataStructure.Population import Population
from Utils.constants import NUMBER_OF_ELITE_SCHEDULES, POPULATION_SIZE, CROSSOVER_RATE

class GeneticAlgorithm:
    """
    Class implementing a genetic algorithm for evolving schedules.
    
    Attributes:
        mutation_func (function): Function to mutate a schedule.
        crossover_func (function): Function to perform crossover between two schedules.
        selection_func (function): Function to select a schedule from the population.
    """
    def __init__(self, mutation_func, crossover_func, selection_func):
         """
        Initializes the genetic algorithm with the given mutation, crossover, and selection functions.
        
        Parameters:
            mutation_func (function): Function to mutate a schedule.
            crossover_func (function): Function to perform crossover between two schedules.
            selection_func (function): Function to select a schedule from the population.
        """
        self.mutation_func = mutation_func
        self.crossover_func = crossover_func
        self.selection_func = selection_func

    def evolve(self, population):
        """
        Evolves the given population by applying crossover and mutation.
        
        Parameters:
            population (Population): The population to evolve.
        
        Returns:
            Population: The evolved population.
        """
        return self.mutate_population(self.crossover_population(population))

    def mutate_population(self, population):
        """
        Mutates the non-elite schedules in the population.
        
        Parameters:
            population (Population): The population whose schedules are to be mutated.
        
        Returns:
            Population: The population with mutated schedules.
        """
        for i in range(NUMBER_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            population.get_schedules()[i] = self.mutation_func(population.get_schedules()[i])
        return population

    def crossover_population(self, population):
        """
        Applies crossover to the population to create a new population.
        
        Parameters:
            population (Population): The population whose schedules are to be crossed over.
        
        Returns:
            Population: The new population created by crossover.
        """
        crossover_pop = Population(0, population.get_schedules()[0].data)

        # Retain elite schedules
        for i in range(NUMBER_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(population.get_schedules()[i])

        # Apply crossover to the rest of the population
        for i in range(NUMBER_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            schedule1 = self.selection_func(population)
            schedule2 = self.selection_func(population)
            if rnd.random() < CROSSOVER_RATE:
                crossover_pop.get_schedules().append(self.crossover_func(schedule1, schedule2))
            else:
                crossover_pop.get_schedules().append(schedule1)
        return crossover_pop
