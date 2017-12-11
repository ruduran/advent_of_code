#!/usr/bin/env python

from aoc.utils import get_file_name


class Position(object):
    def __init__(self, x=0, y=0):
        self._x = 0
        self._y = 0

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Processor(object):
    STEP_MAP = {
        'n': (0, 2),
        's': (0, -2),
        'ne': (1, 1),
        'nw': (-1, 1),
        'se': (1, -1),
        'sw': (-1, -1),
    }

    def __init__(self, filename):
        self.filename = filename
        self.child_path = []
        self.max_dist = 0

    def process(self):
        self.load_path()
        return (self.min_steps_to_child(), self.max_dist)

    def load_path(self):
        with open(self.filename) as f:
            line = f.readline().strip()
            self.child_path = line.split(',')

    def min_steps_to_child(self):
        child_position = self.relative_child_position()
        return self.min_steps_to_position(child_position)

    def relative_child_position(self):
        child_pos = Position()
        for step in self.child_path:
            step_dist = self.STEP_MAP.get(step)
            if not step_dist:
                raise Exception("Wrong step {}".format(step))

            child_pos.move(*step_dist)
            self.max_dist = max(self.max_dist,
                                self.min_steps_to_position(child_pos))

        return child_pos

    def min_steps_to_position(self, pos):
        x = abs(pos.x)
        y = abs(pos.y)
        if y > x:
            return x + int((y-x)/2)
        else:
            return y


def main():
    processor = Processor(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
