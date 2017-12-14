#!/usr/bin/env python

from aoc.utils import get_file_name

from . import BaseProcessor


class Processor(BaseProcessor):
    def process(self):
        self.load_lenghts()
        return self.get_hash()

    def load_lenghts(self):
        with open(self.filename) as f:
            line = f.readline().strip()
            self.set_input(line)


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
