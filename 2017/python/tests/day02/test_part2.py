import unittest

from aoc.day02.part2 import ProcessorP2


class TestProcessorP2(unittest.TestCase):
    def setUp(self):
        self.processor = ProcessorP2('')

    def test_calc_checksum(self):
        test_input = [
            [5, 9, 2, 8],
            [9, 4, 7, 3],
            [3, 8, 6, 5]
        ]
        expected_checksum = 9

        checksum = self.processor._calc_checksum(test_input)
        self.assertEqual(expected_checksum, checksum)
