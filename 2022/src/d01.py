import argparse
from argparse import Namespace


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_elfs_calories(file: str) -> list[list[int]]:
    calorie_list_per_elf = []
    with open(file) as f:
        calorie_list = []
        for line in f:
            data = line.strip()
            if data:
                calorie_list.append(int(data))
            else:
                calorie_list_per_elf.append(calorie_list)
                calorie_list = []

        if calorie_list:
            calorie_list_per_elf.append(calorie_list)
    return calorie_list_per_elf


def main():
    args = parse_arguments()
    calorie_list_per_elf = read_elfs_calories(args.filename)
    calories_per_elf = [sum(cl) for cl in calorie_list_per_elf]
    sorted_elf_calories = sorted(calories_per_elf, reverse=True)

    print(sorted_elf_calories[0])
    print(sum(sorted_elf_calories[:3]))


if __name__ == "__main__":
    main()
