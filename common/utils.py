import math

from datetime import datetime


def distance(city_a, city_b):
    """
    :type city_a: common.city.City
    :type city_b: common.city.City
    :rtype: float
    """
    x_distance = math.fabs(city_a.x - city_b.x)
    y_distance = math.fabs(city_a.y - city_b.y)
    return math.sqrt(math.pow(x_distance, 2) + math.pow(y_distance, 2))


def log(message):
    print("{} | {}".format(datetime.now(), str(message)))
