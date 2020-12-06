from typing import List

from aoc2020.common import get_file_name


class Seat:
    def __init__(self, code: str):
        self.code = code

    def get_id(self) -> int:
        return self._get_row() * 8 + self._get_column()

    def _get_row(self) -> int:
        min = 0
        max = 127
        for c in self.code[:7]:
            if c == 'B':
                min += (max - min + 1) // 2
            elif c == 'F':
                max -= (max - min + 1) // 2
            else:
                raise Exception(c)
        return min

    def _get_column(self) -> int:
        min = 0
        max = 7
        for c in self.code[7:10]:
            if c == 'R':
                min += (max - min + 1) // 2
            elif c == 'L':
                max -= (max - min + 1) // 2
            else:
                raise Exception(c)
        return min


def read_seats() -> List[Seat]:
    seat_list = []
    with open(get_file_name()) as file:
        for line in file:
            if line:
                seat_list.append(Seat(line))
    return seat_list


def main():
    seats = read_seats()
    seat_id_list = [s.get_id() for s in seats]
    print(max(seat_id_list))

    full_plane_of_seats = range(min(seat_id_list), max(seat_id_list) + 1)
    empty_seats = set(full_plane_of_seats) - set(seat_id_list)
    if len(empty_seats) == 1:
        print(empty_seats.pop())
    else:
        print("There is more than one empty seat!!")


if __name__ == '__main__':
    main()
