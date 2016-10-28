from algorithm.bruteforce import Bruteforce

DATASET_100 = "./data/dataset_100_1.csv"
DATASET_1000 = "./data/dataset_1000_1.csv"

bruteforce = Bruteforce(timeout=20, dataset_filename=DATASET_100)
bruteforce.run()