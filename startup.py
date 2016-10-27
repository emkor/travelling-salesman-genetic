from algorithm.genetic import GeneticSalesman

DATASET_100 = "./data/dataset_100_1.csv"
DATASET_1000 = "./data/dataset_1000_1.csv"

genetic = GeneticSalesman(population_size=100, max_generations=100, timeout=20,
                          dataset_filename=DATASET_100,
                          survival_ratio=0.4, mutation_probability=0.05)
genetic.run()
genetic.show_stats()
