from aoc.utils import get_file_name


class BaseProcessor(object):

    DIRECTIONS = {
        'UP': {'x': 0, 'y': -1},
        'DOWN': {'x': 0, 'y': 1},
        'LEFT': {'x': -1, 'y': 0},
        'RIGHT': {'x': 1, 'y': 0},
    }

    def __init__(self):
        self.filename = get_file_name()
        self.network = []
        self.position = {'x': 0, 'y': 0}
        self.direction = 'DOWN'

        self.load_input()

    def get_elem(self, pos):
        try:
            return self.network[pos['x']][pos['y']]
        except Exception:
            return ''

    def load_input(self):
        network = []
        with open(self.filename) as f:
            for line in f:
                network.append(list(line))
        self.network = network

        self.position['y'] = self.network[0].index('|')

    def move(self):
        if not self.can_continue(self.direction):
            if self.direction in {'UP', 'DOWN'}:
                if self.can_continue('LEFT'):
                    self.direction = 'LEFT'
                elif self.can_continue('RIGHT'):
                    self.direction = 'RIGHT'
                else:
                    return False
            else:
                if self.can_continue('UP'):
                    self.direction = 'UP'
                elif self.can_continue('DOWN'):
                    self.direction = 'DOWN'
                else:
                    return False

        self.position = self.next_pos(self.direction)
        return True

    def next_pos(self, direction):
        next_pos = self.position.copy()
        movement = self.DIRECTIONS[direction]
        next_pos['x'] += movement['x']
        next_pos['y'] += movement['y']
        return next_pos

    def can_continue(self, direction):
        next_elem = self.get_elem(self.next_pos(direction))
        return str.isalpha(next_elem) or next_elem in {'|', '-', '+'}
