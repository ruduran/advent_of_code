from __future__ import annotations

import argparse

from argparse import Namespace
from typing import Generator


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def get_grid(file: str) -> Generator[list[int], None, None]:
    with open(file) as f:
        for line in f:
            if data := line.rstrip():
                yield [int(c) for c in data]


def num_visible(grid: list[list[int]]) -> int:
    # start with the perimeter
    height = len(grid)
    width = len(grid[0])
    count = 2*(height - 2) + 2*width

    for h in range(1, height-1):
        for w in range(1, width-1):
            row = grid[h]
            column = [r[w] for r in grid]
            height = grid[h][w]
            max_left = max(row[:w])
            max_right = max(row[w+1:])
            max_top = max(column[:h])
            max_bottom = max(column[h+1:])
            visible = height > max_left or height > max_right or height > max_top or height > max_bottom
            if visible:
                count += 1

    return count


def _viewing_distance(row: list[int], height: int) -> int:
    for i, t in enumerate(row, start=1):
        if t >= height:
            return i

    return len(row)


def max_scenic_score(grid: list[list[int]]) -> int:
    # start with the perimeter
    height = len(grid)
    width = len(grid[0])
    scenic_score = 0

    for h in range(1, height-1):
        for w in range(1, width-1):
            row = grid[h]
            column = [r[w] for r in grid]
            height = grid[h][w]
            left = row[:w]
            right = row[w+1:]
            top = column[:h]
            bottom = column[h+1:]
            score = _viewing_distance(list(reversed(left)), height) * _viewing_distance(right, height) * _viewing_distance(list(reversed(top)), height) * _viewing_distance(bottom, height)
            scenic_score = max(scenic_score, score)

    return scenic_score


def main():
    args = parse_arguments()
    grid = list(get_grid(args.filename))
    print(num_visible(grid))
    print(max_scenic_score(grid))


if __name__ == "__main__":
    main()
