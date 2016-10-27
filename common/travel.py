import random

from common.utils import distance


def generate_travel(cities):
    """
    :type cities: list[common.city.City]
    """
    travel_order = range(0, len(cities))
    random.shuffle(travel_order)
    return Travel(travel_order, cities)


class Travel(object):
    def __init__(self, city_numbers, cities):
        """
        :type city_numbers: list[int]
        :type cities: list[common.city.City]
        """
        self.city_numbers = city_numbers
        self.length = self._calc_distance(cities)

    def _calc_distance(self, cities):
        """
        :type cities: list[]
        :rtype: float
        """
        if len(cities) > len(self.city_numbers):
            raise ValueError("Travel is shorter than all the cities available!")
        cities = map(lambda city_number: cities[city_number], self.city_numbers)
        total_distance = 0
        for i, city in enumerate(cities):
            if i < len(cities) - 1:
                total_distance += distance(city, cities[i + 1])
        return total_distance

    def __str__(self):
        return "Travel[{0};{1:.2f}km]".format(len(self.city_numbers), self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.city_numbers == other.city_numbers

    def __hash__(self):
        return hash(tuple(self.city_numbers))
