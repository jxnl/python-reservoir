"""
    UniformSampler (Object): This module contains a UniformClass object with
        an `feed` method that takes in the ith element and `stream_sample` that
        processes any iterable and returns the sampled elements.

Author: Jason Liu
Date: May 24th, 2014

"""
from __future__ import print_function
from argparse import ArgumentParser
from reservoir.sampling import UniformSampler, ExponentialSampler
import sys


def gen_parser():
    """Generate the CLI argparse object"""

    desc = """Random sampling is often applied to very large datasets and
              in particular to data streams. In this case, the random sample
              has to be generated in one pass over unknown population.
              """
    parser = ArgumentParser(description=desc)
    parser.add_argument('-n', type=int,
                        help="Number of elements to sample",)

    file_or_stream = parser.add_mutually_exclusive_group()
    file_or_stream.add_argument('-f', '--file', default=True, type=str)
    file_or_stream.add_argument('-s', '--stream', default=False,
                                action='store_true',
                                help='take from stdin')

    sampler = parser.add_mutually_exclusive_group()
    sampler.add_argument('--uniform', default=True, action='store_true',
                         help='All elements have equal probability')
    sampler.add_argument('--decay', default=False,
                         help='Prefer more recent elements',
                         type=float)
    sampler.add_argument('--weighted', default=False,
                         help='values are attached to a weight',
                         type=float)
    return parser


def main():
    parser = gen_parser()
    args = parser.parse_args()

    if args.uniform:
        sampler = UniformSampler(size=args.size)

    if args.decay:
        sampler = ExponentialSampler(size=args.size, decay=args.decay)

    if args.file:
        with open(args.file) as res:
            sampler.sample(res)
            print(sampler)

    if args.stream:
        for line in sys.stdin:
            sampler.append(line.strip())
        print(sampler)

if __name__ == "__main__":
    sys.exit(main())
