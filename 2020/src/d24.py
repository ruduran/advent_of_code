from typing import List, Tuple, Set

from aoc2020.common import get_file_name


NEIGHBOR_COORD_MAP = {
    "e": (-2, 0),
    "se": (-1, -1),
    "sw": (1, -1),
    "w": (2, 0),
    "nw": (1, 1),
    "ne": (-1, 1),
}


def _parse_instruction(instruction_str: str) -> List[Tuple[int, int]]:
    parsed_instructions = []
    i = 0
    while i < len(instruction_str):
        parsed = NEIGHBOR_COORD_MAP.get(instruction_str[i])
        if parsed:
            parsed_instructions.append(parsed)
            i += 1
        else:
            parsed = NEIGHBOR_COORD_MAP[instruction_str[i:i+2]]
            parsed_instructions.append(parsed)
            i += 2

    return parsed_instructions


def read_instructions() -> List[List[Tuple[int, int]]]:
    instructions = []
    with open(get_file_name()) as file:
        for line in file:
            line = line.strip()
            if line:
                instructions.append(_parse_instruction(line))

    return instructions


def get_floor_info(instructions: List[List[Tuple[int, int]]]) -> Set[Tuple[int, int]]:
    floor = set()
    for instruction in instructions:
        pos = (0, 0)
        for neighbor in instruction:
            pos = (pos[0] + neighbor[0], pos[1] + neighbor[1])

        if pos in floor:
            floor.remove(pos)
        else:
            floor.add(pos)

    return floor


def _get_num_black_neighbors(floor: Set[Tuple[int, int]], tile: Tuple[int, int]) -> int:
    neighbors = {(tile[0]+n[0], tile[1]+n[1]) for n in NEIGHBOR_COORD_MAP.values()}
    return len(floor & neighbors)


def get_next_floor(floor: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    min_x = min(t[0] for t in floor)
    max_x = max(t[0] for t in floor)
    min_y = min(t[1] for t in floor)
    max_y = max(t[1] for t in floor)

    next_floor = set()
    for x in range(min_x-2, max_x+3):
        for y in range(min_y-1, max_y+2):
            tile = (x, y)
            neighbors_num = _get_num_black_neighbors(floor, tile)
            if tile in floor:
                if neighbors_num in {1, 2}:
                    next_floor.add(tile)
            else:
                if neighbors_num == 2:
                    next_floor.add(tile)

    return next_floor


def main():
    instructions = read_instructions()
    floor = get_floor_info(instructions)
    black_tiles = len(floor)
    print(black_tiles)

    for _ in range(100):
        floor = get_next_floor(floor)

    black_tiles = len(floor)
    print(black_tiles)


if __name__ == '__main__':
    main()
