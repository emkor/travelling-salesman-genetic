class City(object):
    def __init__(self, number, x, y):
        """
        :type number: int
        :type x: float
        :type y: float
        """
        self.number = number
        self.x = x
        self.y = y

    def __str__(self):
        return "City #{0} [{1:.2f}; {2:.2f}]".format(self.number, self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.number == other.number

    def __hash__(self):
        return hash(self.number)
