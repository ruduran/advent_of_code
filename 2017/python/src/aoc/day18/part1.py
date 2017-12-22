#!/usr/bin/env python

from . import BaseProcessor, BaseProgram


class Program(BaseProgram):
    def __init__(self, instruction_list):
        super().__init__(instruction_list)

        self.played_sound = 0
        self.is_sound_recovered = False

    def snd(self, operand):
        self.played_sound = self.get_value(operand)

    def rcv(self, operand):
        cond = self.get_value(operand)
        if cond != 0:
            self.is_sound_recovered = True
        return True

    def run_until_sound_recovered(self):
        while not self.is_sound_recovered:
            self.run_instruction()

    @property
    def recovered_sound(self):
        if self.is_sound_recovered:
            return self.played_sound
        else:
            return None


class Processor(BaseProcessor):
    def __init__(self):
        super().__init__()
        self.program = Program(self.load_instruction_list())

    def process(self):
        self.program.run_until_sound_recovered()
        return self.program.recovered_sound


def main():
    processor = Processor()
    print(processor.process())


if __name__ == '__main__':
    main()
