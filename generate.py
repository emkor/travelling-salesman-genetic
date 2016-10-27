from generator.data_generator import generate_random_cities
from generator.storing import store_to_file

random_cities = generate_random_cities(1000)
store_to_file("./data/dataset_1000_1.csv", random_cities)
