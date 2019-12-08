from unittest import TestCase

from aoc.intcode.intcode_computer import IntcodeComputer


class TestIntcodeComputer(TestCase):
    def setUp(self) -> None:
        self.computer = IntcodeComputer()

    def test_run_opcode_in_memory_ops(self):
        subtests = [
            ("addition", [1, 0, 0, 3, 99], 3, 2),
            ("multiplication", [2, 0, 0, 3, 99], 3, 4)
        ]
        for name, program, output_addr, expected_value in subtests:
            with self.subTest(name):
                # given
                self.computer.load_memory(program)

                # when
                result = self.computer.run_instruction()

                # then
                self.assertTrue(result)
                self.assertEqual(expected_value, self.computer.get_memory_position(output_addr))

    def test_final_opcode(self):
        # given
        self.computer.load_memory([99])

        # when
        result = self.computer.run_instruction()

        # then
        self.assertFalse(result)
