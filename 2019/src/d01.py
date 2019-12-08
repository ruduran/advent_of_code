from common import get_file_name


def input_gen():
    with open(get_file_name()) as f:
        for line in f:
            yield int(line)


def fuel_for_mass(mass):
    # return mass//3 - 2
    fuel = mass//3 - 2
    if fuel > 0:
        return fuel + fuel_for_mass(fuel)
    else:
        return 0


def fuel_calc(input_masses):
    for mass in input_masses:
        yield fuel_for_mass(mass)


def main():
    print(sum(fuel_calc(input_gen())))


if __name__ == '__main__':
    main()
