import argparse
from argparse import Namespace
from typing import Generator


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def parse_assignment(raw_assignment: str) -> set[int]:
    start, end = raw_assignment.split("-")
    return set(range(int(start), int(end) + 1))


def read_assignment_pairs(file: str) -> Generator[tuple[set[int], set[int]], None, None]:
    with open(file) as f:
        for line in f:
            if data := line.strip():
                a1, a2 = data.split(",")
                yield parse_assignment(a1), parse_assignment(a2)


def assignments_fully_containing_one_another(assignment_pairs: list[tuple[set[int], set[int]]]) -> int:
    count = 0
    for a1, a2 in assignment_pairs:
        if a1.issubset(a2) or a2.issubset(a1):
            count += 1

    return count


def assignments_overlapping(assignment_pairs: list[tuple[set[int], set[int]]]) -> int:
    count = 0
    for a1, a2 in assignment_pairs:
        if not a1.isdisjoint(a2):
            count += 1

    return count


def main():
    args = parse_arguments()
    assignment_pairs = list(read_assignment_pairs(args.filename))
    print(assignments_fully_containing_one_another(assignment_pairs))
    print(assignments_overlapping(assignment_pairs))


if __name__ == "__main__":
    main()
