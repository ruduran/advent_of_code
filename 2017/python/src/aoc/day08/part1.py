#!/usr/bin/env python

from . import BaseProcessor

from aoc.utils import get_file_name


class Processor(BaseProcessor):
    def process(self):
        self.load_data()
        return max(self.registers.values())


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
