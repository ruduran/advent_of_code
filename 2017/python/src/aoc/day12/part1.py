#!/usr/bin/env python

from aoc.utils import get_file_name
from . import BaseProcessor


class Processor(BaseProcessor):
    def process(self):
        self.load_program_connections()
        return len(self.programs_connected_with(0))


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
