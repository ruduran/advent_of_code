#!/usr/bin/env python

from tqdm import tqdm

from aoc.utils import get_file_name

from . import BaseProcessor


class Processor(BaseProcessor):
    def __init__(self, filename):
        super().__init__(filename)
        self.ocurrences = {}

    def process(self):
        self.load_instructions()
        self.run_iterations(1000000000)
        return ''.join(self.programs)

    def run_iterations(self, iterations):
        remaining = 0
        for i in tqdm(range(iterations)):
            cycle = self.get_cycle_len(i)
            if cycle:
                remaining = iterations - i
                remaining %= cycle
                break
            else:
                self.run_iteration(i)

        for i in tqdm(range(remaining)):
            self.run_instructions()

    def run_iteration(self, it):
        self.ocurrences[''.join(self.programs)] = it
        self.run_instructions()

    def get_cycle_len(self, current_it):
        current_status = ''.join(self.programs)
        if current_status in self.ocurrences:
            return current_it - self.ocurrences[current_status]


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
