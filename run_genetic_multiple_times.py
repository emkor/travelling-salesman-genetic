from algorithm.genetic import GeneticSalesman
from comparator.multiple_times_runner import MultipleTimesRunner

DATASET_100 = "./data/dataset_100_1.csv"
DATASET_1000 = "./data/dataset_1000_1.csv"

genetic = GeneticSalesman(population_size=100, max_generations=500, timeout=40,
                          dataset_filename=DATASET_100,
                          survival_ratio=0.3, mutation_probability=0.05)

runner = MultipleTimesRunner(genetic)
runner.run(10)
stats = runner.average_stats()
runner.show_stats(stats)
