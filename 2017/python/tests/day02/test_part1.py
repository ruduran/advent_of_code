import unittest

from aoc.day02.part1 import Processor


class TestProcessorP1(unittest.TestCase):
    def setUp(self):
        self.processor = Processor('')

    def test_calc_checksum(self):
        test_input = [
            [5, 1, 9, 5],
            [7, 5, 3],
            [2, 4, 6, 8]
        ]
        expected_checksum = 18

        checksum = self.processor._calc_checksum(test_input)
        self.assertEqual(expected_checksum, checksum)
