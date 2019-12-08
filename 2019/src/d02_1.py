from common import get_file_name
from aoc.intcode.intcode_computer import IntcodeComputer


def main():
    computer = IntcodeComputer()

    with open(get_file_name()) as file:
        memory_str = file.readline()
        program = [int(d) for d in memory_str.strip().split(",")]
        computer.load_memory(program)

    program[1] = 12
    program[2] = 2
    computer.load_memory(program)

    computer.run()

    print(computer.get_memory_position(0))


if __name__ == '__main__':
    main()
