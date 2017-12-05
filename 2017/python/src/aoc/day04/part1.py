#!/usr/bin/env python

from . import BaseProcessor
from aoc.utils import get_file_name


class Processor(BaseProcessor):
    def is_passphrase_valid(self, passphrase):
        words = passphrase.split()
        num_words = len(words)
        num_diff_words = len(set(words))
        return (num_words and num_words == num_diff_words)


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
