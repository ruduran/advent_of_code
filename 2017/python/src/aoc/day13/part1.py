#!/usr/bin/env python

from aoc.utils import get_file_name
from . import BaseProcessor


class Processor(BaseProcessor):
    def process(self):
        self.load_firewall_conf()
        return self.calc_severity()

    def calc_severity(self, start=0, lane=0):
        severity = 0
        for depth, layer_range in self.firewall_layers.items():
            time_on_layer = depth + start
            if self.caught_at_depth(depth, time_on_layer, lane):
                severity += depth * layer_range
        return severity


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
