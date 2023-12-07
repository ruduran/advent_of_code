from typing import List

from aoc2021.common import get_file_name


def read_input() -> List[int]:
    with open(get_file_name()) as file:
        return [int(line) for line in file]


def num_increased_elements(element_list: List[int]) -> int:
    current = element_list[0]
    num_increased = 0
    for n in element_list[1:]:
        if n > current:
            num_increased += 1

        current = n

    return num_increased


def main():
    input_list = read_input()
    sliding_window_list = list(map(sum, zip(input_list[:-2], input_list[1:-1], input_list[2:])))

    print(num_increased_elements(input_list))
    print(num_increased_elements(sliding_window_list))


if __name__ == '__main__':
    main()
