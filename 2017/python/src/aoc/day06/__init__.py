#!/usr/bin/env python

from aoc.utils import get_file_name


class Processor(object):
    def __init__(self, filename):
        self.filename = filename
        self.already_seen_list = []
        self.cycles = 0

    def process(self):
        with open(self.filename) as f:
            bank_list = [int(n) for n in f.readline().strip().split('\t')]
            return self.count_cycles(bank_list)

    def count_cycles(self, bank_list):
        self.cycles = 0
        cycle_seen = 0
        while cycle_seen == 0:
            self.mark_as_seen(bank_list.copy())
            bank_list = self.run_cycle(bank_list)
            cycle_seen = self.already_seen(bank_list)
        return (self.cycles, self.cycles - cycle_seen)

    def mark_as_seen(self, bank_list):
        self.already_seen_list.append((bank_list.copy(), self.cycles))

    def already_seen(self, bank_list):
        for (seen_list, cycle) in self.already_seen_list:
            if seen_list == bank_list:
                return cycle
        return False

    def run_cycle(self, bank_list):
        self.cycles += 1
        index_to_reallocate = self.bank_to_reallocate(bank_list)
        return self.reallocate(bank_list, index_to_reallocate)

    def bank_to_reallocate(self, bank_list):
        return bank_list.index(max(bank_list))

    def reallocate(self, bank_list, index_to_reallocate):
        blocks = bank_list[index_to_reallocate]
        bank_list[index_to_reallocate] = 0
        block_num = len(bank_list)
        blocks_per_bank = int(blocks / block_num)
        blocks_with_extra = blocks % block_num
        for i in range(block_num):
            index = i + index_to_reallocate + 1
            if index >= block_num:
                index -= block_num

            bank_list[index] += blocks_per_bank
            if i < blocks_with_extra:
                bank_list[index] += 1

        return bank_list


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
