#!/usr/bin/env python

from . import BaseProcessor, get_file_name


class ProcessorP1(BaseProcessor):
    def process_number_list(self, numbers):
        last_num = 0
        total = 0
        for num in numbers:
            if last_num == num:
                total += last_num
            last_num = num
        if numbers[0] == numbers[-1] and len(numbers) > 1:
            total += numbers[0]

        return total


def main():
    processor = ProcessorP1(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
