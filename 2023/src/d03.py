from __future__ import annotations

import argparse
from argparse import Namespace
from dataclasses import dataclass


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_raw_file(file: str) -> list[str]:
    content = []
    with open(file) as f:
        for line in f:
            data = line.strip()
            if data:
                content.append(data)
    return content


@dataclass
class Number:
    value: int
    row: int
    start_col: int
    end_col: int

    def is_adjacent_to(self, row: int, col: int) -> bool:
        if self.row-1 <= row <= self.row+1:
            if self.start_col-1 <= col <= self.end_col+1:
                return True
        return False


def get_all_numbers(schematic: list[str]) -> list[Number]:
    numbers = []
    parsing_number = False
    value = 0
    start_col = 0
    for row, line in enumerate(schematic):
        for col, c in enumerate(line):
            if c.isdigit():
                if parsing_number:
                    value = value*10 + int(c)
                else:
                    parsing_number = True
                    value = int(c)
                    start_col = col
            else:
                if parsing_number:
                    numbers.append(Number(value=value, row=row, start_col=start_col, end_col=col-1))
                    parsing_number = False

        if parsing_number:
            numbers.append(Number(value=value, row=row, start_col=start_col, end_col=len(line)))
            parsing_number = False

    return numbers


def is_part_number(schematic: list[str], number: Number) -> bool:
    for row in range(max(number.row-1, 0), min(number.row+2, len(schematic))):
        for col in range(max(number.start_col-1, 0), min(number.end_col+2, len(schematic[row]))):
            c = schematic[row][col]
            if not c.isdigit() and c != '.':
                return True

    return False


def get_gears(schematic: list[str], numbers: list[Number]) -> list[int]:
    gears = []
    for row, line in enumerate(schematic):
        for col, c in enumerate(line):
            if c == '*':
                adjacent_numbers = [n.value for n in numbers if n.is_adjacent_to(row, col)]
                if len(adjacent_numbers) == 2:
                    gears.append(adjacent_numbers[0]*adjacent_numbers[1])
    return gears


def main():
    args = parse_arguments()
    schematic = read_raw_file(args.filename)
    numbers = get_all_numbers(schematic)
    print(sum([n.value for n in numbers if is_part_number(schematic, n)]))
    gears = get_gears(schematic, numbers)
    print(sum(gears))


if __name__ == "__main__":
    main()
