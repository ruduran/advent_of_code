from __future__ import annotations

import argparse

from argparse import Namespace
from dataclasses import dataclass
from enum import Enum, auto
from typing import Generator, Iterator, Tuple


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


@dataclass
class Movement:
    direction: Direction
    steps: int


@dataclass
class Position:
    x: int
    y: int

    def get_close(self, other: Position) -> None:
        if self.x == other.x:
            if self.y - other.y > 1:
                self.y -= 1
            elif other.y - self.y > 1:
                self.y += 1
        elif self.y == other.y:
            if self.x - other.x > 1:
                self.x -= 1
            elif other.x - self.x > 1:
                self.x += 1
        elif abs(self.x - other.x) > 1 or abs(self.y - other.y) > 1:
            if self.x > other.x:
                self.x -= 1
            else:
                self.x += 1

            if self.y > other.y:
                self.y -= 1
            else:
                self.y += 1

    def as_tuple(self) -> Tuple[int, int]:
        return self.x, self.y


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_movements(file: str) -> Generator[Movement, None, None]:
    with open(file) as f:
        for line in f:
            if data := line.rstrip():
                match data.split():
                    case ["L", steps]:
                        yield Movement(Direction.LEFT, int(steps))
                    case ["R", steps]:
                        yield Movement(Direction.RIGHT, int(steps))
                    case ["U", steps]:
                        yield Movement(Direction.UP, int(steps))
                    case ["D", steps]:
                        yield Movement(Direction.DOWN, int(steps))


def simulate(movements: Iterator[Movement], length: int) -> int:
    rope = [Position(0, 0) for _ in range(length)]
    visited_positions = {rope[-1].as_tuple()}
    for m in movements:
        for _ in range(m.steps):
            if m.direction == Direction.UP:
                rope[0].x += 1
            elif m.direction == Direction.DOWN:
                rope[0].x -= 1
            elif m.direction == Direction.RIGHT:
                rope[0].y += 1
            else:
                rope[0].y -= 1

            for i in range(len(rope)-1):
                rope[i + 1].get_close(rope[i])

            visited_positions.add(rope[-1].as_tuple())

    return len(visited_positions)


def main():
    args = parse_arguments()
    movements = list(read_movements(args.filename))
    print(simulate(movements, 2))
    print(simulate(movements, 10))


if __name__ == "__main__":
    main()
