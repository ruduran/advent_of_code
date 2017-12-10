#!/usr/bin/env python

from functools import reduce

from aoc.utils import get_file_name

from . import BaseProcessor


class Processor(BaseProcessor):
    def process(self):
        self.load_lenghts()
        return self.calculate_hash()

    def load_lenghts(self):
        with open(self.filename) as f:
            line = f.readline().strip()
            self.lenghts = [ord(n) for n in line]

        self.lenghts += [17, 31, 73, 47, 23]

    def calculate_hash(self):
        for i in range(64):
            self.run_round()

        group_size = 16
        dense_list = []
        index = 0
        while index < len(self.number_list):
            stop = index + group_size
            dense_list.append(reduce(lambda i, j: int(i) ^ int(j),
                              self.number_list[index: stop]))
            index = stop

        return ''.join(map("{:02x}".format, dense_list))


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
