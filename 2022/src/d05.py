import argparse
import re
from argparse import Namespace
from copy import deepcopy
from dataclasses import dataclass
from typing import TextIO

Stacks = dict[int, list[str]]


@dataclass
class Step:
    count: int
    orig: int
    dest: int


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def parse_stacks(f: TextIO) -> Stacks:
    raw_stacks = []
    stacks = Stacks()
    for line in f:
        if data := line.rstrip():
            raw_stacks.append(data)
        else:
            break

    stack_num_split = raw_stacks[-1].split()
    for stack_num in stack_num_split:
        position = raw_stacks[-1].find(stack_num)
        stack_i = int(stack_num)
        stacks[stack_i] = []
        for i in reversed(range(0, len(raw_stacks) - 1)):
            if position > len(raw_stacks[i]) or raw_stacks[i][position] == " ":
                break
            stacks[stack_i].append(raw_stacks[i][position])

    return stacks


def parse_step(raw_step: str) -> Step:
    if match := re.match(r"move (\d+) from (\d+) to (\d+)", raw_step):
        return Step(count=int(match[1]), orig=int(match[2]), dest=int(match[3]))

    raise Exception(f"Could not match step {raw_step}")


def read_input(file: str) -> tuple[Stacks, list[Step]]:
    with open(file) as f:
        stacks = parse_stacks(f)

        steps = []
        for l in f:
            if raw_step := l.strip():
                steps.append(parse_step(raw_step))

        return stacks, steps


def run(stacks: Stacks, steps: list[Step], reverse_on_move: bool) -> Stacks:
    new_stacks = deepcopy(stacks)
    for s in steps:
        to_move = new_stacks[s.orig][-s.count:]
        if reverse_on_move:
            to_move = reversed(to_move)
        new_stacks[s.dest].extend(to_move)
        new_stacks[s.orig] = new_stacks[s.orig][:-s.count]

    return new_stacks


def main():
    args = parse_arguments()
    stacks, steps = read_input(args.filename)

    new_stacks = run(stacks, steps, reverse_on_move=True)
    result = "".join([new_stacks[i][-1] for i in sorted(new_stacks.keys())])
    print(result)

    new_stacks = run(stacks, steps, reverse_on_move=False)
    result = "".join([new_stacks[i][-1] for i in sorted(new_stacks.keys())])
    print(result)


if __name__ == "__main__":
    main()
