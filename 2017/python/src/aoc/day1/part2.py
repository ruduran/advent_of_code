#!/usr/bin/env python

from . import BaseProcessor, get_file_name


class ProcessorP1(BaseProcessor):
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
    processor = ProcessorP1(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
