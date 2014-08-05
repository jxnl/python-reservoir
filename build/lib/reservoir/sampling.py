from __future__ import division
from reservoir.sbc import ReservoirBase
from math import exp


class UniformSampler(ReservoirBase):
    """Uniform Sampling with a Reservoir

    P(accept; n, k) = k/n

    Attributes:
        reservoir (list): Reservoir of random samples.
        counter (int): Saves the total number of values seen (n)
        _max (int): the max number of samples allowed in memory (k)
    """

    def accept(self):
        probability = self._max / self.counter
        return probability


class ExponentialSampler(ReservoirBase):
    """Exponential Sampling with a Reservoir

    P(accept; n, k) = k(1 - exp(-1 / B))

    Attributes:
        decay (float): decay constant used in `k(1 - exp(-1/B))`
        reservoir (list): Reservoir of random samples
        counter (int): saves the total number of values seen (n)
        _max (int): the max number of samples allowed in memory (k)

    References:
        "Exponential Reservoir Sampling for Streaming Language Models"
        http://personal.denison.edu/~lalla/acl2014.pdf
    """
    def __init__(self, decay=1.1, size=10):
        super().__init__(size=size)
        self.decay = decay

    def accept(self):
        probability = self._max * (1 - exp(-1 / self.decay))
        return probability
