from math import prod
from typing import List

from aoc2020.common import get_file_name


AreaMap = List[str]


def read_map() -> AreaMap:
    trajectory_map = []
    with open(get_file_name()) as file:
        for line in file:
            trajectory_map.append(line.strip())
    return trajectory_map


def num_of_collisions(area_map: AreaMap, slope_x: int, slope_y: int) -> int:
    x = y = collisions = 0
    while y < len(area_map) - slope_y:
        y += slope_y
        x += slope_x
        x %= len(area_map[y])

        if area_map[y][x] == '#':
            collisions += 1

    return collisions


def slope_study(area_map: AreaMap) -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod([num_of_collisions(area_map, x, y) for (x, y) in slopes])


def main():
    trajectory_map = read_map()

    print(num_of_collisions(trajectory_map, 3, 1))
    print(slope_study(trajectory_map))


if __name__ == '__main__':
    main()
