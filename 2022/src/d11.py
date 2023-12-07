from __future__ import annotations

import argparse
import operator

from argparse import Namespace
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Callable, Union


@dataclass
class Monkey:
    operation: Callable[[int, int], int]
    operand1: Union[str, int]
    operand2: Union[str, int]
    divisible_by: int
    throw_to: dict[bool, int]
    items: list[int] = field(default_factory=list)
    inspected_items: int = 0


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_monkeys(file: str) -> dict[int, Monkey]:
    monkeys = {}
    with open(file) as f:
        monkey_number = 0
        items = []
        operation = None
        operand1 = None
        operand2 = None
        divisible_by = None
        throw_to = {}
        for line in f:
            if data := line.strip():
                match data.split():
                    case ["Monkey", number]:
                        monkey_number = int(number[:-1])
                    case ["Starting", "items:", *str_items]:
                        items = [int(i.rstrip(",")) for i in str_items]
                    case ["Operation:", "new", "=", op1, op, op2]:
                        operation = operator.mul if op == "*" else operator.add
                        operand1 = op1 if op1 == "old" else int(op1)
                        operand2 = op2 if op2 == "old" else int(op2)
                    case ["Test:", "divisible", "by", number]:
                        divisible_by = int(number)
                    case ["If", boolean, "throw", "to", "monkey", number]:
                        condition = True if boolean == "true:" else False
                        throw_to[condition] = int(number)

            else:
                monkeys[monkey_number] = Monkey(
                    operation=operation,
                    operand1=operand1,
                    operand2=operand2,
                    divisible_by=divisible_by,
                    items=items,
                    throw_to=throw_to
                )

                monkey_number = 0
                items = []
                operation = None
                test = None
                throw_to = {}

        monkeys[monkey_number] = Monkey(
            operation=operation,
            operand1=operand1,
            operand2=operand2,
            divisible_by=divisible_by,
            items=items,
            throw_to=throw_to
        )

    return monkeys


def simulate(monkeys: dict[int, Monkey], cycles: int, worry_division=1) -> None:
    cycle_states = {}

    c = 0
    while c < cycles:
        monkeys_before_cycle = {n: deepcopy(m) for n, m in monkeys.items()}
        cycle_state = []
        for m in monkeys.values():
            monkey_state = []
            for i in m.items:
                m.inspected_items += 1

                op1 = i if m.operand1 == "old" else m.operand1
                op2 = i if m.operand2 == "old" else m.operand2
                new_i = m.operation(op1, op2) // worry_division
                divisible = new_i % m.divisible_by == 0
                dest_monkey = m.throw_to[divisible]
                monkeys[dest_monkey].items.append(new_i)

                monkey_state.append(divisible)

            m.items = []

            cycle_state.append(tuple(monkey_state))

        cycle_state = tuple(cycle_state)
        if prev_state := cycle_states.get(cycle_state):
            loop_start_cycle = prev_state["cycle"]
            cycle_diff = c - loop_start_cycle
            num_of_loops = (cycles - loop_start_cycle) // cycle_diff
            for n, m in prev_state["monkeys"].items():
                inspected_per_loop = monkeys_before_cycle[n].inspected_items - m.inspected_items
                monkeys[n].inspected_items = m.inspected_items + inspected_per_loop * num_of_loops
                monkeys[n].items = monkeys_before_cycle[n].items

            c += cycle_diff * (num_of_loops - 1)

            cycle_states = {}
        else:
            cycle_states[cycle_state] = {
                "cycle": c,
                "monkeys": monkeys_before_cycle
            }
            c += 1


def main():
    args = parse_arguments()
    monkeys = read_monkeys(args.filename)
    simulate(monkeys, 20, 3)
    sorted_monkeys = sorted(monkeys.values(), key=lambda m: m.inspected_items, reverse=True)
    print(sorted_monkeys[0].inspected_items * sorted_monkeys[1].inspected_items)
    #simulate(monkeys, 10000)
    #sorted_monkeys = sorted(monkeys.values(), key=lambda m: m.inspected_items, reverse=True)
    #print(sorted_monkeys[0].inspected_items * sorted_monkeys[1].inspected_items)


if __name__ == "__main__":
    main()
