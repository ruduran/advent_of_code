import argparse


class BaseProcessor(object):
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        with open(self.filename) as f:
            line = f.readline().strip()
            numbers = [int(c) for c in line]
            return self.process_number_list(numbers)

    def process_number_list(self, numbers):
        raise NotImplementedError()


def get_file_name():
    parser = argparse.ArgumentParser(description='Advent of Code Day 1')
    parser.add_argument('file', help='input file')
    args = parser.parse_args()
    return args.file
