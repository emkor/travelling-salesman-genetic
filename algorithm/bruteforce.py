import itertools

from datetime import datetime

from algorithm.abstract_algorithm import AbstractAlgorithm
from common.travel import Travel
from common.utils import log
from generator.storing import load_from_file


class Bruteforce(AbstractAlgorithm):
    def __init__(self, timeout, dataset_filename):
        self.timeout = timeout
        self.dataset_filename = dataset_filename
        self.iteration = 1
        self.stats = {}
        self.cities = {}
        self.start_time = None

    def run(self):
        log("Started run!")
        self.best_travel = None
        self.iteration = 1
        self.start_time = datetime.now()
        self.cities = load_from_file(self.dataset_filename)

        for travel_permutation in itertools.permutations(range(0, len(self.cities))):
            if self._seconds_since() > self.timeout:
                break
            else:
                travel = Travel(travel_permutation, self.cities)
                if self.best_travel:
                    if self.best_travel.length > travel.length:
                        self.best_travel = travel
                        time = self._seconds_since()
                        self.stats.update(
                            {self.iteration: {"min": travel.length, "avg": travel.length, "max": travel.length,
                                              "time": time}})
                        log("Found new best at {} iteration!".format(self.iteration))
                        log("Iteration {} stats: {}".format(self.iteration, self.stats.get(self.iteration)))
                        self.iteration += 1
                else:
                    self.best_travel = travel
        log("Ended run! Took {0:.1f} seconds.".format(self._seconds_since()))

    def _seconds_since(self):
        return (datetime.now() - self.start_time).total_seconds()

    def get_stats(self):
        return self.stats

    def __str__(self):
        return "BruteForce method"
