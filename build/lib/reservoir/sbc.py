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
        self.counter = int(0)
        self._max = size

    def accept(self):
        pass

    def append(self, element):
        """Accepts a new element into the reservoir

        Arguments:
            element (any): new element that may go into the reservoir
        """
        if self.counter < self._max:
            self.reservoir.append(element)
        elif random.random() < self.accept():
            self.swap(element)
        self.counter += 1

    def swap(self, new_element):
        """Changes a random element from the reservoir with a new element

        Arguments:
            new_element (any): a new element that much go into the reservoir
        """
        choose = random.randint(0, self._max-1)
        self.reservoir[choose] = new_element

    def sample(self, stream):
        """Samples data stream and feeds into

        Arguments:
            stream (iterable): stream from which to sample
        """
        for element in stream:
            self.append(element)
        return self.reservoir

    def __iter__(self):
        for element in self.reservoir:
            yield element

    def __repr__(self):
        return str(self.reservoir)
