#!/usr/bin/env python

from . import BaseProcessor


class Processor(BaseProcessor):
    def calculate_steps(self):
        if self.number == 1:
            return 0

        current_number = 1
        side_size = 0
        while current_number < self.number:
            side_size += 2
            current_number += 4 * side_size

        x, y = self.calc_distance(side_size)
        return x + y

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


def main():
    processor = Processor()
    print(processor.calculate_steps())


if __name__ == '__main__':
    main()
