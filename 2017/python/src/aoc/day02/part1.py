#!/usr/bin/env python

from . import BaseProcessor, get_file_name


class ProcessorP1(BaseProcessor):
    def _calc_checksum(self, file_data):
        checksum = 0
        for line_data in file_data:
            sorted_line = sorted(line_data)
            min_value = sorted_line[0]
            max_value = sorted_line[-1]
            checksum += max_value - min_value

        return checksum


def main():
    processor = ProcessorP1(get_file_name())
    print(processor.calculate_checksum())


if __name__ == '__main__':
    main()
