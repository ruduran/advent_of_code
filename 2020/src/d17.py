from typing import List, Tuple, Set

from aoc2020.common import get_file_name


class Board:
    def __init__(self, flat_raw_board: List[str], dimensions: int = 3) -> None:
        self._dimensions = dimensions
        self._min_pos = [0] * dimensions
        self._max_pos = [0] * dimensions
        self._max_pos[0] = len(flat_raw_board) - 1
        self._max_pos[1] = len(flat_raw_board[0]) - 1

        self._board = set()

        position = [0] * dimensions
        for x, line in enumerate(flat_raw_board):
            for y, c in enumerate(line):
                alive = c == '#'
                if alive:
                    position[0] = x
                    position[1] = y
                    self._board.add(tuple(position))

    def num_active(self) -> int:
        return len(self._board)

    def iterate(self):
        self._board, self._min_pos, self._max_pos = self._iterate()

    def _iterate(self, already_built_pos: Tuple[int, ...] = ()) -> Tuple[Set[Tuple[int, ...]], List[int], List[int]]:
        new_board = set()
        new_min_pos = [0] * self._dimensions
        new_max_pos = [0] * self._dimensions
        dimension = len(already_built_pos)
        if dimension == self._dimensions:
            num_neighbours = self._get_num_neighbours(already_built_pos)
            cube_active = already_built_pos in self._board
            if cube_active and num_neighbours in {2, 3} or num_neighbours == 3:
                new_board.add(already_built_pos)
                new_min_pos = list(already_built_pos)
                new_max_pos = list(already_built_pos)
        else:
            for coord in range(self._min_pos[dimension] - 1, self._max_pos[dimension] + 2):
                partial_board, partial_min_pos, partial_max_pos = self._iterate(already_built_pos + (coord,))
                new_board |= partial_board
                for dim in range(self._dimensions):
                    new_min_pos[dim] = min(new_min_pos[dim], partial_min_pos[dim])
                    new_max_pos[dim] = max(new_max_pos[dim], partial_max_pos[dim])

        return new_board, new_min_pos, new_max_pos

    def _get_num_neighbours(self, cube_pos: Tuple[int, ...], already_built_neighbour_pos: Tuple[int, ...] = ()) -> int:
        num_found = 0
        dimension = len(already_built_neighbour_pos)
        if dimension == self._dimensions:
            if cube_pos != already_built_neighbour_pos and already_built_neighbour_pos in self._board:
                num_found += 1
        else:
            for d in (-1, 0, 1):
                coord = cube_pos[dimension] + d
                num_found += self._get_num_neighbours(cube_pos, already_built_neighbour_pos + (coord,))

        return num_found


def read_input() -> List[str]:
    with open(get_file_name()) as file:
        return [line.strip() for line in file]


def main():
    input_board = read_input()

    board = Board(input_board)
    for i in range(6):
        board.iterate()
    print(board.num_active())

    board = Board(input_board, dimensions=4)
    for i in range(6):
        board.iterate()
    print(board.num_active())


if __name__ == '__main__':
    main()
