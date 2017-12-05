#!/usr/bin/env python

from . import BaseProcessor
from aoc.utils import get_file_name


class Processor(BaseProcessor):
    def _calc_checksum(self, file_data):
        checksum = 0
        for line_data in file_data:
            sorted_line = sorted(line_data)
            min_value = sorted_line[0]
            max_value = sorted_line[-1]
            checksum += max_value - min_value

        return checksum


def main():
    processor = Processor(get_file_name())
    print(processor.calculate_checksum())


if __name__ == '__main__':
    main()
