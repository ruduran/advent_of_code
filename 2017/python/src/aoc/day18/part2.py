#!/usr/bin/env python

import queue

from . import BaseProcessor, BaseProgram


class Program(BaseProgram):
    def __init__(self, instruction_list, pid, queue_in, queue_out):
        super().__init__(instruction_list)

        self.set('p', pid)
        self.queue_in = queue_in
        self.queue_out = queue_out
        self.send_count = 0

    def snd(self, operand):
        self.queue_out.put(self.get_value(operand))
        self.send_count += 1

    def rcv(self, operand):
        try:
            value = self.queue_in.get_nowait()
            self.set(operand, value)
            return True
        except queue.Empty:
            return False


class Processor(BaseProcessor):
    def __init__(self):
        super().__init__()
        instruction_list = self.load_instruction_list()
        queue1 = queue.Queue()
        queue2 = queue.Queue()
        self.programs = [Program(instruction_list, 0, queue1, queue2),
                         Program(instruction_list, 1, queue2, queue1)]

    def process(self):
        while (self.programs[0].run_instruction() or
               self.programs[1].run_instruction()):
            pass
        return self.programs[1].send_count


def main():
    processor = Processor()
    print(processor.process())


if __name__ == '__main__':
    main()
