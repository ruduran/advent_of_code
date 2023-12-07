import argparse
from argparse import Namespace
from enum import Enum


class Option(Enum):
    Rock = "Rock"
    Paper = "Paper"
    Scissors = "Scissors"

    def __gt__(self, other):
        return (self == Option.Rock and other == Option.Scissors or
                self == Option.Paper and other == Option.Rock or
                self == Option.Scissors and other == Option.Paper)


selection_to_points = {
    Option.Rock: 1,
    Option.Paper: 2,
    Option.Scissors: 3,
}


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_instructions(file: str) -> list[tuple[str, str]]:
    instructions = []
    with open(file) as f:
        for line in f:
            data = line.strip()
            if data:
                o, p = data.split(" ")
                instructions.append((o, p))
    return instructions


def play_v1(instructions: list[tuple[str, str]]) -> int:
    points = 0
    for round in instructions:
        opponent = {"A": Option.Rock, "B": Option.Paper, "C": Option.Scissors}[round[0]]
        selection = {"X": Option.Rock, "Y": Option.Paper, "Z": Option.Scissors}[round[1]]

        points += selection_to_points[selection]

        if selection == opponent:
            points += 3
        elif selection > opponent:
            points += 6

    return points


def play_v2(instructions: list[tuple[str, str]]) -> int:
    points = 0
    for round in instructions:
        opponent = {"A": Option.Rock, "B": Option.Paper, "C": Option.Scissors}[round[0]]
        if round[1] == "X":
            selection = {Option.Rock: Option.Scissors, Option.Paper: Option.Rock, Option.Scissors: Option.Paper}[opponent]
        elif round[1] == "Y":
            points += 3
            selection = opponent
        else:  # Z
            points += 6
            selection = {Option.Rock: Option.Paper, Option.Paper: Option.Scissors, Option.Scissors: Option.Rock}[opponent]

        points += selection_to_points[selection]

    return points


def main():
    args = parse_arguments()
    input = read_instructions(args.filename)
    print(play_v1(input))
    print(play_v2(input))


if __name__ == "__main__":
    main()
