from functools import lru_cache
from typing import Dict, List, Tuple

from aoc2020.common import get_file_name


def read_adapters() -> List[int]:
    adapters = []
    with open(get_file_name()) as file:
        for line in file:
            if line:
                adapters.append(int(line))

    return adapters


def connect_all_adapters(adapters: List[int]) -> Dict[int, int]:
    current = 0
    diffs = {1: 0, 2: 0, 3: 1}
    for ad in sorted(adapters):
        diff = ad - current
        if diff <= 0:
            raise Exception(f"{ad} <= {current}")

        if diff > 3:
            raise Exception(f"The diff is too high: {diff}")

        current = ad
        diffs[diff] += 1

    return diffs


@lru_cache(maxsize=None)
def _generate_combinations(adapters: Tuple[int]) -> int:
    if len(adapters) <= 2:
        return 1

    combinations = _generate_combinations(adapters[1:])
    if adapters[2] - adapters[0] <= 3:
        combinations += _generate_combinations(adapters[2:])

    if len(adapters) > 3 and adapters[3] - adapters[0] <= 3:
        combinations += _generate_combinations(adapters[3:])

    return combinations


def generate_combinations(adapters: List[int]) -> int:
    sorted_adapters = sorted(adapters + [0, max(adapters) + 3])
    return _generate_combinations(tuple(sorted_adapters))


def main():
    adapters = read_adapters()
    adapters_diff_info = connect_all_adapters(adapters)
    print(f"{adapters_diff_info[1]}x{adapters_diff_info[3]}={adapters_diff_info[1]*adapters_diff_info[3]}")
    print(generate_combinations(adapters))


if __name__ == '__main__':
    main()
