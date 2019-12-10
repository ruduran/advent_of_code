from common import get_file_name
from aoc.asteroid_field import AsteroidField


def main():
    input_data = []
    with open(get_file_name()) as file:
        for line in file:
            input_data.append(list(line.strip()))

    asteroid_field = AsteroidField()
    asteroid_field.load(input_data)
    selected_location, asteroids_in_sight = asteroid_field.get_best_asteroid()
    print("Selected_location: {}".format(selected_location))
    print("Asteroids in sight: {}".format(asteroids_in_sight))


if __name__ == '__main__':
    main()
