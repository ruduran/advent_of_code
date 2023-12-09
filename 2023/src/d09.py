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
class Node:
    left: str
    right: str


def parse_input(data: list[str]) -> list[list[int]]:
    return [[int(n) for n in line.split()] for line in data]


def extrapolated_next_value(sequence: list[int]) -> int:
    diff_sequence = [b - a for a, b in zip(sequence[:-1], sequence[1:])]
    if all(map(lambda x: x == 0, diff_sequence)):
        return sequence[-1]
    else:
        extrapolated_next_diff = extrapolated_next_value(diff_sequence)
        return sequence[-1] + extrapolated_next_diff


def extrapolated_previous_value(sequence: list[int]) -> int:
    """Could it be refactored with the previous function? yes.... do I feel like it? :D"""
    diff_sequence = [b - a for a, b in zip(sequence[:-1], sequence[1:])]
    if all(map(lambda x: x == 0, diff_sequence)):
        return sequence[0]
    else:
        extrapolated_previous_diff = extrapolated_previous_value(diff_sequence)
        return sequence[0] - extrapolated_previous_diff


def main():
    args = parse_arguments()
    file_content = read_raw_file(args.filename)
    sequences = parse_input(file_content)

    extrapolated_next_values = [extrapolated_next_value(s) for s in sequences]
    print(sum(extrapolated_next_values))

    extrapolated_previous_values = [extrapolated_previous_value(s) for s in sequences]
    print(sum(extrapolated_previous_values))


if __name__ == "__main__":
    main()
