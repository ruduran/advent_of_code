import argparse
from argparse import Namespace
from typing import Generator


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_rucksacks(file: str) -> Generator[str, None, None]:
    with open(file) as f:
        for line in f:
            if data := line.strip():
                yield data


def find_redundant(rucksack: str) -> str:
    c_size = len(rucksack)//2
    c1, c2 = set(rucksack[:c_size]), set(rucksack[c_size:])
    return (c1 & c2).pop()


def priority(element: str) -> int:
    if element.islower():
        return ord(element) - ord("a") + 1
    else:
        return ord(element) - ord("A") + 27


def main():
    args = parse_arguments()
    rucksacks = list(read_rucksacks(args.filename))

    redundants = [find_redundant(rucksack) for rucksack in rucksacks]
    priorities = [priority(e) for e in redundants]
    print(sum(priorities))

    groups = zip(rucksacks[:-2:3], rucksacks[1:-1:3], rucksacks[2::3])
    tags = [(set(a) & set(b) & set(c)).pop() for (a, b, c) in groups]
    priorities = [priority(e) for e in tags]
    print(sum(priorities))


if __name__ == "__main__":
    main()
