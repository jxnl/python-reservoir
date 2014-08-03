# Reservoir

A lightweight module for generating samples from interable data structures.

>Random sampling is often applied to very large datasets
and in particular to data streams. In this case, the random sample has to be
generated in one pass over an initially unknown population. An elegant and
eﬃcient approach to generate random samples from data streams is the use
of a reservoir of size k, where k is sample size. The reservoir-based sampling
algorithms maintain the invariant that, at each step of the sampling process,
the contents of the reservoir are a valid random sample for the set of items
that have been processed up to that point. [--- Weighted Random Sampling over Data Streams](http://arxiv.org/pdf/1012.0256.pdf)

## Installation

    pip install Reservoir

# Usage

As a command line interface, just run the `-h` flag to see whats up.

    $ res-sample -h

    usage: r [-h] [-f FILE | -s] size

    Sample k elements from a stream or file

    positional arguments:
      size                  The number of elements you wish you sample

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE
      -s, --stream          For use with pipes and redirects

###  File and Streams

    # sample 10 lines from 'input.txt'
    $ res-sample -f input.txt 10

To use pipes and redirects use the `-s | --stream` flag.

    # sample 10 lines from my twitter api
    $ twitter_stream.py | res-sample  -s 10 > output.txt

### Module

As a module the `UniformSampler` interface is quite simple.

    from reservoir import UniformSampler
    sampler = UniformSampler(max_samples=2)

    # sampler.feed takes in an item at a time
    sampler.feed("github")
    sampler.feed(1)
    sampler.feed([1, 2, 3]) 

    sampler.saves
    >>> ["github", [1, 2, 3]]

    # sampler.stream_sample takes in an iterable and selects the k elements
    sampler.stream_sample(some_generator())
    sampler.stream_sample(dictionary.keys())
    sampler.stream_sample(xrange(1,10))
