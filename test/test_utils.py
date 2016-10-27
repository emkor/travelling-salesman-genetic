import unittest

from common.city import City
from common.utils import distance


class UtilsTest(unittest.TestCase):
    def test_distance_function(self):
        a = City(1, 9.0, 7.0)
        b = City(2, 3.0, 2.0)
        actual_distance = distance(a, b)
        self.assertAlmostEqual(7.81, actual_distance, places=2)

    def test_distance_function_on_negative(self):
        a = City(1, -3.0, 5.0)
        b = City(2, 7.0, -1.0)
        actual_distance = distance(a, b)
        self.assertAlmostEqual(11.66, actual_distance, places=2)
