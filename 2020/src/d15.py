from typing import List

from aoc2020.common import get_file_name


def read_input() -> List[int]:
    with open(get_file_name()) as file:
        input_split = file.readline().strip().split(',')
        return [int(s) for s in input_split]


class ElvesGame:
    def __init__(self, initial_numbers: List[int]) -> None:
        self._number_turn = {n: i for i, n in enumerate(initial_numbers, start=1)}
        self._turns = len(initial_numbers) + 1
        self._next_number = 0

    def count_till(self, turn: int) -> int:
        for t in range(self._turns, turn):
            previous_turn = self._number_turn.get(self._next_number)

            self._number_turn[self._next_number] = t

            if previous_turn is None:
                self._next_number = 0
            else:
                self._next_number = t - previous_turn

        self._turns = turn

        return self._next_number


def main():
    input_numbers = read_input()
    game = ElvesGame(input_numbers)
    print(game.count_till(2020))
    print(game.count_till(30000000))


if __name__ == '__main__':
    main()
