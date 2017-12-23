#!/usr/bin/env python

from . import BaseProcessor


class Processor(BaseProcessor):
    def process(self):
        steps = 1
        while self.move():
            steps += 1
        return steps


def main():
    processor = Processor()
    print(processor.process())


if __name__ == '__main__':
    main()
