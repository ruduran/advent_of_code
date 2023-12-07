from __future__ import annotations

import argparse
from argparse import Namespace
from dataclasses import dataclass
from functools import cached_property


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
class Card:
    id: int
    winning_numbers: set[int]
    numbers_on_card: set[int]

    @cached_property
    def winning_numbers_on_card(self) -> set[int]:
        return self.winning_numbers & self.numbers_on_card

    @property
    def points(self) -> int:
        return 1<<len(self.winning_numbers_on_card)-1 if self.winning_numbers_on_card else 0

    @classmethod
    def from_str(cls, raw: str) -> Card:
        raw_game, raw_numbers = raw.split(': ', 1)
        card_id = int(raw_game.split(" ")[-1])
        raw_winning, raw_numbers_on_card = raw_numbers.split('|', 1)
        winning_numbers = {int(n) for n in raw_winning.split()}
        numbers_on_card = {int(n) for n in raw_numbers_on_card.split()}
        return Card(id=card_id, winning_numbers=winning_numbers, numbers_on_card=numbers_on_card)


def parse_cards(data: list[str]) -> list[Card]:
    return [Card.from_str(line) for line in data]


def total_number_or_scratchcards(cards: list[Card]) -> int:
    card_copies = {c.id: 1 for c in cards}
    for c in cards:
        card_won = len(c.winning_numbers_on_card)
        for i in range(c.id+1, c.id+card_won+1):
            if i in card_copies:
                card_copies[i] += card_copies[c.id]

    return sum(card_copies.values())


def main():
    args = parse_arguments()
    file_content = read_raw_file(args.filename)
    cards = parse_cards(file_content)
    print(sum([c.points for c in cards]))

    print(total_number_or_scratchcards(cards))


if __name__ == "__main__":
    main()
