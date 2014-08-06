from __future__ import division
import math
import random
import heapq
from reservoir.sbc import ReservoirBase


class UniformSampler(ReservoirBase):
    """Uniform Sampling with a Reservoir

    P(accept; n, k) = k/n

    Attributes:
        reservoir (list): Reservoir of random samples.
        counter (int): Saves the total number of values seen (n)
        _max (int): the max number of samples allowed in memory (k)

    References:
        J.S. Vitter. Random sampling with a reservoir.
    """

    def accept(self):
        probability = self._max / self.counter
        return probability


class AbsoluteWeightSampler(ReservoirBase):
    """Weighted Sampling with a Reservoir of absolute weighting schemes. Note
    that for this algorithm, reservoir is implimented as a heap.

    Example:
        Assume that we want to select a weighted random sample of size
        m = 2 from a population of 4 items with weights 1, 1, 1 and 2,
        respectively. The probability of items 1, 2 and 3 to be in the
        random sample is 0.4 while the probability of item 4 is 0.8.

    Attributes:
        reservoir (list): Reservoir of random samples.
        counter (int): Saves the total number of values seen (n)
        _max (int): the max number of samples allowed in memory (k)

    References:
        Pavlos S. Efraimidis. Weighted Random Sampling over Data Streams

    """
    def __init__(self, size=10):
        self.reservoir = heapq.heapify([]*size)
        self.counter = int(0)
        self._max = size

    def append(self, pair):
        """Accepts new element into the reservoir

        Arguments:
            element (any): new element that may go into the reservoir

        """
        weight, element = pair
        key = random.random()**(1 / weight)
        self.reservoir.heapreplace((key, element))
        self.counter += 1


class ExponentialSampler(ReservoirBase):
    """Exponential Sampling with a Reservoir

    P(accept; n, k) = k(1 - exp(-1 / B))

    Attributes:
        decay (float): decay constant, the larger it is, the more uniform
        reservoir (list): reservoir of random samples
        counter (int): saves the total number of values seen (n)
        _max (int): the max number of samples allowed in memory (k)

    References:
        "Exponential Reservoir Sampling for Streaming Language Models"
        http://personal.denison.edu/~lalla/acl2014.pdf
    """
    def __init__(self, decay=1.1, size=10):
        ReservoirBase.__init__(self, size=size)
        self.decay = decay

    def accept(self):
        probability = self._max * (1 - math.exp(-1 / self.decay))
        return probability
