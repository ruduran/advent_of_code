from __future__ import annotations

import argparse
from argparse import Namespace
from functools import reduce


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


def parse_input(data: list[str]) -> (list[int], list[int]):
    times = [int(t) for t in data[0].split(":")[1].split()]
    distances = [int(t) for t in data[1].split(":")[1].split()]
    return times, distances


def parse_input_correcting_kerning(data: list[str]) -> (int, int):
    time = int("".join([c for c in data[0] if c.isdigit()]))
    distance = int("".join([c for c in data[1] if c.isdigit()]))
    return time, distance


def ways_to_beat_the_record(distance: int, time: int) -> int:
    """Could be optimized finding just the first and last possibility but... meh"""
    ways = 0
    for t in range(1, time):
        moving_time = time-t
        speed = t
        if moving_time*speed > distance:
            ways += 1
    return ways


def main():
    args = parse_arguments()
    file_content = read_raw_file(args.filename)
    times, distances = parse_input(file_content)
    ways_to_beat = []
    for i in range(0, len(times)):
        ways_to_beat.append(ways_to_beat_the_record(distances[i], times[i]))
    print(reduce(lambda x, y: x*y, [w for w in ways_to_beat], 1))

    time, distance = parse_input_correcting_kerning(file_content)
    print(ways_to_beat_the_record(distance, time))


if __name__ == "__main__":
    main()
