from __future__ import annotations

from functools import reduce
from typing import List

from aoc2021.common import get_file_name


def parse_input() -> List[List[int]]:
    with open(get_file_name()) as file:
        return [[int(c) for c in line.strip()] for line in file]


def to_int(binary_number: List[int]) -> int:
    return reduce(lambda t, n: t*2+n, binary_number)


def power_consumption(diagnostic_report: List[List[int]]) -> int:
    gamma = []
    epsilon = []
    for p in range(len(diagnostic_report[0])):
        occurrences = {
            0: 0,
            1: 0
        }
        for number in diagnostic_report:
            occurrences[number[p]] += 1

        if occurrences[0] >= occurrences[1]:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)

    return to_int(gamma)*to_int(epsilon)


def main():
    diagnostic_report = parse_input()
    print(power_consumption(diagnostic_report))


if __name__ == '__main__':
    main()
