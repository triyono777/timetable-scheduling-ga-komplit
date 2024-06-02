# genetic_algorithm.py
import random as rnd

from DataStructure.Population import Population
from Utils.constants import NUMBER_OF_ELITE_SCHEDULES, POPULATION_SIZE, CROSSOVER_RATE

class GeneticAlgorithm:
    def __init__(self, mutation_func, crossover_func, selection_func):
        self.mutation_func = mutation_func
        self.crossover_func = crossover_func
        self.selection_func = selection_func

    def evolve(self, population):
        return self.mutate_population(self.crossover_population(population))

    def mutate_population(self, population):
        for i in range(NUMBER_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            population.get_schedules()[i] = self.mutation_func(population.get_schedules()[i])
        return population

    def crossover_population(self, population):
        crossover_pop = Population(0, population.get_schedules()[0].data)
        for i in range(NUMBER_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(population.get_schedules()[i])
        for i in range(NUMBER_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            schedule1 = self.selection_func(population)
            schedule2 = self.selection_func(population)
            if rnd.random() < CROSSOVER_RATE:
                crossover_pop.get_schedules().append(self.crossover_func(schedule1, schedule2))
            else:
                crossover_pop.get_schedules().append(schedule1)
        return crossover_pop
