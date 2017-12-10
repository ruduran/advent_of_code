#!/usr/bin/env python

from . import BaseProcessor

from aoc.utils import get_file_name


class Processor(BaseProcessor):
    def process(self):
        self.load_lenghts()
        self.run_round()
        return self.number_list[0] * self.number_list[1]

    def load_lenghts(self):
        with open(self.filename) as f:
            line = f.readline().strip()
            self.lenghts = [int(n) for n in line.split(',')]


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
