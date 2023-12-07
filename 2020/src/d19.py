from typing import Tuple, List, Dict, Any, Set
from aoc2020.common import get_file_name


def _process_sub_rule_str(sub_rule_str: str) -> Tuple[Any, ...]:
    sub_rule_split = sub_rule_str.split(' ')
    return tuple(int(e) if e.isnumeric() else e[1] for e in sub_rule_split)


def read_messages_info() -> Tuple[Dict[int, Tuple[Tuple[Any, ...]]], List[str]]:
    with open(get_file_name()) as file:
        rules = {}
        messages = []
        for line in file:
            line = line.strip()
            if line:
                if line[0].isnumeric():
                    line_split = line.split(': ')
                    rule_num = int(line_split[0])
                    sub_rules_str = line_split[1].split(' | ')
                    rules[rule_num] = tuple(_process_sub_rule_str(sub_rule_str) for sub_rule_str in sub_rules_str)
                else:
                    messages.append(line)
    return rules, messages


def generate_possibilities(rules: Dict[int, Tuple[Tuple[Any, ...]]], rule_num: int = 0) -> Set[str]:
    possibilities = set()
    for sub_rule in rules[rule_num]:
        sub_possibilities = set()
        for elem in sub_rule:
            if type(elem) is int:
                element_possibilities = generate_possibilities(rules, elem)
            else:
                element_possibilities = {elem}

            if sub_possibilities:
                new_sub_possibilities = set()
                for sub_possibility in sub_possibilities:
                    for element_possibility in element_possibilities:
                        new_sub_possibilities.add(sub_possibility + element_possibility)
                sub_possibilities = new_sub_possibilities
            else:
                sub_possibilities = element_possibilities

        possibilities |= sub_possibilities

    return possibilities


def follows_rules(rules: Dict[int, Tuple[Tuple[Any, ...]]], message: str) -> bool:
    leftovers = _follows_rules(rules, [message], 0)
    return '' in leftovers


def _follows_rules(rules: Dict[int, Tuple[Tuple[Any, ...]]], messages: List[str], rule_num: int = 0) -> List[str]:
    if not messages:
        return []

    leftovers = []
    for sub_rule in rules[rule_num]:
        remaining_messages = messages
        for elem in sub_rule:
            if type(elem) is int:
                remaining_messages = _follows_rules(rules, [m for m in remaining_messages if m], elem)
            else:
                remaining_messages = [m[1:] for m in remaining_messages if m[0] == elem]

        leftovers.extend(remaining_messages)

    return leftovers


def main():
    rules, messages = read_messages_info()
    possibilities = generate_possibilities(rules)
    print(sum(m in possibilities for m in messages))

    rules[8] = ((42,), (42, 8))
    rules[11] = ((42, 31), (42, 11, 31))
    print(sum(follows_rules(rules, m) for m in messages))


if __name__ == '__main__':
    main()
