#!/usr/bin/env python

from aoc.utils import get_file_name

from . import BaseProcessor


class Processor(BaseProcessor):

    def process(self):
        self.load_instructions()
        self.run_instructions()
        return ''.join(self.programs)


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
