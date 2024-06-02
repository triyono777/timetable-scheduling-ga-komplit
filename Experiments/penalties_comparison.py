import itertools
import matplotlib.pyplot as plt
import numpy as np
from data import Data
from GeneticAlgorithmComponents.genetic_algorithm import GeneticAlgorithm, Population
from GeneticAlgorithmComponents.mutation import binary_mutation, swap_mutation
from GeneticAlgorithmComponents.selection import tournament_selection, ranking_selection
from GeneticAlgorithmComponents.crossover import single_point_crossover, uniform_crossover
from Utils.constants import *

# Different method combinations
crossover_methods = [single_point_crossover, uniform_crossover]
mutation_methods = [binary_mutation, swap_mutation]
selection_methods = [tournament_selection, ranking_selection]

# Number of runs for each combination
NUM_RUNS = 30

# Penalty values to test
hard_constraint_penalties = [1, 5, 10, 20, 50]
soft_constraint_penalties = [0.01, 0.05, 0.1, 0.2, 0.5]

def run_experiment_penalties(crossover_method, mutation_method, selection_method, hard_penalty, soft_penalty):
    data = Data()
    avg_fitness_per_generation = np.zeros(MAX_GENERATIONS)

    for run in range(NUM_RUNS):
        population = Population(POPULATION_SIZE, data)
        genetic_algorithm = GeneticAlgorithm(mutation_method, crossover_method, selection_method)

        # Update penalty values
        global HARD_CONSTRAINT_PENALTY
        global SOFT_CONSTRAINT_PENALTY
        HARD_CONSTRAINT_PENALTY = hard_penalty
        SOFT_CONSTRAINT_PENALTY = soft_penalty

        fitness_per_generation = []

        for generation in range(MAX_GENERATIONS):
            population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
            best_fitness = population.get_schedules()[0].get_fitness()
            fitness_per_generation.append(best_fitness)

            population = genetic_algorithm.evolve(population)

        avg_fitness_per_generation[:len(fitness_per_generation)] += fitness_per_generation

    avg_fitness_per_generation /= NUM_RUNS
    return avg_fitness_per_generation

def plot_results(all_results):
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))
    axs = axs.flatten()

    # Define a colormap from light to dark green
    colors = plt.cm.Greens(np.linspace(0.3, 1, len(hard_constraint_penalties) * len(soft_constraint_penalties)))

    for i, ((method_label, results), ax) in enumerate(zip(all_results.items(), axs)):
        # Sort the results by the combined penalty values to ensure proper color mapping
        sorted_results = sorted(results.items(), key=lambda x: (x[0][0], x[0][1]))

        for j, ((hard_penalty, soft_penalty), avg_fitness) in enumerate(sorted_results):
            ax.plot(avg_fitness, color=colors[j])

        ax.set_title(method_label)
        ax.set_xlabel('Generations')
        ax.grid(True)

    plt.suptitle('Average Fitness over Generations for Different Penalty Combinations and Methods')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def main():
    method_combinations = list(itertools.product(crossover_methods, mutation_methods, selection_methods))
    all_results = {}

    for crossover_method, mutation_method, selection_method in method_combinations:
        method_label = f"{crossover_method.__name__.split('_')[0]}_{mutation_method.__name__.split('_')[0]}_{selection_method.__name__.split('_')[0]}"
        print(f"Running experiments for method combination: {method_label}")
        results = {}

        for hard_penalty, soft_penalty in itertools.product(hard_constraint_penalties, soft_constraint_penalties):
            avg_fitness_per_generation = run_experiment_penalties(crossover_method, mutation_method, selection_method, hard_penalty, soft_penalty)
            results[(hard_penalty, soft_penalty)] = avg_fitness_per_generation

        all_results[method_label] = results

    plot_results(all_results)

if __name__ == '__main__':
    main()
