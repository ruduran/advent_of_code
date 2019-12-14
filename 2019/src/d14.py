from aoc.space_refinery import SpaceRefinery
from common import get_file_name


def main():
    refinery = SpaceRefinery()
    with open(get_file_name()) as file:
        input_data = file.read().splitlines()
        refinery.parse_reactions(input_data)

    print("Quantity of ORE needed for 1 FUEL: {}".format(refinery.get_ore_needed_for_fuel()))

    num_of_ores = 1000000000000
    print("FUEL produced with {} OREs: {}".format(num_of_ores, refinery.get_fuel_produced_with(num_of_ores)))


if __name__ == '__main__':
    main()
