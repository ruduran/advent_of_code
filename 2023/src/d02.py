from __future__ import annotations

import argparse
from argparse import Namespace
from dataclasses import dataclass


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def read_raw_file(file: str) -> list[str]:
    content = []
    with open(file) as f:
        for line in f:
            data = line.strip()
            if data:
                content.append(data)
    return content


@dataclass
class Set:
    red: int
    green: int
    blue: int

    @property
    def power(self) -> int:
        return self.red * self.green * self.blue

    def contains(self, other: Set) -> bool:
        return self.red >= other.red and self.green >= other.green and self.blue >= other.blue

    @classmethod
    def from_str(cls, raw: str) -> Set:
        colors = {}
        for raw_color in raw.split(", "):
            quantity, name = raw_color.split(" ", 1)
            colors[name] = int(quantity)

        return Set(red=colors.get("red", 0), green=colors.get("green", 0), blue=colors.get("blue", 0))


@dataclass
class Game:
    id: int
    sets: list[Set]

    @property
    def guessed_set(self) -> Set:
        guess = Set(0, 0, 0)
        for s in self.sets:
            guess.red = max(guess.red, s.red)
            guess.green = max(guess.green, s.green)
            guess.blue = max(guess.blue, s.blue)
        return guess

    @classmethod
    def from_str(cls, raw: str) -> Game:
        raw_game, raw_sets = raw.split(': ', 1)
        game_id = int(raw_game.split(" ")[-1])
        sets = [Set.from_str(raw_set) for raw_set in raw_sets.split("; ")]
        return Game(id=game_id, sets=sets)


def parse_games(data: list[str]) -> list[Game]:
    return [Game.from_str(line) for line in data]


def main():
    args = parse_arguments()
    file_content = read_raw_file(args.filename)
    games = parse_games(file_content)

    available = Set(red=12, green=13, blue=14)
    possible = [g for g in games if available.contains(g.guessed_set)]
    print(sum([p.id for p in possible]))
    print(sum([g.guessed_set.power for g in games]))


if __name__ == "__main__":
    main()
