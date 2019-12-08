from common import get_file_name
from aoc.orbit_map import OrbitMap


def main():
    orbit_map = OrbitMap()

    orbit_list = []
    with open(get_file_name()) as file:
        for line in file:
            orbited, orbiter = line.strip().split(')')
            orbit_list.append((orbited, orbiter))
    orbit_map.load_orbit_map(orbit_list)

    print(orbit_map.get_total_number_or_orbits())


if __name__ == '__main__':
    main()
