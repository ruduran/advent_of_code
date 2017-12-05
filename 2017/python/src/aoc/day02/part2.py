#!/usr/bin/env python

from . import BaseProcessor
from aoc.utils import get_file_name


class Processor(BaseProcessor):
    def _calc_checksum(self, file_data):
        checksum = 0
        for line_data in file_data:
            sorted_line = sorted(line_data)
            for i in range(len(sorted_line)):
                for j in range((i + 1), len(sorted_line)):
                    if sorted_line[j] % sorted_line[i] == 0:
                        checksum += int(sorted_line[j] / sorted_line[i])

        return checksum


def main():
    processor = Processor(get_file_name())
    print(processor.calculate_checksum())


if __name__ == '__main__':
    main()
