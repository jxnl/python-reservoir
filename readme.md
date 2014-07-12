# Reservoir

A lightweight module for to generate a sample of elements any interable data structure
or stream using the Reservoir Sampling algorithm.

## Installation

Just clone this repo and use the script provided! I'll consider adding this to the Python 
Package Index once I've figured out weighted sampling.

# Usage

As a command line interface, just run the `-h` flag to see whats up.

    $ python reservoir -h

    usage: reservoir.py [-h] [-f FILE | -s] size

    Sample k elements from a stream or file

    positional arguments:
      size                  The number of elements you wish you sample

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE
      -s, --stream          For use with pipes and redirects

###  File and Streams

Currently only supports reading a file, to output you'll need to do a redirect.

    # sample 10 lines from input.txt
    $ python reservoir.py -f input.txt 10 > output.txt

To use pipes and redirects use the `-s | --stream` flag.
    
    # sample 10 lines from my twitter api
    $ twitterstream | python reservoir.py -s 10 > output.txt

### Module

As a module the Class `UniformSampler` is quite simple.

    from reservoir import UniformSampler
    sampler = UniformSampler(max_samples=2)

The only methods available are `accept` or `consume`.
    
    # sampler.accept takes in an item at a time
    sampler.accept("github")
    sampler.accept(1)
    sampler.accept([1, 2, 3]) 

    sampler.saves
    >>> ["github", [1, 2, 3]]

    # sampler.consume takes in an iterable and selects the k elements
    sampler.accept(some_generator())
    sampler.accept(dictionary.keys())
    sampler.accept(xrange(1,10))
