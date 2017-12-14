#!/usr/bin/env python

from aoc.utils import get_file_name

from . import BaseProcessor


class Processor(BaseProcessor):

    def process(self):
        self.load_input()
        return self.num_squares_used()

    def num_squares_used(self):
        disk_status = self.get_disk_status()

        used = 0
        for row in disk_status:
            used += row.count('1')
        return used


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
