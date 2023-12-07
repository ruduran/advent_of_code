import argparse
from argparse import Namespace
from typing import Generator, Optional


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def get_datastreams(file: str) -> Generator[str, None, None]:
    with open(file) as f:
        for line in f:
            if data := line.rstrip():
                yield data


def find_first_marker(datastream: str, num_distinct: int) -> Optional[int]:
    for i in range(num_distinct, len(datastream)):
        possible_marker = datastream[i-num_distinct:i]
        if len(set(possible_marker)) == num_distinct:
            return i

    return None


def main():
    args = parse_arguments()
    for datastream in get_datastreams(args.filename):
        print(find_first_marker(datastream, 4))
        print(find_first_marker(datastream, 14))


if __name__ == "__main__":
    main()
