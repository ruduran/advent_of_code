#!/usr/bin/env python

from aoc.utils import get_file_name

from . import BaseProcessor


class Processor(BaseProcessor):

    def process(self):
        self.load_input()
        return self.num_regions()

    def num_regions(self):
        disk_status = self.get_disk_status()

        regions = 0
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if disk_status[i][j] == '1':
                    regions += 1
                    self.mark_region(disk_status, i, j)
        return regions

    def mark_region(self, disk_status, i, j):
        if disk_status[i][j] != '1':
            return

        disk_status[i][j] = '_'
        if i > 0:
            self.mark_region(disk_status, i - 1, j)
        if i < self.SIZE - 1:
            self.mark_region(disk_status, i + 1, j)
        if j > 0:
            self.mark_region(disk_status, i, j - 1)
        if j < self.SIZE - 1:
            self.mark_region(disk_status, i, j + 1)


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
