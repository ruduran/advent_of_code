import argparse


class BaseProcessor(object):
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        with open(self.filename) as f:
            jump_list = [int(l) for l in f]
            return self.number_of_jumps_to_get_out(jump_list)

    def number_of_jumps_to_get_out(self, jump_list):
        raise NotImplementedError()


def get_file_name():
    parser = argparse.ArgumentParser(description='Advent of Code Day 5')
    parser.add_argument('file', help='input file')
    args = parser.parse_args()
    return args.file
