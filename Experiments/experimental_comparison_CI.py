import itertools
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem, t
from GeneticAlgorithmComponents.crossover import single_point_crossover, uniform_crossover
from GeneticAlgorithmComponents.mutation import binary_mutation, swap_mutation
from GeneticAlgorithmComponents.selection import tournament_selection, ranking_selection
from data import Data
from GeneticAlgorithmComponents.genetic_algorithm import GeneticAlgorithm, Population
from Utils.constants import POPULATION_SIZE, MAX_GENERATIONS

# Define method combinations
crossover_methods = [single_point_crossover, uniform_crossover]
mutation_methods = [binary_mutation, swap_mutation]
selection_methods = [tournament_selection, ranking_selection]

# Number of runs for each combination
NUM_RUNS = 30

def run_experiment(crossover_method, mutation_method, selection_method):
    data = Data()
    all_fitness_per_generation = np.zeros((NUM_RUNS, MAX_GENERATIONS))

    for run in range(NUM_RUNS):
        population = Population(POPULATION_SIZE, data)
        genetic_algorithm = GeneticAlgorithm(mutation_method, crossover_method, selection_method)
        fitness_per_generation = []

        for generation in range(MAX_GENERATIONS):
            population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
            best_fitness = population.get_schedules()[0].get_fitness()
            fitness_per_generation.append(best_fitness)

            population = genetic_algorithm.evolve(population)

        all_fitness_per_generation[run, :len(fitness_per_generation)] = fitness_per_generation

    return all_fitness_per_generation

def calculate_confidence_intervals(all_fitness_per_generation):
    means = np.mean(all_fitness_per_generation, axis=0)
    std_err = sem(all_fitness_per_generation, axis=0)
    confidence = std_err * t.ppf((1 + 0.95) / 2., NUM_RUNS - 1)  # 95% confidence interval
    return means, confidence

def plot_results(results):
    plt.figure(figsize=(12, 8))

    for label, all_fitness_per_generation in results.items():
        means, confidence = calculate_confidence_intervals(all_fitness_per_generation)
        generations = np.arange(MAX_GENERATIONS)
        plt.plot(generations, means, label=label)
        plt.fill_between(generations, means - confidence, means + confidence, alpha=0.2)

    plt.xlabel('Generations')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness per Generation w/ Confidence Intervals for Different Method Combinations')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    results = {}

    for crossover_method, mutation_method, selection_method in itertools.product(crossover_methods, mutation_methods, selection_methods):
        label = f"{crossover_method.__name__.split('_')[0]}_{mutation_method.__name__.split('_')[0]}_{selection_method.__name__.split('_')[0]}"
        print(f"Running experiment with {label}")
        all_fitness_per_generation = run_experiment(crossover_method, mutation_method, selection_method)
        results[label] = all_fitness_per_generation

    plot_results(results)

if __name__ == '__main__':
    main()
