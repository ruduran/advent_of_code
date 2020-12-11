from typing import List

from aoc2020.common import get_file_name


def read_seat_layout() -> List[List[str]]:
    rows = []
    with open(get_file_name()) as file:
        for line in file:
            if line:
                rows.append(list(line.strip()))

    return rows


class FerrySimulator:

    MIN_OCCUPIED_TO_LEAVE = 4

    def __init__(self, seat_layout: List[List[str]]) -> None:
        self._seat_layout = seat_layout

    def run(self) -> List[List[str]]:
        current_seat_layout = self._seat_layout
        seating_completed = False
        while not seating_completed:
            self._iterate()
            if self._seat_layout == current_seat_layout:
                seating_completed = True
            else:
                current_seat_layout = self._seat_layout

        return current_seat_layout

    def _iterate(self) -> None:
        new_seat_layout = []
        for row in range(len(self._seat_layout)):
            new_row = []
            for column in range(len(self._seat_layout[row])):
                current_status = self._seat_layout[row][column]
                num_occupied_adjacent = self._num_occupied_adjacent(row, column)
                if current_status == 'L' and num_occupied_adjacent == 0:
                    new_row.append('#')
                elif current_status == '#' and num_occupied_adjacent >= self.MIN_OCCUPIED_TO_LEAVE:
                    new_row.append('L')
                else:
                    new_row.append(current_status)
            new_seat_layout.append(new_row)

        self._seat_layout = new_seat_layout

    def _num_occupied_adjacent(self, row, column) -> int:
        num_occupied = 0
        for r in (row - 1, row, row + 1):
            for c in (column - 1, column, column + 1):
                out_of_bounds = r < 0 or c < 0 or r >= len(self._seat_layout) or c >= len(self._seat_layout[r])
                if out_of_bounds or (r == row and c == column):
                    continue

                if self._seat_layout[r][c] == '#':
                    num_occupied += 1

        return num_occupied


class FerrySimulatorWithVisibility(FerrySimulator):

    MIN_OCCUPIED_TO_LEAVE = 5

    def _num_occupied_adjacent(self, row, column) -> int:
        num_occupied = 0
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                r = row
                c = column
                seat_or_end_found = False
                while not seat_or_end_found:
                    r += x
                    c += y
                    out_of_bounds = r < 0 or c < 0 or r >= len(self._seat_layout) or c >= len(self._seat_layout[r])
                    if out_of_bounds or (r == row and c == column):
                        seat_or_end_found = True
                    else:
                        position_state = self._seat_layout[r][c]
                        if position_state in {'L', '#'}:
                            if position_state == '#':
                                num_occupied += 1

                            seat_or_end_found = True

        return num_occupied


def occupied_seats(seat_layout: List[List[str]]) -> int:
    return sum([sum([s == '#' for s in row]) for row in seat_layout])


def main():
    seat_layout = read_seat_layout()

    final_seating = FerrySimulator(seat_layout).run()
    print(occupied_seats(final_seating))

    final_seating = FerrySimulatorWithVisibility(seat_layout).run()
    print(occupied_seats(final_seating))


if __name__ == '__main__':
    main()
