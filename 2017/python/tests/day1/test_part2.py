import unittest

from aoc.day1.part2 import ProcessorP2


class TestProcessorP2(unittest.TestCase):
    def setUp(self):
        self.processor = ProcessorP2('')

    def test_process_number_list(self):
        tests = (
            (6, [1, 2, 1, 2]),
            (0, [1, 2, 2, 1]),
            (4, [1, 2, 3, 4, 2, 5]),
            (12, [1, 2, 3, 1, 2, 3]),
            (4, [1, 2, 1, 3, 1, 4, 1, 5]),
        )
        for exp_sol, test_input in tests:
            count = self.processor.process_number_list(test_input)
            self.assertEqual(exp_sol, count)
