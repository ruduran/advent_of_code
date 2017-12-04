import argparse


class BaseProcessor(object):
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        total_valid = 0
        with open(self.filename) as f:
            for line in f:
                if self.is_passphrase_valid(line.strip()):
                    total_valid += 1
        return total_valid

    def is_passphrase_valid(self, passphrase):
        raise NotImplementedError()


def get_file_name():
    parser = argparse.ArgumentParser(description='Advent of Code Day 4')
    parser.add_argument('file', help='input file')
    args = parser.parse_args()
    return args.file
