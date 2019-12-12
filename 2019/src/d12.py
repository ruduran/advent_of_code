import re

from aoc.moon_system import MoonSystem
from common import get_file_name


AXES = ['x', 'y', 'z']


def main():
    moon_re = re.compile(r"<x=(?P<x>-?\d+), *y=(?P<y>-?\d+), *z=(?P<z>-?\d+)>")
    moon_list = []
    with open(get_file_name()) as file:
        for line in file:
            moon_match = moon_re.match(line.strip())
            moon = [int(moon_match[a]) for a in AXES]
            moon_list.append(moon)

    moon_system = MoonSystem(moon_list)
    moon_system.iterate(times=1000)
    print("Total energy after 1000 iterations: {}".format(moon_system.get_total_energy()))

    moon_system = MoonSystem(moon_list)
    print("Iterations until first loop: {}".format(moon_system.find_period()))


if __name__ == '__main__':
    main()
