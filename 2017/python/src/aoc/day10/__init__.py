#!/usr/bin/env python

from aoc.utils import get_file_name


class Processor(object):
    MARKS = 256

    def __init__(self, filename):
        self.filename = filename
        self.number_list = list(range(self.MARKS))
        self.lenghts = []
        self.current_position = 0
        self.skip_size = 0

    def process(self):
        self.load_lenghts()
        self.process_hash()
        return self.number_list[0] * self.number_list[1]

    def load_lenghts(self):
        with open(self.filename) as f:
            line = f.readline().strip()
            self.lenghts = [int(n) for n in line.split(',')]

    def process_hash(self):
        for lenght in self.lenghts:
            if lenght <= self.MARKS:
                self.reverse(lenght)
                self.current_position += lenght + self.skip_size
                self.current_position %= self.MARKS
                self.skip_size += 1

    def reverse(self, lenght):
        if lenght <= 1:
            return

        start = self.current_position
        end = self.current_position + lenght
        to_reverse = self.number_list[start:end]
        # self.number_list[start:end] = to_reverse[::-1]
        if len(to_reverse) < lenght:
            end %= self.MARKS
            to_reverse += self.number_list[0:end]

        reversed_list = to_reverse[::-1]

        if start + len(reversed_list) > self.MARKS:
            division = self.MARKS - start
            self.number_list[start:self.MARKS] = reversed_list[0:division]
            self.number_list[0:end] = reversed_list[division:]
        else:
            self.number_list[start:end] = reversed_list


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
