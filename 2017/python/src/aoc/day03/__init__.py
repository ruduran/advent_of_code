import argparse


class BaseProcessor(object):
    def __init__(self, number):
        self.number = number

    def calculate_steps(self):
        if self.number == 1:
            return 0

        current_number = 1
        side_size = 0
        while current_number < self.number:
            side_size += 2
            current_number += 4 * side_size

        x, y = self.calc_distance(side_size)
        return self._calc_steps(x, y)

    def calc_distance(self, side_size):
        prev_max_number = (side_size - 1) ** 2
        number_pos_on_level = self.number - prev_max_number
        side_num = int(number_pos_on_level / side_size)

        if side_num == 4:
            return (side_size, side_size)

        number_pos_on_side = number_pos_on_level % side_size
        if side_num % 2 == 0:
            x_dist = int(side_size / 2)
            y_dist = self.calc_dist_to_side_center(side_size,
                                                   number_pos_on_side)
        else:
            x_dist = self.calc_dist_to_side_center(side_size,
                                                   number_pos_on_side)
            y_dist = int(side_size / 2)

        return (x_dist, y_dist)

    def calc_dist_to_side_center(self, side_size, num_on_side):
        half_side = int(side_size / 2)
        if num_on_side == half_side:
            dist = 0
        elif num_on_side < half_side:
            dist = half_side - num_on_side
        else:
            dist = num_on_side - half_side
        return dist

    def _calc_steps(self, x_dist, y_dist):
        raise NotImplementedError()


def get_input_number():
    parser = argparse.ArgumentParser(description='Advent of Code Day 3')
    parser.add_argument('number', type=int, help='input number')
    args = parser.parse_args()
    return args.number
