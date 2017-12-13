#!/usr/bin/env python

from aoc.utils import get_file_name
from . import BaseProcessor


class Processor(BaseProcessor):
    def process(self):
        self.load_firewall_conf()
        return self.first_time_not_cautht()

    def first_time_not_cautht(self, lane=0):
        start_time = 0
        # FIXME: This could lead to an infinite loop if always caught
        # The limit could be the LCM of the full_cycles (range*2 - 2)
        while self.caught(start=start_time, lane=lane) > 0:
            start_time += 1
        return start_time

    def caught(self, start=0, lane=0):
        for depth, layer_range in self.firewall_layers.items():
            time_on_layer = depth + start
            if self.caught_at_depth(depth, time_on_layer, lane):
                return True
        return False


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
