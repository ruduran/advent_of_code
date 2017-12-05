from . import BaseProcessorTester

from aoc.day01.part1 import Processor


class TestProcessorP1(BaseProcessorTester):
    def setUp(self):
        self.set_processor(Processor)

    def test_process_number_list(self):
        tests = (
            (3, [1, 1, 2, 2]),
            (4, [1, 1, 1, 1]),
            (0, [1, 2, 3, 4]),
            (9, [9, 1, 2, 1, 2, 1, 2, 9]),
        )
        self.call_process_number_list(tests)
