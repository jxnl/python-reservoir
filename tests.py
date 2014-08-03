"""
Emperical evidence for uniformity
"""

from reservoir import reservoir

DATA = xrange(1, 51)
counter = [0]*50

for _ in xrange(0):
    sampler = reservoir.UniformSampler(size=2)
    for sampled_item in sampler.stream_sample(DATA):
        index = sampled_item - 1
        counter[index] += 1
print counter
