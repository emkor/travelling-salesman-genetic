from algorithm.bruteforce import Bruteforce
from algorithm.genetic import GeneticSalesman
from comparator.time_comparator import TimeComparator

DATASET_100 = "./data/dataset_100_1.csv"
DATASET_1000 = "./data/dataset_1000_1.csv"
TIMEOUT = 20

genetic1 = GeneticSalesman(population_size=25, max_generations=1000000, timeout=TIMEOUT,
                           dataset_filename=DATASET_100,
                           survival_ratio=0.3, mutation_probability=0.1)

genetic2 = GeneticSalesman(population_size=50, max_generations=1000000, timeout=TIMEOUT,
                           dataset_filename=DATASET_100,
                           survival_ratio=0.3, mutation_probability=0.1)

genetic3 = GeneticSalesman(population_size=100, max_generations=100000, timeout=TIMEOUT,
                           dataset_filename=DATASET_100,
                           survival_ratio=0.3, mutation_probability=0.1)

genetic4 = GeneticSalesman(population_size=200, max_generations=100000, timeout=TIMEOUT,
                           dataset_filename=DATASET_100,
                           survival_ratio=0.3, mutation_probability=0.1)

genetic5 = GeneticSalesman(population_size=400, max_generations=100000, timeout=TIMEOUT,
                           dataset_filename=DATASET_100,
                           survival_ratio=0.3, mutation_probability=0.1)

bruteforce = Bruteforce(timeout=TIMEOUT, dataset_filename=DATASET_100)

comparator = TimeComparator([genetic1, genetic2, genetic3, genetic4, genetic5, bruteforce])

comparator.run()
comparator.show_stats()
