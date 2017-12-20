#!/usr/bin/env python

from aoc.utils import get_file_name
from . import BaseProcessor


class Processor(BaseProcessor):

    def process(self):
        self.load_steps()
        self.run(2017, 2017)
        self.pos = self.buffer.index(2017)
        self.move(1)
        return self.buffer[self.pos]


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
