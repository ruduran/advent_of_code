#!/usr/bin/env python

from . import BaseProcessor
from aoc.utils import get_file_name


class Processor(BaseProcessor):
    def process_number_list(self, numbers):
        total = 0
        half_lenght = int(len(numbers) / 2)
        for i in range(half_lenght):
            num = numbers[i]
            mirror_num = numbers[half_lenght + i]
            if num == mirror_num:
                total += 2 * num

        return total


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
