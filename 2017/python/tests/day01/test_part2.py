from . import BaseProcessorTester

from aoc.day01.part2 import Processor


class TestProcessorP2(BaseProcessorTester):
    def setUp(self):
        self.set_processor(Processor)

    def test_process_number_list(self):
        tests = (
            (6, [1, 2, 1, 2]),
            (0, [1, 2, 2, 1]),
            (4, [1, 2, 3, 4, 2, 5]),
            (12, [1, 2, 3, 1, 2, 3]),
            (4, [1, 2, 1, 3, 1, 4, 1, 5]),
        )
        self.call_process_number_list(tests)
