#!/usr/bin/env python

from . import BaseProcessor
from aoc.utils import get_file_name


class Processor(BaseProcessor):
    def number_of_jumps_to_get_out(self, jump_list):
        index = 0
        jump_count = 0
        while index >= 0 and index < len(jump_list):
            jump = jump_list[index]
            if jump >= 3:
                jump_list[index] -= 1
            else:
                jump_list[index] += 1
            index += jump
            jump_count += 1
        return jump_count


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
