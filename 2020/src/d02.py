from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Callable

from aoc2020.common import get_file_name


@dataclass
class PasswordInfo:
    password: str
    num_1: int
    num_2: int
    letter: str

    PASSWORD_INFO_RE = re.compile(r"(?P<num_1>\d+)-(?P<num_2>\d+) (?P<letter>\w): (?P<password>\w+)")

    @staticmethod
    def from_str(input_str: str) -> PasswordInfo:
        match = PasswordInfo.PASSWORD_INFO_RE.match(input_str)
        return PasswordInfo(
            password=match["password"],
            letter=match["letter"],
            num_1=int(match["num_1"]),
            num_2=int(match["num_2"])
        )


def read_password_list() -> List[PasswordInfo]:
    with open(get_file_name()) as file:
        return [PasswordInfo.from_str(line) for line in file]


def get_valid_password_num(password_list: List[PasswordInfo], check_password: Callable[[PasswordInfo], bool]) -> int:
    valid_passwords = 0
    for password in password_list:
        if check_password(password):
            valid_passwords += 1

    return valid_passwords


def is_valid_password_1(pw_info: PasswordInfo) -> bool:
    count = pw_info.password.count(pw_info.letter)
    return pw_info.num_1 <= count <= pw_info.num_2


def is_valid_password_2(pw_info: PasswordInfo) -> bool:
    pos_1 = pw_info.num_1 - 1
    pos_2 = pw_info.num_2 - 1
    return (pw_info.password[pos_1] == pw_info.letter) ^ (pw_info.password[pos_2] == pw_info.letter)


def main():
    passwords = read_password_list()
    print(get_valid_password_num(passwords, is_valid_password_1))
    print(get_valid_password_num(passwords, is_valid_password_2))


if __name__ == '__main__':
    main()
