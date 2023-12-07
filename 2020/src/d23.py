from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple

from aoc2020.common import get_file_name


@dataclass
class Cup:
    value: int
    next: Optional[Cup]


class CupsGame:
    def __init__(self, cup_values: List[int]):
        self._directory = {c: Cup(value=c, next=None) for c in cup_values}

        for i, c in enumerate(cup_values[:-1]):
            self._directory[c].next = self._directory[cup_values[i+1]]
        self._directory[cup_values[-1]].next = self._directory[cup_values[0]]
        self._current = self._directory[cup_values[0]]

    def play(self, turns: int):
        for _ in range(turns):
            saved = self._current.next
            self._current.next = saved.next.next.next

            destination_value = self._current.value - 1
            saved_values = {saved.value, saved.next.value, saved.next.next.value}
            while destination_value in saved_values or destination_value not in self._directory:
                destination_value -= 1
                if destination_value not in self._directory:
                    destination_value = max(self._directory.keys())

            destination_cup = self._directory[destination_value]
            saved.next.next.next = destination_cup.next
            destination_cup.next = saved

            self._current = self._current.next

    def get_layout(self) -> List[int]:
        int_layout = []
        cup = self._directory[1].next
        while cup.value != 1:
            int_layout.append(cup.value)
            cup = cup.next
        return int_layout

    def return_two_after_one(self) -> Tuple[int, int]:
        cup_one = self._directory[1]
        return cup_one.next.value, cup_one.next.next.value


def read_input() -> List[int]:
    with open(get_file_name()) as file:
        raw_input = file.readline().strip()
        return [int(n) for n in raw_input]


def extend_cups(cups: List[int]) -> List[int]:
    max_value = max(cups)
    num_to_generate = 1000000 - len(cups)
    return cups + list(range(max_value + 1, num_to_generate + max_value + 1))


def main():
    input_cups = read_input()

    game = CupsGame(input_cups)
    game.play(100)
    layout = game.get_layout()
    print(''.join(str(c) for c in layout))

    extended_cups = extend_cups(input_cups)
    game = CupsGame(extended_cups)
    game.play(10000000)
    c1, c2 = game.return_two_after_one()
    print(c1*c2)


if __name__ == '__main__':
    main()
