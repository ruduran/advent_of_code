#!/usr/bin/env python

from collections import defaultdict

from aoc.utils import get_file_name

from . import BaseProcessor


class Processor(BaseProcessor):
    def process(self):
        self.load_data()
        self.balance_towers()
        return self.balanced

    def balance_towers(self):
        self.get_and_balance_weight(self.root)

    # TODO: Refactor and IMPROVE
    def get_and_balance_weight(self, program):
        weight_sum = 0
        weights_programs = defaultdict(list)
        for p, p_info in program['children'].items():
            weight = self.get_and_balance_weight(p_info)
            weight_sum += weight
            weights_programs[weight].append(p)

        if len(weights_programs) > 1:
            weights = list(weights_programs)
            weight_diff = abs(weights[0] - weights[1])
            mean = sum(weights) / 2

            for weight, prog_list in weights_programs.items():
                if len(prog_list) == 1:
                    if weight > mean:
                        weight_diff = -weight_diff
                    prog_name = prog_list[0]
                    program['children'][prog_name]['weight'] += weight_diff
                    self.balanced = program['children'][prog_name]['weight']
                    weight_sum += weight_diff

        return weight_sum + program['weight']


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
