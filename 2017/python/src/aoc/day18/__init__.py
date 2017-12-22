from collections import defaultdict

from aoc.utils import get_file_name


class Instruction(object):
    _instruction = ''
    _operand1 = ''
    _operand2 = ''

    def __init__(self, instruction_str):
        instruction_split = instruction_str.split()
        self._instruction = instruction_split[0]
        try:
            self._operand1 = int(instruction_split[1])
        except Exception:
            self._operand1 = instruction_split[1].strip()

        if len(instruction_split) > 2:
            try:
                self._operand2 = int(instruction_split[2])
            except Exception:
                self._operand2 = instruction_split[2].strip()

    @property
    def instruction(self):
        return self._instruction

    @property
    def operand1(self):
        return self._operand1

    @property
    def operand2(self):
        return self._operand2


class BaseProgram(object):
    def __init__(self, instruction_list):
        self.instruction_list = instruction_list

        self.inst_num = 0
        self.registers = defaultdict(int)

    def run_instruction(self):
        if self.inst_num < 0 or self.inst_num >= len(self.instruction_list):
            return False

        jump_offset = 1
        inst = self.instruction_list[self.inst_num]
        if inst.instruction == 'snd':
            self.snd(inst.operand1)
        elif inst.instruction == 'set':
            self.set(inst.operand1, inst.operand2)
        elif inst.instruction == 'add':
            self.add(inst.operand1, inst.operand2)
        elif inst.instruction == 'mul':
            self.mul(inst.operand1, inst.operand2)
        elif inst.instruction == 'mod':
            self.mod(inst.operand1, inst.operand2)
        elif inst.instruction == 'rcv':
            if not self.rcv(inst.operand1):
                return False
        elif inst.instruction == 'jgz':
            jump_offset = self.jgz(inst.operand1, inst.operand2)
        else:
            raise Exception('Unrecognized instruction')

        self.inst_num += jump_offset

        return True

    def snd(self, operand):
        raise NotImplementedError()

    def rcv(self, operand):
        raise NotImplementedError()

    def set(self, operand1, operand2):
        self.registers[operand1] = self.get_value(operand2)

    def add(self, operand1, operand2):
        self.registers[operand1] += self.get_value(operand2)

    def mul(self, operand1, operand2):
        self.registers[operand1] *= self.get_value(operand2)

    def mod(self, operand1, operand2):
        self.registers[operand1] %= self.get_value(operand2)

    def jgz(self, operand1, operand2):
        cond = self.get_value(operand1)
        if cond > 0:
            return self.get_value(operand2)

        return 1

    def get_value(self, value):
        if isinstance(value, int):
            return value
        else:
            return self.registers[value]


class BaseProcessor(object):

    def __init__(self):
        self.filename = get_file_name()

    def load_instruction_list(self):
        instruction_list = []
        with open(self.filename) as f:
            for line in f:
                instruction = Instruction(line.strip())
                instruction_list.append(instruction)
        return instruction_list
