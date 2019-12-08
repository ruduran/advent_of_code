from aoc.cable_panel import CablePanel
from common import get_file_name


def main():
    panel = CablePanel()

    with open(get_file_name()) as file:
        for line in file:
            panel.add_cable(line)

    print(panel.get_closest_collision_distance())


if __name__ == '__main__':
    main()
