#!/usr/bin/env python

from . import BaseProcessor, get_input_number


class ProcessorP1(BaseProcessor):
    def _calc_steps(self, x_dist, y_dist):
        return x_dist + y_dist


def main():
    processor = ProcessorP1(get_input_number())
    print(processor.calculate_steps())


if __name__ == '__main__':
    main()
