#!/usr/bin/env python

from tqdm import tqdm

from aoc.utils import get_file_name

from . import BaseProcessor


class Processor(BaseProcessor):

    def process(self):
        self.load_instructions()
        # TODO: Check positions after the first run and after that just do the exchange
        for i in tqdm(range(1000000000)):
            self.run_instructions()
        return ''.join(self.programs)


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
