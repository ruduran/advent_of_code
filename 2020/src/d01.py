from math import prod
from typing import List

from aoc2020.common import get_file_name


def read_expense_report() -> List[int]:
    with open(get_file_name()) as file:
        return [int(line) for line in file]


def find_entries_that_sum(num_of_entries: int, entries_sum: int, report: List[int]) -> List[int]:
    if num_of_entries < 1:
        raise Exception("No entries?")

    if num_of_entries > len(report):
        raise Exception("Ehem...")

    if num_of_entries == 1:
        if entries_sum in report:
            return [entries_sum]
    else:
        for i, e in enumerate(report[:-num_of_entries]):
            remaining_entries = find_entries_that_sum(num_of_entries - 1, entries_sum - e, report[i+1:])
            if remaining_entries:
                return [e] + remaining_entries

    return []


def main():
    report = read_expense_report()
    for entry_num in (2, 3):
        entries = find_entries_that_sum(entry_num, 2020, report)
        if entries:
            print(prod(entries))
        else:
            print("Not found")


if __name__ == '__main__':
    main()
