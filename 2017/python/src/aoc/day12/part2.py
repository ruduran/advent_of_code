#!/usr/bin/env python

from aoc.utils import get_file_name
from . import BaseProcessor


class Processor(BaseProcessor):
    def process(self):
        self.load_program_connections()
        return len(self.program_groups())

    def program_groups(self):
        groups = []
        programs_to_check = set(self.program_connections.keys())
        while programs_to_check:
            group = self.programs_connected_with(programs_to_check.pop())
            groups.append(group)
            programs_to_check.difference_update(group)
        return groups


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
