from algorithm.bruteforce import Bruteforce
from algorithm.genetic import GeneticSalesman
from comparator.time_comparator import TimeComparator

DATASET_100 = "./data/dataset_100_1.csv"
DATASET_1000 = "./data/dataset_1000_1.csv"
TIMEOUT = 10

genetic1 = GeneticSalesman(population_size=100, max_generations=100000, timeout=TIMEOUT,
                           dataset_filename=DATASET_100,
                           survival_ratio=0.1, mutation_probability=0.05)

genetic2 = GeneticSalesman(population_size=100, max_generations=100000, timeout=TIMEOUT,
                           dataset_filename=DATASET_100,
                           survival_ratio=0.3, mutation_probability=0.05)

genetic3 = GeneticSalesman(population_size=100, max_generations=10000, timeout=TIMEOUT,
                           dataset_filename=DATASET_100,
                           survival_ratio=0.5, mutation_probability=0.05)

genetic4 = GeneticSalesman(population_size=100, max_generations=10000, timeout=TIMEOUT,
                           dataset_filename=DATASET_100,
                           survival_ratio=0.7, mutation_probability=0.05)

genetic5 = GeneticSalesman(population_size=100, max_generations=10000, timeout=TIMEOUT,
                           dataset_filename=DATASET_100,
                           survival_ratio=0.9, mutation_probability=0.05)

bruteforce = Bruteforce(timeout=10, dataset_filename=DATASET_100)

comparator = TimeComparator([genetic1, genetic2, genetic3, genetic4, genetic5, bruteforce])

comparator.run()
comparator.show_stats()
