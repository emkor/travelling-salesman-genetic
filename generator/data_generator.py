import random

from common.city import City
from generator.storing import store_to_file


def generate_random_cities(count=100):
    """
    :type count: int
    :rtype: list[]
    """
    cities = []
    for number in xrange(0, count):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        cities.append(City(number, x, y))
    return cities
