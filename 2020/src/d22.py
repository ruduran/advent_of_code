from copy import deepcopy
from typing import Tuple, List
from aoc2020.common import get_file_name


def read_desks_info() -> Tuple[List[int], List[int]]:
    desk1 = []
    desk2 = []
    with open(get_file_name()) as file:
        desk = desk1
        for line in file:
            if line.startswith("Player 1"):
                desk = desk1
            elif line.startswith("Player 2"):
                desk = desk2
            else:
                line = line.strip()
                if line:
                    desk.append(int(line))

    return desk1, desk2


def play_game(orig_desk1: List[int], orig_desk2: List[int]) -> List[int]:
    desk1 = deepcopy(orig_desk1)
    desk2 = deepcopy(orig_desk2)
    while desk1 and desk2:
        card1 = desk1.pop(0)
        card2 = desk2.pop(0)

        if card1 > card2:
            desk1.extend([card1, card2])
        else:
            desk2.extend([card2, card1])

    return desk1 if desk1 else desk2


def winning_score(desk: List[int]) -> int:
    return sum([i*c for i, c in enumerate(reversed(desk), start=1)])


def play_recursive_game(desk1: List[int], desk2: List[int]) -> List[int]:
    _, winning_desk = _play_recursive_game(desk1, desk2)
    return winning_desk


def _play_recursive_game(desk1: List[int], desk2: List[int]) -> Tuple[int, List[int]]:
    played_rounds = set()
    while desk1 and desk2:
        current_round = (tuple(desk1), tuple(desk2))

        if current_round in played_rounds:
            return 1, desk1

        played_rounds.add(current_round)

        card1 = desk1.pop(0)
        card2 = desk2.pop(0)

        if len(desk1) >= card1 and len(desk2) >= card2:
            winner, winning_desk = _play_recursive_game(desk1[:card1], desk2[:card2])
            if winner == 1:
                desk1.extend([card1, card2])
            else:
                desk2.extend([card2, card1])
        else:
            if card1 > card2:
                desk1.extend([card1, card2])
            else:
                desk2.extend([card2, card1])

    return (1, desk1) if desk1 else (2, desk2)


def main():
    desk1, desk2 = read_desks_info()
    winning_desk = play_game(desk1, desk2)
    print(winning_score(winning_desk))

    winning_desk = play_recursive_game(desk1, desk2)
    print(winning_score(winning_desk))


if __name__ == '__main__':
    main()
