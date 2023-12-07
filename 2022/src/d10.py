from __future__ import annotations

import argparse

from argparse import Namespace
from typing import Generator, Iterator


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_instructions(file: str) -> Generator[str, None, None]:
    with open(file) as f:
        for line in f:
            if data := line.rstrip():
                yield data


def simulate(instructions: Iterator[str]) -> list[int]:
    cycles = [1]
    for m in instructions:
        match m.split():
            case ["noop"]:
                cycles.append(cycles[-1])
            case ["addx", value]:
                cycles.append(cycles[-1])
                cycles.append(cycles[-1] + int(value))

    return cycles


def render(cycles: list[int]) -> None:
    pixels = []
    for p in range(240):
        h_p = p % 40
        sprite_pos = cycles[p]
        if sprite_pos - 1 <= h_p <= sprite_pos + 1:
            pixels.append("#")
        else:
            pixels.append(".")

    for r in range(6):
        start_p = r*40
        print("".join(pixels[start_p:start_p+40]))


def main():
    args = parse_arguments()
    instructions = read_instructions(args.filename)
    cycles = simulate(instructions)
    print(20*cycles[19]+60*cycles[59]+100*cycles[99]+140*cycles[139]+180*cycles[179]+220*cycles[219])
    render(cycles)


if __name__ == "__main__":
    main()
