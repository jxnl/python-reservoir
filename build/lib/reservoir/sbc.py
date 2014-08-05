import random


class ReservoirBase(object):
    """Base class reference for Abstract Reservoir Algorithms

    Attributes:
        reservoir (list): reservoir of random samples.
        counter (int): saves the total number of values seen.
        _max (int): the max number of samples allowed in memory.
    """

    def __init__(self, size=10):
        self.reservoir = list()
        self.counter = int()
        self._max = size

    def accept(self):
        pass

    def feed(self, item):
        """Consumes a new item and decides weither or not to accept it"""
        if self.counter < self._max:
            self.reservoir.append(item)
        elif random.random() < self.accept():
            self.swap(item)
        self.counter += 1

    def swap(self, item):
        """Changes a random item from the reservoir with new item"""
        choose = random.randint(0, self._max-1)
        self.reservoir[choose] = item

    def sample(self, stream):
        """Samples data stream and feeds into

        Arguments:
            stream (iterable): stream from which to sample

        """
        for item in stream:
            self.feed(item)
        return self.reservoir

    def __repr__(self):
        return str(self.reservoir)
