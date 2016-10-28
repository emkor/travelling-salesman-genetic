import random
from datetime import datetime
import matplotlib.pyplot as plt

from algorithm.abstract_algorithm import AbstractAlgorithm
from common.travel import generate_travel, Travel
from common.utils import log, random_ratio
from generator.storing import load_from_file


class GeneticSalesman(AbstractAlgorithm):
    def __init__(self, population_size, max_generations, timeout, dataset_filename, survival_ratio,
                 mutation_probability):
        """
        :type population_size: int
        :type max_generations: int
        :type timeout: int
        :type dataset_filename: str
        :type survival_ratio: float
        :type mutation_probability: float
        """
        self.mutation_probability = mutation_probability
        self.survival_ratio = survival_ratio
        self.dataset_filename = dataset_filename
        self.max_generations = max_generations
        self.timeout = timeout
        self.population_size = population_size
        self._init_variables()

    def run(self):
        log("Started run!")
        self._init_variables()
        self.initialize()
        self.evaluate()
        while self.generation <= self.max_generations and not self._is_timeout():
            self.selection()
            self.crossover()
            self.mutation()
            self.evaluate()
            log("Gen. {}. stats: {}".format(self.generation, self.stats.get(self.generation)))
            self.generation += 1
        log("Ended run! Took {0:.1f} seconds.".format((datetime.now() - self.start_time).total_seconds()))

    def get_stats(self):
        return self.stats

    def initialize(self):
        self.start_time = datetime.now()
        log("Initializing...")
        log("Loading cities from: {} ...".format(self.dataset_filename))
        self.cities = load_from_file(self.dataset_filename)
        log("Growing population...")
        while len(self.population) < self.population_size:
            new_travel = generate_travel(self.cities)
            self.population.append(new_travel)
        log("Ended initialization!")

    def evaluate(self):
        log("Evaluating {}. generation...".format(self.generation))
        population_to_evaluation = {travel: travel.length for travel in self.population}
        min_distance = min(population_to_evaluation.values())
        max_distance = max(population_to_evaluation.values())
        avg_distance = sum(population_to_evaluation.values()) / len(population_to_evaluation.values())
        time = (datetime.now() - self.start_time).total_seconds()
        self.stats.update(
            {self.generation: {"min": min_distance, "max": max_distance, "avg": avg_distance, "time": time}})
        log("Ended evaluation!")

    def selection(self):
        log("Started {}. gen. selection from {} of population...".format(self.generation, len(self.population)))
        travel_length_tuples_list = [(travel, travel.length) for travel in self.population]
        travel_length_tuples_list.sort(key=lambda tuple: tuple[1])
        sorted_population_length = float(len(travel_length_tuples_list))
        survivors_count = int(self.survival_ratio * sorted_population_length)
        log("Calculating survivors count: {} * {} = {}".format(self.survival_ratio, sorted_population_length,
                                                               survivors_count))
        self.population = [travel for travel, _ in travel_length_tuples_list[:survivors_count]]
        log("Ended selection, best {} elems survived!".format(len(self.population)))

    def crossover(self):
        log("Started {}. gen. crossover...".format(self.generation))
        while len(self.population) < self.population_size:
            new_elem = self._crossover_single_elem()
            self.population.append(new_elem)
        log("Ended crossover, population counts {} elements again!".format(len(self.population)))

    def mutation(self):
        log("Started {}. gen. mutation...".format(self.generation))
        counter = 0
        for travel in self.population:
            if random_ratio() <= self.mutation_probability:
                self._swap_random_points(travel)
                counter += 1
        log("Ended mutation! {} elements were mutated.".format(counter))

    def _init_variables(self):
        self.cities = []
        self.population = []
        self.generation = 1
        self.stats = {}
        self.start_time = None

    def _swap_random_points(self, travel):
        first_random_point = self._random_travel_point()
        second_random_point = self._random_travel_point()
        tmp = travel.city_numbers[first_random_point]
        travel.city_numbers[first_random_point] = travel.city_numbers[second_random_point]
        travel.city_numbers[second_random_point] = tmp

    def _crossover_single_elem(self):
        left_elem = self._get_random_population_elem()
        right_elem = self._get_random_population_elem()
        pivot = self._random_travel_point()
        new_city_numbers = left_elem.city_numbers[:pivot]
        for right_elem_city_number in right_elem.city_numbers:
            if right_elem_city_number not in new_city_numbers:
                new_city_numbers.append(right_elem_city_number)
        return Travel(new_city_numbers, self.cities)

    def _get_random_population_elem(self):
        """
        :rtype: common.travel.Travel
        """
        return self.population[random.randint(0, len(self.population) - 1)]

    def _random_travel_point(self):
        """
        :rtype: int
        """
        return random.randint(0, len(self.cities) - 1)

    def _is_timeout(self):
        """
        :rtype: bool
        """
        return (datetime.now() - self.start_time).total_seconds() > self.timeout

    def show_stats(self):
        generations = self.stats.keys()
        mins = [stats.get("min") for _, stats in self.stats.iteritems()]
        avgs = [stats.get("avg") for _, stats in self.stats.iteritems()]
        maxs = [stats.get("max") for _, stats in self.stats.iteritems()]
        plt.plot(generations, mins, 'r--', generations, avgs, 'b--', generations, maxs, 'g--')
        plt.xlabel("Generation")
        plt.ylabel("max / avg / min distance of population")
        plt.show()
