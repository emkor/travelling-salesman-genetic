import unittest

from common.city import City
from generator.data_generator import generate_random_cities
from generator.storing import store_to_file, load_from_file


class StoringTest(unittest.TestCase):
    def test_should_store_and_read_back(self):
        a = City(1, 9.0, 7.0)
        b = City(2, 3.0, 2.0)
        c = City(2, 3.0, 2.0)
        input_cities = [a, b, c]
        test_filename = "storing_test.csv"
        # when
        store_to_file(test_filename, input_cities)
        loaded_cities = load_from_file(test_filename)
        # then
        self.assertEquals(input_cities, loaded_cities)

    def test_should_generate_100_cities(self):
        desired_length = 100
        random_cities = generate_random_cities(desired_length)
        self.assertEquals(desired_length, len(random_cities))
        self.assertNotEquals(random_cities[0], random_cities[1])
        self.assertNotEquals(random_cities[-1], random_cities[0])
        self.assertNotEquals(random_cities[41], random_cities[24])
