from common import get_file_name
from aoc.painting_robot import PaintingRobot


def main():
    robot = PaintingRobot()

    with open(get_file_name()) as file:
        memory_str = file.readline()
        program = [int(d) for d in memory_str.strip().split(",")]

    robot.load_program(program)
    robot.run()
    print(len(robot.get_painted_cells()))

    robot = PaintingRobot(initial_color=1)
    robot.load_program(program)
    robot.run()

    image = robot.get_board_as_image()
    image.render()


if __name__ == '__main__':
    main()
