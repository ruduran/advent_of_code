from typing import List, Tuple

from aoc2020.common import get_file_name


PREAMBLE = 25


def read_data() -> List[int]:
    data = []
    with open(get_file_name()) as file:
        for line in file:
            if line:
                data.append(int(line))

    return data


def not_2_entries_that_sum(entries_sum: int, data: List[int]) -> bool:
    for i, e in enumerate(data[:-1]):
        if entries_sum - e in data[i+1:]:
            return False

    return True


def first_not_sum_of_two_before(data: List[int]) -> Tuple[int, int]:
    for i in range(PREAMBLE, len(data)):
        value = data[i]
        if not_2_entries_that_sum(value, data[i-PREAMBLE:i]):
            return i, value
    raise Exception("Not found!")


def find_encryption_weakness(data: List[int], value: int) -> int:
    for i in range(0, len(data)-1):
        for j in range(i+1, len(data)):
            if sum(data[i:j]) == value:
                return min(data[i:j]) + max(data[i:j])

    raise Exception("Not found!")


def main():
    data = read_data()
    index, found_value = first_not_sum_of_two_before(data)
    print(found_value)
    weakness = find_encryption_weakness(data[:index], found_value)
    print(weakness)


if __name__ == '__main__':
    main()
