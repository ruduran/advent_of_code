#!/usr/bin/env python

from . import BaseProcessor


DIRECTIONS = {
    'UP': {'x': 0, 'y': 1},
    'DOWN': {'x': 0, 'y': -1},
    'LEFT': {'x': -1, 'y': 0},
    'RIGHT': {'x': 1, 'y': 0},
}


class Processor(BaseProcessor):
    def __init__(self):
        super().__init__()

        self.spiral = {(0, 0): 1}
        self.curr_number = 1
        self.next_pos = {'x': 1, 'y': 0}
        self.direction = 'UP'

    def find_first_larger(self):
        while self.number >= self.curr_number:
            self.generate_next_number()
            self.move_to_next_pos()
            self.change_direction_if_needed()
        return self.curr_number

    def generate_next_number(self):
        x = self.next_pos['x']
        y = self.next_pos['y']
        num = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                num += self.spiral.get((i, j), 0)
        self.spiral[(x, y)] = num
        self.curr_number = num

    def move_to_next_pos(self):
        movement = DIRECTIONS[self.direction]
        self.next_pos['x'] += movement['x']
        self.next_pos['y'] += movement['y']

    def change_direction_if_needed(self):
        neighbor = self.next_pos.copy()
        if self.direction == 'UP':
            neighbor['x'] -= 1
        if self.direction == 'DOWN':
            neighbor['x'] += 1
        if self.direction == 'LEFT':
            neighbor['y'] -= 1
        if self.direction == 'RIGHT':
            neighbor['y'] += 1

        neighbor_value = self.spiral.get((neighbor['x'], neighbor['y']))
        if neighbor_value is None:
            if self.direction == 'UP':
                self.direction = 'LEFT'
            elif self.direction == 'DOWN':
                self.direction = 'RIGHT'
            elif self.direction == 'LEFT':
                self.direction = 'DOWN'
            elif self.direction == 'RIGHT':
                self.direction = 'UP'


def main():
    processor = Processor()
    print(processor.find_first_larger())


if __name__ == '__main__':
    main()
