from typing import List

from aoc2020.common import get_file_name


class Seat:
    def __init__(self, code: str):
        self.code = code

    def get_id(self) -> int:
        return self._get_row() * 8 + self._get_column()

    def _get_row(self) -> int:
        return self._code_to_number(self.code[:7], 0, 127)

    def _get_column(self) -> int:
        return self._code_to_number(self.code[7:10], 0, 7)

    @staticmethod
    def _code_to_number(code: str, start: int, end: int) -> int:
        for c in code:
            if c in {'B', 'R'}:
                start += (end - start + 1) // 2
            elif c in {'F', 'L'}:
                end -= (end - start + 1) // 2
            else:
                raise Exception(c)
        return start


def read_seats() -> List[Seat]:
    seat_list = []
    with open(get_file_name()) as file:
        for line in file:
            if line:
                seat_list.append(Seat(line))
    return seat_list


def main():
    seats = read_seats()
    seat_id_set = {s.get_id() for s in seats}
    print(max(seat_id_set))

    full_plane_of_seats = range(min(seat_id_set), max(seat_id_set) + 1)
    empty_seats = set(full_plane_of_seats) - seat_id_set
    if len(empty_seats) == 1:
        print(empty_seats.pop())
    else:
        print("There is more than one empty seat!!")


if __name__ == '__main__':
    main()
