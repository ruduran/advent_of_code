from __future__ import annotations

import argparse
from argparse import Namespace
from dataclasses import dataclass
from enum import Enum
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


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


CARD_ORDER = "23456789TJQKA"
CARD_ORDER_WITH_JOKER = "J23456789TQKA"


def lt_card(first: str, second: str, order: str = CARD_ORDER) -> bool:
    return order.find(first) < order.find(second)


@dataclass
class Hand:
    cards: str
    bid: int

    with_joker = False

    @cached_property
    def type(self) -> HandType:
        card_set = set(self.cards)
        num_diff_cards = len(card_set)
        match num_diff_cards:
            case 1:
                return HandType.FIVE_OF_A_KIND
            case 2:
                for c in card_set:
                    if self.cards.count(c) == 4:
                        return HandType.FOUR_OF_A_KIND
                else:
                    return HandType.FULL_HOUSE
            case 3:
                for c in card_set:
                    if self.cards.count(c) == 3:
                        return HandType.THREE_OF_A_KIND
                else:
                    return HandType.TWO_PAIR
            case 4:
                return HandType.ONE_PAIR
            case _:
                return HandType.HIGH_CARD

    @cached_property
    def type_with_joker(self) -> HandType:
        card_set = set(self.cards)
        num_diff_cards = len(card_set)
        num_of_jokers = self.cards.count("J")
        match num_diff_cards:
            case 1:
                return HandType.FIVE_OF_A_KIND
            case 2:
                for c in card_set:
                    if self.cards.count(c) == 4:
                        if num_of_jokers:
                            return HandType.FIVE_OF_A_KIND

                        return HandType.FOUR_OF_A_KIND
                else:
                    if num_of_jokers == 1:
                        return HandType.FOUR_OF_A_KIND
                    elif num_of_jokers:
                        return HandType.FIVE_OF_A_KIND

                    return HandType.FULL_HOUSE
            case 3:
                for c in card_set:
                    if self.cards.count(c) == 3:
                        if num_of_jokers:
                            return HandType.FOUR_OF_A_KIND

                        return HandType.THREE_OF_A_KIND
                else:
                    if num_of_jokers == 1:
                        return HandType.FULL_HOUSE
                    elif num_of_jokers:
                        return HandType.FOUR_OF_A_KIND

                    return HandType.TWO_PAIR
            case 4:
                if num_of_jokers:
                    return HandType.THREE_OF_A_KIND

                return HandType.ONE_PAIR
            case _:
                if num_of_jokers:
                    return HandType.ONE_PAIR
                return HandType.HIGH_CARD

    def __lt__(self, other: Hand) -> bool:
        if self.with_joker:
            if self.type_with_joker != other.type_with_joker:
                return self.type_with_joker.value < other.type_with_joker.value
        else:
            if self.type != other.type:
                return self.type.value < other.type.value

        for i in range(5):
            if self.cards[i] != other.cards[i]:
                if self.with_joker:
                    return lt_card(self.cards[i], other.cards[i], order=CARD_ORDER_WITH_JOKER)
                else:
                    return lt_card(self.cards[i], other.cards[i])

        return False


def parse_hands(data: list[str]) -> list[Hand]:
    hands = []
    for line in data:
        cards, str_bid = line.split()
        hands.append(Hand(cards=cards, bid=int(str_bid)))

    return hands


def main():
    args = parse_arguments()
    file_content = read_raw_file(args.filename)
    hands = parse_hands(file_content)

    sorted_hands = sorted(hands)
    winnings = sum(sorted_hands[i].bid * (i+1) for i in range(len(hands)))
    print(winnings)

    for h in hands:
        h.with_joker = True
    sorted_hands = sorted(hands)
    winnings = sum(sorted_hands[i].bid * (i + 1) for i in range(len(hands)))
    print(winnings)


if __name__ == "__main__":
    main()
