import argparse


class BaseProcessor(object):
    def __init__(self):
        self.number = get_input_number()


def get_input_number():
    parser = argparse.ArgumentParser(description='Advent of Code Day 3')
    parser.add_argument('number', type=int, help='input number')
    args = parser.parse_args()
    return args.number
