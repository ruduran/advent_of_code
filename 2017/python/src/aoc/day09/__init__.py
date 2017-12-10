#!/usr/bin/env python

from aoc.utils import get_file_name


class Processor(object):
    def __init__(self, filename):
        self.filename = filename
        self.score = 0
        self.garbage_chars = 0

    def process(self):
        self.load_data()
        return (self.score, self.garbage_chars)

    def load_data(self):
        with open(self.filename) as f:
            for line in f:
                self.process_line(line.strip())

    def process_line(self, line):
        level = 1
        garbage = False
        line_iter = iter(line)
        for c in line_iter:
            if c == '!':
                next(line_iter)
            elif c == '>':
                garbage = False
            elif garbage:
                self.garbage_chars += 1
            elif c == '<':
                garbage = True
            elif c == '{':
                self.score += level
                level += 1
            elif c == '}':
                level -= 1


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
