import unittest

from aoc.day1.part1 import ProcessorP1


class TestProcessorP1(unittest.TestCase):
    def setUp(self):
        self.processor = ProcessorP1('')

    def test_process_number_list(self):
        tests = (
            (3, [1, 1, 2, 2]),
            (4, [1, 1, 1, 1]),
            (0, [1, 2, 3, 4]),
            (9, [9, 1, 2, 1, 2, 1, 2, 9]),
        )
        for exp_sol, test_input in tests:
            count = self.processor.process_number_list(test_input)
            self.assertEqual(exp_sol, count)
