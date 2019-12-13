from common import get_file_name
from aoc.arcade_cabinet import ArcadeCabinet


def main():

    with open(get_file_name()) as file:
        program_str = file.readline()
        program = [int(d) for d in program_str.strip().split(",")]

    arcade = ArcadeCabinet()
    arcade.load_game(program)
    arcade.run()
    print("Number of initial blocks: {}".format(arcade.get_num_of_blocks()))

    free_arcade = ArcadeCabinet(free_play=True)
    free_arcade.load_game(program)
    free_arcade.run()
    assert free_arcade.get_num_of_blocks() == 0, "There are blocks left"
    print("Final score: {}".format(free_arcade.get_score()))


if __name__ == '__main__':
    main()
