from common import get_file_name
from aoc.intcode.intcode_computer import IntcodeComputer


EXPECTED_OUTPUT = 19690720


def main():
    computer = IntcodeComputer()

    with open(get_file_name()) as file:
        memory_str = file.readline()
        program = [int(d) for d in memory_str.strip().split(",")]
        computer.load_memory(program)

    for noun in range(100):
        for verb in range(100):
            program[1] = noun
            program[2] = verb
            computer.load_memory(program)

            computer.run()

            result = computer.get_memory_position(0)

            if result == EXPECTED_OUTPUT:
                print(100*noun+verb)
                return


if __name__ == '__main__':
    main()
