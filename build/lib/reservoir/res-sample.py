"""
This is a effective random uniform sampling module known as
Reservoir Sampling which uniformly samples a subset of k elements from
a larger 'reservoir' of size N where N may be unknown or very large.


Examples:
---------
    The command line tool itself takes in either a stream or a file.
    The following examples samples 100 elements a streaming twitter
    api and a text file respectably.

        $ twitter-streaming-api | python sample.py --stream 100
        $ python sample.py --file tweets.txt 100
        $ python sample.py -h

Attributes:
-----------
    UniformSampler (Object): This module contains a UniformClass object with
        an `feed` method that takes in the ith element and `stream_sample` that
        processes any iterable and returns the sampled elements.

Author: Jason Liu
Date: May 24th, 2014

"""
from __future__ import print_function
from argparse import ArgumentParser
import sys

def gen_parser():
    """Generate the CLI argparse object"""
    desc = """Random sampling is often applied to very large datasets and
              in particular to data streams. In this case, the random sample
              has to be generated in one pass over an potentially unknown population.
              """
    parser = ArgumentParser(description=desc)
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('size',
                        help="The number of elements you wish you sample",
                        type=int)
    group.add_argument('-f', '--file',
                      default=False,
                       type=str)
    group.add_argument('-s', '--stream',
                       default=False,
                       action='store_true',
                       help='For use with pipes and redirects')
    return parser


def main():
    parser = gen_parser()
    args = parser.parse_args()
    sampler = UniformSampler(size=args.size)

    if args.file:
        with open(args.file) as res:
            sampler.stream_sample(res)
            print(sampler)

    if args.stream:
        for line in sys.stdin:
            sampler.feed(line.strip())
        print(sampler)

if __name__ == "__main__":
    sys.exit(main())
