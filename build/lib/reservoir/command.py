"""
    UniformSampler (Object): This module contains a UniformClass object with
        an `feed` method that takes in the ith element and `stream_sample` that
        processes any iterable and returns the sampled elements.

Author: Jason Liu
Date: May 24th, 2014

"""
from __future__ import print_function
import sys
from argparse import ArgumentParser
from reservoir.sampling import (UniformSampler, ExponentialSampler,
                                AbsoluteWeightSampler)


def gen_parser():
    """Generate the CLI argparse object"""

    desc = """Command line interface to sample large data sets using various
              reservoir sampling algorithms."""

    # Define size of reservoir
    parser = ArgumentParser(description=desc)
    parser.add_argument('-k', '--size', type=int,
                        help="Number of elements to sample",)

    # Parse either a file or from standard input as a stream
    file_or_stream = parser.add_mutually_exclusive_group()
    file_or_stream.add_argument('-f', '--file', type=str)
    file_or_stream.add_argument('-s', '--stream', action='store_true',
                                help='Consume values from stdin as a stream')

    # Sampler options include Uniform, Exponential, and Absolute Weights
    sampler = parser.add_mutually_exclusive_group()
    sampler.add_argument('-u', '--uniform', action='store_true',
                         help="""All elements have equal probability
                         of appearing in the reservoir""")

    sampler.add_argument('-e', '--decay', type=float,
                         help="""Apply an exponential bias to items near
                         the end of stream""")

    sampler.add_argument('-w', '--sep', type=str,
                         help="""Apply bias proportional to the weight
                         of the sample.""")
    return parser


def main():
    parser = gen_parser()
    args = parser.parse_args()

    if args.uniform:
        sampler = UniformSampler(size=args.size)

    if args.decay:
        sampler = ExponentialSampler(size=args.size, decay=args.decay)

    if args.sep:
        print(args.sep)
        sampler = AbsoluteWeightSampler(size=args.size, sep=args.sep)

    if args.file:
        with open(args.file) as res:
            sampler.sample(res)

    if args.stream:
        for line in sys.stdin:
            sampler.append(line.strip())
        print(sampler)

    for item in sampler:
        print(item)

if __name__ == "__main__":
    sys.exit(main())
