from __future__ import annotations

import argparse
import re
from argparse import Namespace
from dataclasses import dataclass
from itertools import product
from math import lcm


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_raw_file(file: str) -> list[str]:
    content = []
    with open(file) as f:
        for line in f:
            data = line.strip()
            if data:
                content.append(data)
    return content


@dataclass
class Node:
    left: str
    right: str


def parse_input(data: list[str]) -> (str, dict[Node]):
    instructions = data[0]

    node_re = re.compile(r"(?P<src>\w{3}) = \((?P<left>\w{3}), (?P<right>\w{3})\)")

    nodes = {}
    for line in data[1:]:
        m = node_re.match(line)
        nodes[m["src"]] = Node(left=m["left"], right=m["right"])

    return instructions, nodes


def num_of_steps(instructions: str, nodes: dict[Node], src="AAA", dst="ZZZ") -> int:
    steps = 0
    node = src
    while True:
        for i in instructions:
            steps += 1
            node = nodes[node].right if i == "R" else nodes[node].left

            if node == dst:
                return steps


def num_of_steps_til_loop(instructions: str, nodes: dict[Node], src: str, find_condition=lambda n: n[-1] == "Z") -> list[int]:
    find_locations = set()
    steps = 0
    step_list = []
    node = src
    while True:
        for p, i in enumerate(instructions):
            steps += 1
            node = nodes[node].right if i == "R" else nodes[node].left
            if find_condition(node):
                step_list.append(steps)
                find_location = (p, node)
                if find_location in find_locations:
                    return step_list
                else:
                    find_locations.add(find_location)


def num_of_simultaneous_steps(instructions: str, nodes: dict[Node], start_condition=lambda n: n[-1] == "A"):
    src_nodes = [n for n in nodes if start_condition(n)]
    list_of_num_of_step_lists = []
    for node in src_nodes:
        list_of_num_of_step_lists.append(num_of_steps_til_loop(instructions, nodes, node))

    # We have a list (loop) of the steps needed per node to reach a "Z"
    # Generate all the possible combinations and get the smallest lcm of the steps
    # to get the first time they get there simultaneously
    return min(lcm(*p) for p in (product(*list_of_num_of_step_lists)))


def main():
    args = parse_arguments()
    file_content = read_raw_file(args.filename)
    instructions, nodes = parse_input(file_content)

    # print(num_of_steps(instructions, nodes))
    print(num_of_simultaneous_steps(instructions, nodes))


if __name__ == "__main__":
    main()
