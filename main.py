# main.py
from DataStructure.Population import Population
from GeneticAlgorithmComponents.crossover import single_point_crossover, cycle_crossover, uniform_crossover
from GeneticAlgorithmComponents.mutation import swap_mutation, binary_mutation
from GeneticAlgorithmComponents.selection import tournament_selection, ranking_selection
from data import Data
from GeneticAlgorithmComponents.genetic_algorithm import GeneticAlgorithm
from Utils.display import DisplaySchedule
from Utils.constants import POPULATION_SIZE, MAX_GENERATIONS
import itertools

# Define method combinations
crossover_methods = [single_point_crossover, cycle_crossover, uniform_crossover]
mutation_methods = [binary_mutation, swap_mutation]
selection_methods = [tournament_selection, ranking_selection]

# Store results
results = []
best_schedule = None
best_schedule_details = None

# Run experiments
for crossover_method, mutation_method, selection_method in itertools.product(crossover_methods, mutation_methods, selection_methods):
    data = Data()
    display_schedule = DisplaySchedule(data)

    print(f"\nRunning experiment with {crossover_method.__name__}, {mutation_method.__name__}, {selection_method.__name__}")

    generation_number = 0
    population = Population(POPULATION_SIZE, data)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)

    geneticAlgorithm = GeneticAlgorithm(mutation_method, crossover_method, selection_method)

    while population.get_schedules()[0].get_fitness() != 0 and generation_number < MAX_GENERATIONS:
        generation_number += 1
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)

    best_fitness = population.get_schedules()[0].get_fitness()
    results.append((crossover_method.__name__, mutation_method.__name__, selection_method.__name__, best_fitness, generation_number))

    if best_schedule is None or best_fitness > best_schedule.get_fitness():
        best_schedule = population.get_schedules()[0]
        best_schedule_details = (crossover_method.__name__, mutation_method.__name__, selection_method.__name__)

    if best_fitness == 0:
        print("\nOptimal solution found!")
    else:
        print("\nReached maximum generations without finding an optimal solution.")

# Print results
print("\n\nExperimental Results:")
print(f"{'Crossover':<25} {'Mutation':<25} {'Selection':<25} {'Best Fitness':<15} {'Generations':<15}")
for result in results:
    print(f"{result[0]:<25} {result[1]:<25} {result[2]:<25} {result[3]:<15} {result[4]:<15}")

# Print the best schedule and the methods used
if best_schedule is not None:
    print("\nBest Schedule Details:")
    print(f"Methods Used: Crossover: {best_schedule_details[0]}, Mutation: {best_schedule_details[1]}, Selection: {best_schedule_details[2]}")
    display_schedule.print_schedule_as_table(best_schedule)
else:
    print("No valid schedule found.")

"""""""""
The algorithm continues to evolve the population until it finds a schedule with a fitness of 0.
 
This means that the algorithm will keep running indefinitely until it reaches an optimal solution 
(a schedule with no conflicts).

To provide more control over the number of generations the algorithm runs, we  introduce a maximum 
number of generations. 

This will prevent the algorithm from running indefinitely and allows to specify how many generations
you want it to run before stopping.
"""""""""
