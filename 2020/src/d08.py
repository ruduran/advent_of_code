from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from typing import List

from aoc2020.common import get_file_name


class Operation(str, Enum):
    ACC = "acc"
    JMP = "jmp"
    NOP = "nop"


@dataclass
class Instruction:
    operation: Operation
    argument: int


def read_instructions() -> List[Instruction]:
    instructions = []
    with open(get_file_name()) as file:
        for line in file:
            if line:
                (op, arg) = line.split()
                instructions.append(Instruction(operation=op, argument=int(arg)))

    return instructions


class HandheldProcessor:
    def __init__(self):
        self._instructions = []
        self._acc = 0
        self._cursor = 0

    def reset(self):
        self._acc = 0
        self._cursor = 0

    def load_instructions(self, instructions: List[Instruction]):
        self._instructions = instructions
        self.reset()

    def get_acc(self) -> int:
        return self._acc

    def run_until_loop(self):
        run_instructions = set()
        while self._cursor not in run_instructions:
            run_instructions.add(self._cursor)
            instruction = self._instructions[self._cursor]
            self._run_instruction(instruction)

    def _run_instruction(self, instruction: Instruction):
        if instruction.operation == Operation.ACC:
            self._acc += instruction.argument
            self._cursor += 1
        elif instruction.operation == Operation.JMP:
            self._cursor += instruction.argument
        elif instruction.operation == Operation.NOP:
            self._cursor += 1

    def run_until_done(self):
        saved_states = []
        run_instructions = set()
        changed_already = False
        while self._cursor < len(self._instructions):
            if self._cursor in run_instructions:
                (self._acc, self._cursor, run_instructions) = saved_states.pop()
                changed_already = True
                instruction = deepcopy(self._instructions[self._cursor])
                if instruction.operation == Operation.NOP:
                    instruction.operation = Operation.JMP
                else:  # JMP
                    instruction.operation = Operation.NOP
            else:
                instruction = self._instructions[self._cursor]
                if instruction.operation in {Operation.NOP, Operation.JMP} and not changed_already:
                    saved_states.append((self._acc, self._cursor, deepcopy(run_instructions)))

            run_instructions.add(self._cursor)
            self._run_instruction(instruction)


def main():
    instructions = read_instructions()
    processor = HandheldProcessor()
    processor.load_instructions(instructions)
    processor.run_until_loop()
    print(processor.get_acc())

    processor.reset()
    processor.run_until_done()
    print(processor.get_acc())


if __name__ == '__main__':
    main()
