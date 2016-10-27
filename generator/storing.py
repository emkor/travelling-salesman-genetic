import csv

from common.city import City


def load_from_file(filename):
    """
    :type filename: str
    :rtype: list[common.city.City]
    """
    cities = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
        for row in csv_reader:
            if row:
                cities.append(City(number=int(row[0]), x=float(row[1]), y=float(row[2])))
    return cities


def store_to_file(filename, cities_list):
    """
    :type filename: str
    :type cities_list: list[common.city.City]
    """
    with open(filename, 'wb') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for city in cities_list:
            csv_writer.writerow([city.number, city.x, city.y])
