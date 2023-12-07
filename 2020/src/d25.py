from typing import Tuple

from aoc2020.common import get_file_name


SUBJECT_NUMBER = 7
MOD_VALUE = 20201227


def get_card_and_door_pks() -> Tuple[int, int]:
    with open(get_file_name()) as file:
        card_pk = int(file.readline().strip())
        door_pk = int(file.readline().strip())
        return card_pk, door_pk


def loop(subject: int, times: int, value: int = 1) -> int:
    for _ in range(times):
        value *= subject
        value %= MOD_VALUE

    return value


def find_loop_size(pk: int) -> int:
    size = 0
    value = 1

    while value != pk:
        value = loop(SUBJECT_NUMBER, 1, value)
        size += 1

    return size


def main():
    card_pk, door_pk = get_card_and_door_pks()
    door_loop_size = find_loop_size(door_pk)
    encryption_key = loop(card_pk, door_loop_size)
    print(encryption_key)


if __name__ == '__main__':
    main()
