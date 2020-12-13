from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import List

from aoc2020.common import get_file_name


def read_instructions() -> List[str]:
    instruction = []
    with open(get_file_name()) as file:
        for line in file:
            if line:
                instruction.append(line.strip())

    return instruction


class Orientation(IntEnum):
    North = 0
    East = 1
    South = 2
    West = 3

    def rotate(self, left: int = 0, right: int = 0) -> Orientation:
        if left > 0 and right > 0:
            raise Exception("Left or right??")

        num_rotations = 0

        if left > 0:
            num_rotations -= left // 90

        if right > 0:
            num_rotations = right // 90

        return Orientation((self + num_rotations) % len(Orientation))


@dataclass
class Position:
    x: int = 0
    y: int = 0

    def move(self, orientation: Orientation, value: int) -> None:
        if orientation == Orientation.North:
            self.y += value
        elif orientation == Orientation.East:
            self.x += value
        elif orientation == Orientation.South:
            self.y -= value
        else:
            self.x -= value


STR_TO_ORIENTATION = {
    'N': Orientation.North,
    'E': Orientation.East,
    'S': Orientation.South,
    'W': Orientation.West
}


class Ferry:
    def __init__(self):
        self._pos = Position()
        self._orientation = Orientation.East

    def get_pos(self) -> Position:
        return self._pos

    def execute_instructions(self, instructions: List[str]) -> None:
        for instruction in instructions:
            action = instruction[0]
            value = int(instruction[1:])

            self._execute_instruction(action, value)

    def _execute_instruction(self, action: str, value: int) -> None:
        if action == 'F':
            self._pos.move(self._orientation, value)
        elif action == 'R':
            self._orientation = self._orientation.rotate(right=value)
        elif action == 'L':
            self._orientation = self._orientation.rotate(left=value)
        elif action in STR_TO_ORIENTATION.keys():
            self._pos.move(STR_TO_ORIENTATION[action], value)


class FerryWithWaypoint(Ferry):
    def __init__(self):
        super().__init__()

        self._w_pos = Position(x=10, y=1)

    def _execute_instruction(self, action: str, value: int) -> None:
        if action == 'F':
            self._move_ferry(value)
        elif action == 'R':
            self._rotate_waypoint(right=value)
        elif action == 'L':
            self._rotate_waypoint(left=value)
        elif action in STR_TO_ORIENTATION.keys():
            self._w_pos.move(STR_TO_ORIENTATION[action], value)

    def _move_ferry(self, value: int) -> None:
        self._pos.x += value * self._w_pos.x
        self._pos.y += value * self._w_pos.y

    def _rotate_waypoint(self, left: int = 0, right: int = 0) -> None:
        if left > 0 and right > 0:
            raise Exception("Left or right??")

        num_rotations = 0

        if left > 0:
            num_rotations -= left // 90

        if right > 0:
            num_rotations = right // 90

        num_rotations %= 4

        if num_rotations == 1:
            self._w_pos = Position(self._w_pos.y, -self._w_pos.x)
        elif num_rotations == 2:
            self._w_pos = Position(-self._w_pos.x, -self._w_pos.y)
        elif num_rotations == 3:
            self._w_pos = Position(-self._w_pos.y, self._w_pos.x)
        else:
            raise Exception(f"num_rotations={num_rotations}")


def main():
    instruction = read_instructions()

    ferry = Ferry()
    ferry.execute_instructions(instruction)
    pos = ferry.get_pos()
    print(abs(pos.x) + abs(pos.y))

    ferry = FerryWithWaypoint()
    ferry.execute_instructions(instruction)
    pos = ferry.get_pos()
    print(abs(pos.x) + abs(pos.y))


if __name__ == '__main__':
    main()
