import math
from typing import Tuple

from common import get_file_name
from aoc.asteroid_field import AsteroidField

NUM_OF_ASTEROIDS_TO_DESTROY = 200


def main():
    input_data = []
    with open(get_file_name()) as file:
        for line in file:
            input_data.append(list(line.strip()))

    asteroid_field = AsteroidField()
    asteroid_field.load(input_data)
    selected_location, asteroids_in_sight = asteroid_field.get_best_asteroid()
    print("Selected_location: {}".format(selected_location))
    print("Asteroids in sight: {}".format(len(asteroids_in_sight)))

    num_of_asteroids_to_destroy = NUM_OF_ASTEROIDS_TO_DESTROY
    while num_of_asteroids_to_destroy > len(asteroids_in_sight):
        asteroid_field.destroy(asteroids_in_sight)
        num_of_asteroids_to_destroy -= len(asteroids_in_sight)

        asteroids_in_sight = asteroid_field.get_asteroids_in_sight_from(selected_location)

    asteroids_with_degree_info = [(a, get_degree_info(selected_location, a)) for a in asteroids_in_sight]
    asteroids_by_destroy_order = sorted(asteroids_with_degree_info, key=destroy_order_key)

    last_asteroid_to_destroy, angle = asteroids_by_destroy_order[num_of_asteroids_to_destroy-1]
    result = 100*last_asteroid_to_destroy[0] + last_asteroid_to_destroy[1]
    print("{} at {:.2f}° -> {}".format(last_asteroid_to_destroy, angle, result))


def destroy_order_key(a):
    degree_a = a[1]

    if degree_a < 0:
        return abs(degree_a) + 90

    if degree_a <= 90:
        return abs(degree_a - 90)
    else:
        return abs(degree_a - 360) + 90


def get_degree_info(origin: Tuple[int, int], asteroid: Tuple[int, int]):
    o_x, o_y = origin
    a_x, a_y = asteroid
    return delta_to_degrees(a_x - o_x, o_y - a_y)


def delta_to_degrees(delta_x: int, delta_y: int):
    radians = math.atan2(delta_y, delta_x)
    return radians * 180 / math.pi


if __name__ == '__main__':
    main()
