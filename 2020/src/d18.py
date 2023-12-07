from typing import List, Tuple, Set
from operator import add, mul
from aoc2020.common import get_file_name


OPERATORS = {'*', '+'}


def process_operation(operation: str, immediate_ops: Set[str]) -> int:
    result, _ = _process_operation(operation, immediate_ops)
    return result


def _process_operation(operation: str, immediate_ops: Set[str]) -> Tuple[int, int]:
    operands = []
    operators = []
    i = 0
    while i < len(operation):
        c = operation[i]
        if c == ')':
            break
        elif c in ' ':
            i += 1
        elif c in OPERATORS:
            operators.append(c)
            i += 1
        else:
            if c == '(':
                result, index_delta = _process_operation(operation[i+1:], immediate_ops)
                operands.append(result)
                i += index_delta + 1
            else:
                operands.append(int(c))
                i += 1

            if operators and operators[-1] in immediate_ops:
                op = operators.pop()
                op_fn = add if op == '+' else mul
                o1 = operands.pop()
                o2 = operands.pop()
                operands.append(op_fn(o1, o2))

    while operators:
        op = operators.pop()
        op_fn = add if op == '+' else mul
        o1 = operands.pop()
        o2 = operands.pop()
        operands.append(op_fn(o1, o2))

    return operands.pop(), i+1


def read_input() -> List[str]:
    with open(get_file_name()) as file:
        return [line.strip() for line in file]


def main():
    input_operations = read_input()

    total = 0
    for operation in input_operations:
        result = process_operation(operation, OPERATORS)
        total += result
    print(total)

    total = 0
    for operation in input_operations:
        result = process_operation(operation, {'+'})
        total += result
    print(total)


if __name__ == '__main__':
    main()
