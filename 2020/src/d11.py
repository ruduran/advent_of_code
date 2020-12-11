from typing import List

from aoc2020.common import get_file_name


def read_seat_layout() -> List[List[str]]:
    rows = []
    with open(get_file_name()) as file:
        for line in file:
            if line:
                rows.append(list(line.strip()))

    return rows


def _num_occupied_adjacent(seat_layout, row, column) -> int:
    num_occupied = 0
    for r in (row - 1, row, row + 1):
        for c in (column - 1, column, column + 1):
            if r < 0 or c < 0 or r >= len(seat_layout) or c >= len(seat_layout[r]) or (r == row and c == column):
                continue

            if seat_layout[r][c] == '#':
                num_occupied += 1

    return num_occupied


def _iterate(seat_layout: List[List[str]]) -> List[List[str]]:
    new_seat_layout = []
    for row in range(len(seat_layout)):
        new_row = []
        for column in range(len(seat_layout[row])):
            current_status = seat_layout[row][column]
            num_occupied_adjacent = _num_occupied_adjacent(seat_layout, row, column)
            if current_status == 'L' and num_occupied_adjacent == 0:
                new_row.append('#')
            elif current_status == '#' and num_occupied_adjacent >= 4:
                new_row.append('L')
            else:
                new_row.append(current_status)

        new_seat_layout.append(new_row)
    return new_seat_layout


def simulate_seating(seat_layout: List[List[str]]) -> List[List[str]]:
    current_seat_layout = seat_layout
    everybody_seated = False
    while not everybody_seated:
        next_seat_layout = _iterate(current_seat_layout)
        if next_seat_layout == current_seat_layout:
            everybody_seated = True
        else:
            current_seat_layout = next_seat_layout

    return current_seat_layout


def _num_visible_occupied(seat_layout, row, column) -> int:
    num_occupied = 0
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            r = row
            c = column
            seat_or_end_found = False
            while not seat_or_end_found:
                r += x
                c += y
                if r < 0 or c < 0 or r >= len(seat_layout) or c >= len(seat_layout[r]) or (r == row and c == column):
                    seat_or_end_found = True
                else:
                    position_state = seat_layout[r][c]
                    if position_state in {'L', '#'}:
                        if position_state == '#':
                            num_occupied += 1

                        seat_or_end_found = True

    return num_occupied


def _iterate_weird(seat_layout: List[List[str]]) -> List[List[str]]:
    new_seat_layout = []
    for row in range(len(seat_layout)):
        new_row = []
        for column in range(len(seat_layout[row])):
            current_status = seat_layout[row][column]
            num_occupied_adjacent = _num_visible_occupied(seat_layout, row, column)
            if current_status == 'L' and num_occupied_adjacent == 0:
                new_row.append('#')
            elif current_status == '#' and num_occupied_adjacent >= 5:
                new_row.append('L')
            else:
                new_row.append(current_status)

        new_seat_layout.append(new_row)
    return new_seat_layout


def simulate_weird_seating(seat_layout: List[List[str]]) -> List[List[str]]:
    current_seat_layout = seat_layout
    everybody_seated = False
    while not everybody_seated:
        next_seat_layout = _iterate_weird(current_seat_layout)
        if next_seat_layout == current_seat_layout:
            everybody_seated = True
        else:
            current_seat_layout = next_seat_layout

    return current_seat_layout


def occupied_seats(seat_layout: List[List[str]]) -> int:
    return sum([sum([s == '#' for s in row]) for row in seat_layout])


def main():
    seat_layout = read_seat_layout()

    final_seating = simulate_seating(seat_layout)
    print(occupied_seats(final_seating))

    final_seating = simulate_weird_seating(seat_layout)
    print(occupied_seats(final_seating))


if __name__ == '__main__':
    main()
