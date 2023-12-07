from math import prod
from typing import List, Tuple, Dict, Set

from aoc2020.common import get_file_name


FieldRules = Dict[str, Set[int]]


# TODO: Improve
def read_input() -> Tuple[FieldRules, List[int], List[List[int]]]:
    with open(get_file_name()) as file:
        fields = {}
        line = file.readline().strip()
        while line:
            line_split = line.split(": ")
            field_name = line_split[0]
            field_set = set()
            for range_str in line_split[1].split(" or "):
                range_split = range_str.split("-")
                field_set |= set(range(int(range_split[0]), int(range_split[1]) + 1))

            fields[field_name] = field_set
            line = file.readline().strip()

        file.readline()  # your ticket:
        your_ticket = [int(n) for n in file.readline().strip().split(",")]

        file.readline()  # empty:
        file.readline()  # nearby tickets:

        nearby_tickets = []
        line = file.readline().strip()
        while line:
            ticket = [int(n) for n in line.split(",")]
            nearby_tickets.append(ticket)
            line = file.readline().strip()

        return fields, your_ticket, nearby_tickets


class TicketProcessor:
    def __init__(self, rules: FieldRules) -> None:
        self._error_rate = 0
        self._field_rules = rules
        self._tickets = []

    def load_nearby_tickets(self, ticket_list: List[List[int]]) -> None:
        for ticket in ticket_list:
            valid = True
            for ticket_field in ticket:
                if not any([ticket_field in s for s in self._field_rules.values()]):
                    valid = False
                    self._error_rate += ticket_field

            if valid:
                self._tickets.append(ticket)

    def get_error_rate(self) -> int:
        return self._error_rate

    def foo(self, temp_mapping: Dict[str, Set[int]], rule, pos):
        if pos in temp_mapping[rule]:
            temp_mapping[rule].discard(pos)

            if len(temp_mapping[rule]) == 1:
                for field_name in temp_mapping.keys():
                    if field_name != rule:
                        self.foo(temp_mapping, field_name, list(temp_mapping[rule])[0])

    def get_field_position_mapping(self) -> Dict[str, int]:
        positions = len(self._tickets[0])
        temp_mapping = {name: set(range(positions)) for name in self._field_rules.keys()}

        for ticket in self._tickets:
            for pos, field in enumerate(ticket):
                for rule_name, rule_set in self._field_rules.items():
                    if pos in temp_mapping[rule_name]:
                        if field not in rule_set:
                            self.foo(temp_mapping, rule_name, pos)

        mapping = {}
        for field_name, positions in temp_mapping.items():
            if len(positions) > 1:
                raise Exception("Not enough information!")

            if len(positions) == 0:
                raise Exception(f"Not good pos for {field_name}!")

            mapping[field_name] = positions.pop()

        return mapping


def main():
    field_rules, ticket, nearby_tickets = read_input()

    processor = TicketProcessor(field_rules)
    processor.load_nearby_tickets(nearby_tickets)
    print(processor.get_error_rate())

    mapping = processor.get_field_position_mapping()
    print(mapping)
    product = prod([ticket[pos] for name, pos in mapping.items() if name.startswith("departure")])
    print(product)


if __name__ == '__main__':
    main()
