#!/usr/bin/env python

from . import BaseProcessor

from aoc.utils import get_file_name


class Processor(BaseProcessor):
    def __init__(self, filename):
        super().__init__(filename)
        self.max_value = None

    def process(self):
        self.load_data()
        return self.max_value

    # TODO: Improve this
    def process_line(self, line):
        super().process_line(line)
        max_on_this_iter = max(self.registers.values())
        if self.max_value is not None:
            self.max_value = max(max_on_this_iter, self.max_value)
        else:
            self.max_value = max_on_this_iter


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
