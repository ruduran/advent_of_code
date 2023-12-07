from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List

from aoc2021.common import get_file_name


class Direction(str, Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"


@dataclass
class Command:
    direction: Direction
    units: int

    @staticmethod
    def from_str(value: str) -> Command:
        value_split = value.strip().split(" ", 1)
        return Command(Direction(value_split[0]), int(value_split[1]))


def parse_input() -> List[Command]:
    with open(get_file_name()) as file:
        return [Command.from_str(line) for line in file]


def execute(command_list: List[Command]) -> int:
    horizontal = depth = 0
    for command in command_list:
        if command.direction == Direction.FORWARD:
            horizontal += command.units
        elif command.direction == Direction.DOWN:
            depth += command.units
        elif command.direction == Direction.UP:
            depth -= command.units

    return horizontal*depth


def execute_correct(command_list: List[Command]) -> int:
    horizontal = depth = aim = 0
    for command in command_list:
        if command.direction == Direction.FORWARD:
            horizontal += command.units
            depth += aim*command.units
        elif command.direction == Direction.DOWN:
            aim += command.units
        elif command.direction == Direction.UP:
            aim -= command.units

    return horizontal*depth


def main():
    command_list = parse_input()
    print(execute(command_list))
    print(execute_correct(command_list))


if __name__ == '__main__':
    main()
