"""
This is a effective random uniform sampling module known as
Reservoir Sampling which uniformly samples a subset of k elements from
a larger 'reservoir' of size N where N may be unknown or very large.


Examples:
---------
    The command line tool itself takes in either a stream or a file.
    The following examples samples 100 elements a streaming twitter
    api and a text file respectly.

        $ twitter-streaming-api | python sample.py --stream 100
        $ python sample.py --file tweets.txt 100
        $ python sample.py -h

Attributes:
-----------
    UniformSampler (Object): This module contains a UniformClass object with
        an `accept` method that takes in the ith element and `consume` that
        processes an iterable and returns the sampled elements.

Author: Jason Liu
Date: May 24th, 2014

"""

from random import randint
import argparse
import sys

class UniformSampler(object):
    """Sample k elements from a stream/iterable of unknown/large size.

    Attributes:
        saves (list): List the k elements currently in memory
        counter (int): Memory of the number of elements that have been looked at
        _max (int): The max number of samples allowed in memory, `k`

    """
    def __init__(self, max_sample=1):
        self.saves = list()
        self._max = max_sample
        self.counter = int()

    def accept(self, item):
        """Accept new value and persist in memory if selected

        Args:
            item: Item you wish you inspect for selection, if successfull,
                  it will switch places with a random element in `saves`

        """
        self.counter += 1
        switch = randint(0, self.counter)
        if len(self.saves) < self._max:
            self.saves.append(item)
        elif switch < self._max:
            self.saves[switch] = item

        return self.saves

    def consume(self, iterable):
        """Sample k elemebts from an iterable! Duh.

        Args:
            iterable: Iterable

        Returns:
            the list of elements sampled from the iterable

        """
        for item in iterable:
            self.accept(item)

        return self.saves
    def __str__(self):
        output = str()
        for item in self.saves:
            output += "{item}\n".format(item=item.strip())
        return output

def gen_parser():
    """Generate the CLI args parser"""
    desc = """Sample k elements from a stream or file"""
    parser = argparse.ArgumentParser(description=desc)
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
    sampler = UniformSampler(max_sample=args.size)

    if args.file:
        with open(args.file) as res:
            sampler.consume(res)
            print sampler

    if args.stream:
        for line in sys.stdin:
            sampler.accept(line.strip())
        print sampler

if __name__ == "__main__":
    sys.exit(main())

