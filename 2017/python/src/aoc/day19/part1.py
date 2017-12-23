#!/usr/bin/env python

from . import BaseProcessor


class Processor(BaseProcessor):
    def process(self):
        letters = ''
        while self.move():
            elem = self.get_elem(self.position)
            if str.isalpha(elem):
                letters += elem
        return letters


def main():
    processor = Processor()
    print(processor.process())


if __name__ == '__main__':
    main()
