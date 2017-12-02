import unittest


class BaseProcessorTester(unittest.TestCase):
    def set_processor(self, processor_class):
        self.processor = processor_class('')

    def call_process_number_list(self, numbers_tests):
        for exp_sol, test_input in numbers_tests:
            count = self.processor.process_number_list(test_input)
            self.assertEqual(exp_sol, count)
