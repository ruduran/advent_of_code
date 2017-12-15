#!/usr/bin/env python

from aoc.utils import get_file_name

from . import BaseProcessor


class Processor(BaseProcessor):
    def __init__(self, filename):
        super().__init__(filename)
        self.generator['A'].set_multiple_of_condition(4)
        self.generator['B'].set_multiple_of_condition(8)

    def process(self):
        self.load_start_values()
        return self.get_eq_count(5000000)


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
