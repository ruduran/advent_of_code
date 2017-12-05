#!/usr/bin/env python

from itertools import permutations

from . import BaseProcessor
from aoc.utils import get_file_name


class Processor(BaseProcessor):
    def is_passphrase_valid(self, passphrase):
        words = passphrase.split()
        anagrams = set()
        for word in words:
            if word in anagrams:
                return False

            anagrams.update(self.generate_anagrams(word))

        return True

    def generate_anagrams(self, word):
        return {''.join(p) for p in permutations(word)}


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
