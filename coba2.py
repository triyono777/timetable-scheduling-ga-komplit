# experimental_comparison.py
import itertools
import matplotlib.pyplot as plt
import numpy as np
import logging
import time
import csv

from GeneticAlgorithmComponents.crossover import cycle_crossover, single_point_crossover, uniform_crossover
from GeneticAlgorithmComponents.mutation import binary_mutation, swap_mutation
from GeneticAlgorithmComponents.selection import tournament_selection, ranking_selection,truncation_selection
from data import Data
from GeneticAlgorithmComponents.genetic_algorithm import GeneticAlgorithm, Population
from Utils.constants import POPULATION_SIZE, MAX_GENERATIONS

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define method combinations
# crossover_methods = [single_point_crossover, cycle_crossover, uniform_crossover]
crossover_methods = [ single_point_crossover]
# mutation_methods = [binary_mutation, swap_mutation]
mutation_methods = [swap_mutation]
# selection_methods = [tournament_selection, ranking_selection,truncation_selection]
selection_methods = [tournament_selection]

# Number of runs for each combination
NUM_RUNS = 30

def run_experiment(crossover_method, mutation_method, selection_method):
    data = Data()
    avg_fitness_per_generation = np.zeros(MAX_GENERATIONS)
    total_runtime = 0

    for run in range(NUM_RUNS):
        start_time = time.time()
        population = Population(POPULATION_SIZE, data)
        genetic_algorithm = GeneticAlgorithm(mutation_method, crossover_method, selection_method)
        fitness_per_generation = []

        for generation in range(MAX_GENERATIONS):
            population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
            best_fitness = population.get_schedules()[0].get_fitness()
            fitness_per_generation.append(best_fitness)

            population = genetic_algorithm.evolve(population)

        end_time = time.time()
        total_runtime += (end_time - start_time)
        avg_fitness_per_generation[:len(fitness_per_generation)] += fitness_per_generation

    avg_fitness_per_generation /= NUM_RUNS
    avg_runtime = total_runtime / NUM_RUNS
    return avg_fitness_per_generation, avg_runtime

def plot_results(results):
    plt.figure(figsize=(12, 8))

    for label, (avg_fitness, _) in results.items():
        plt.plot(avg_fitness, label=label)

    plt.xlabel('Generations')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness per Generation for Different Method Combinations')
    plt.legend()
    plt.grid(True)
    plt.savefig("hasil_gambar/"+label)
    # plt.show()

def save_results(results, filename='experiment_results.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Method Combination', 'Average Runtime', 'Average Fitness per Generation'])

        for label, (avg_fitness, avg_runtime) in results.items():
            writer.writerow([label, avg_runtime, *avg_fitness])

def main():
    results = {}

    for crossover_method, mutation_method, selection_method in itertools.product(crossover_methods, mutation_methods, selection_methods):
        label = f"{crossover_method.__name__.split('_')[0]}_{mutation_method.__name__.split('_')[0]}_{selection_method.__name__.split('_')[0]}"
        logging.info(f"Running experiment with {label}")
        avg_fitness_per_generation, avg_runtime = run_experiment(crossover_method, mutation_method, selection_method)
        results[label] = (avg_fitness_per_generation, avg_runtime)
        logging.info(f"Completed experiment with {label} in {avg_runtime:.2f} seconds")

    plot_results(results)
    save_results(results,filename="hasil/"+label+" experiment_results.csv")

if __name__ == '__main__':
    main()
