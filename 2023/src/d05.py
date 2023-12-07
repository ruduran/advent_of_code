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
class Range:
    start: int
    end: int


@dataclass
class Map:
    id: str
    raw_map: list[list[int]]

    def map_values(self, values: list[int]) -> list[int]:
        mapped_values = []
        for v in values:
            for m in self.raw_map:
                if v in range(m[1], m[1] + m[2]):
                    mapped_values.append(v + m[0]-m[1])
                    break
            else:
                mapped_values.append(v)
        return mapped_values

    def map_ranges(self, ranges: list[Range]) -> list[Range]:
        mapped_ranges = []
        for r in ranges:
            for m in self.raw_map:
                dst_range_start = m[0]
                src_range_start = m[1]
                range_elements = m[2]
                src_range_end = src_range_start + range_elements - 1
                map_diff = dst_range_start-src_range_start

                possible_start = max(r.start, src_range_start)
                possible_end = min(r.end, src_range_end)
                if possible_start <= possible_end:
                    if possible_start > r.start:
                        mapped_ranges.append(Range(start=r.start, end=possible_start-1))

                    mapped_ranges.append(Range(start=possible_start + map_diff, end=possible_end + map_diff))

                    if possible_end > r.end:
                        mapped_ranges.append(Range(start=possible_end+1, end=r.end))

                    break
            else:
                mapped_ranges.append(r)

        return mapped_ranges


def parse_input(data: list[str]) -> (list[int], list[Map]):
    raw_seeds = data[0].split(": ")[-1]
    seeds = [int(n) for n in raw_seeds.split()]

    maps = []
    map_id = None
    raw_map = []
    for line in data[1:]:
        if line[0].isdigit():
            raw_map.append([int(n) for n in line.split()])
        else:
            if map_id:
                maps.append(Map(id=map_id, raw_map=raw_map))
                raw_map = []

            map_id = line.split()[0]
    if map_id:
        maps.append(Map(id=map_id, raw_map=raw_map))

    return seeds, maps


def generate_seed_ranges(seeds: list[int]) -> list[Range]:
    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append(Range(start=seeds[i], end=seeds[i]+seeds[i+1]-1))
    return ranges


def location_from_seeds(seeds: list[int], maps: list[Map]) -> list[int]:
    values = seeds
    for m in maps:
        values = m.map_values(values)
    return values


def main():
    args = parse_arguments()
    file_content = read_raw_file(args.filename)
    seeds, maps = parse_input(file_content)
    print(min(location_from_seeds(seeds, maps)))

    ranges = generate_seed_ranges(seeds)
    for m in maps:
        ranges = m.map_ranges(ranges)
    print(min([r.start for r in ranges]))


if __name__ == "__main__":
    main()
