from __future__ import annotations

import argparse
from argparse import Namespace
from dataclasses import dataclass
from typing import Optional


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_raw_file(file: str) -> (tuple[int, int], list[str]):
    start_position = None
    content = []
    with open(file) as f:
        for line in f:
            data = line.strip()
            if data:
                content.append(data)

            if "S" in data:
                start_position = (len(content)-1, data.find("S"))

    if start_position is None:
        raise Exception("Could not find starting position.")

    return start_position, content


@dataclass
class Tile:
    next: tuple[int, int]
    prev: Optional[tuple[int, int]] = None


PIPES = "|-LJ/F"


def next_two_pos_for(raw_tile: str, pos: tuple[int, int]) -> (tuple[int, int], tuple[int, int]):
    r, c = pos
    match raw_tile:
        case "|":
            return (r-1, c), (r+1, c)
        case "-":
            return (r, c-1), (r, c+1)
        case "L":
            return (r-1, c), (r, c+1)
        case "J":
            return (r-1, c), (r, c-1)
        case "7":
            return (r+1, c), (r, c-1)
        case "F":
            return (r+1, c), (r, c+1)
        case _:
            raise Exception("This should not happen")


def find_loop(start_position: tuple[int, int], grid: list[str]) -> dict[tuple[int, int], Tile]:
    prev_pos = None
    pos = start_position
    loop = {}
    while True:
        r, c = pos
        raw_tile = grid[r][c]
        if raw_tile == "S":
            if r - 1 >= 0 and grid[r-1][c] in PIPES and pos in next_two_pos_for(grid[r-1][c], (r-1, c)):
                next_pos = (r - 1, c)
            elif r + 1 < len(grid) and grid[r + 1][c] in PIPES and pos in next_two_pos_for(grid[r+1][c], (r+1, c)):
                next_pos = (r + 1, c)
            elif c - 1 >= 0 and grid[r][c - 1] in PIPES and pos in next_two_pos_for(grid[r][c-1], (r, c-1)):
                next_pos = (r, c - 1)
            elif c + 1 < len(grid[r]) and grid[r][c + 1] in PIPES and pos in next_two_pos_for(grid[r][c+1], (r, c+1)):
                next_pos = (r, c + 1)
            else:
                raise Exception("Cannot detect pipe from 'S'")

            loop[pos] = Tile(next=next_pos)
            prev_pos = pos
            pos = next_pos
        else:
            next_pos_1, next_pos_2 = next_two_pos_for(raw_tile, pos)
            if next_pos_1 not in loop:
                loop[pos] = Tile(next=next_pos_1, prev=prev_pos)
                prev_pos = pos
                pos = next_pos_1
            elif next_pos_2 not in loop:
                loop[pos] = Tile(next=next_pos_2, prev=prev_pos)
                prev_pos = pos
                pos = next_pos_2
            else:
                break

    loop[pos] = Tile(next=start_position, prev=prev_pos)
    loop[start_position].prev = pos

    return loop


def raw_tile_from_tile(tile_pos: tuple[int, int], tile: Tile) -> str:
    r, c = tile_pos
    tile_set = {tile.next, tile.prev}
    if (r-1, c) in tile_set:
        if (r, c-1) in tile_set:
            return "J"
        elif (r+1, c) in tile_set:
            return "|"
        elif (r, c+1) in tile_set:
            return "L"
        else:
            raise Exception("This shouldn't happen")
    elif (r+1, c) in tile_set:
        if (r, c-1) in tile_set:
            return "7"
        elif (r, c+1) in tile_set:
            return "F"
        else:
            raise Exception("This shouldn't happen")
    elif (r, c-1) in tile_set and (r, c+1) in tile_set:
        return "-"
    else:
        raise Exception("This shouldn't happen")


def inside_outside_going_down(is_inside: bool, previous_raw_tile: str) -> bool:
    match previous_raw_tile:
        case "|":
            return is_inside
        case "-":
            return not is_inside
        case "L":
            return is_inside
        case "J":
            return not is_inside
        case "7":
            return not is_inside
        case "F":
            return is_inside
        case _:
            return is_inside


def inside_outside_going_right(is_inside: bool, previous_raw_tile: str) -> bool:
    match previous_raw_tile:
        case "|":
            return not is_inside
        case "-":
            return is_inside
        case "L":
            return not is_inside
        case "J":
            return not is_inside
        case "7":
            return is_inside
        case "F":
            return is_inside
        case _:
            return is_inside


def inside_outside_row(row_inx: int, row: str, is_inside: bool, loop: dict[tuple[int, int], Tile]) -> list[Optional[bool]]:
    bool_row = []
    for i, t in enumerate(row):
        if i > 0 and (row_inx, i-1) in loop:
            is_inside = inside_outside_going_right(is_inside, row[i-1])

        bool_row.append(is_inside if (row_inx, i) not in loop else None)
    return bool_row


def inside_outside_grid(grid: list[str], loop: dict[tuple[int, int], Tile]) -> list[list[Optional[bool]]]:
    io_grid = []
    is_inside = False
    for i, r in enumerate(grid):
        if i > 0 and (i-1, 0) in loop:
            is_inside = inside_outside_going_down(is_inside, grid[i-1][0])

        io_grid.append(inside_outside_row(i, r, is_inside, loop))

    return io_grid


def main():
    args = parse_arguments()
    start_position, grid = read_raw_file(args.filename)
    loop = find_loop(start_position, grid)
    print((len(loop)+1)//2)

    start_tile = loop[start_position]
    start_r, start_c = start_position
    grid[start_r] = grid[start_r].replace("S", raw_tile_from_tile(start_position, start_tile))

    io_grid = inside_outside_grid(grid, loop)
    print(sum(r.count(True) for r in io_grid))


if __name__ == "__main__":
    main()
