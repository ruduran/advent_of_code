from __future__ import annotations

import re
from dataclasses import dataclass
from functools import partial
from typing import List, Iterable, Tuple

from aoc2020.common import get_file_name


def valid_year(input_str: str, min_year: int, max_year: int):
    try:
        return len(input_str) == 4 and min_year <= int(input_str) <= max_year
    except ValueError:
        return False


def valid_height(input_str: str):
    unit = input_str[-2:]
    try:
        value = int(input_str[:-2])
    except ValueError:
        return False

    if unit == "cm":
        return 150 <= value <= 193
    elif unit == "in":
        return 59 <= value <= 76
    else:
        return False


@dataclass
class Passport(dict):
    VALID_PID_RE = re.compile(r"^\d{9}$")
    VALID_HCL_RE = re.compile(r"^#[0-9a-f]{6}$")
    VALID_COLORS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    VALIDATIONS = {
        "byr": partial(valid_year, min_year=1920, max_year=2002),
        "iyr": partial(valid_year, min_year=2010, max_year=2020),
        "eyr": partial(valid_year, min_year=2020, max_year=2030),
        "hgt": valid_height,
        "hcl": VALID_HCL_RE.match,
        "ecl": VALID_COLORS.__contains__,
        "pid": VALID_PID_RE.match}

    def __init__(self, data: Iterable[Tuple[str, str]]):
        super().__init__(data)

    @staticmethod
    def from_field_list(field_list: List[str]) -> Passport:
        return Passport([field.strip().split(":", maxsplit=1) for field in field_list])

    def has_all_the_required_fields(self) -> bool:
        return set(self.VALIDATIONS.keys()).issubset(self.keys())

    def is_valid(self) -> bool:
        for field, is_valid in self.VALIDATIONS.items():
            if field not in self.keys() or not is_valid(self[field]):
                return False

        return True


def read_passports() -> List[Passport]:
    password_list = []
    with open(get_file_name()) as file:
        content = file.read()
        for raw_pwd in content.split("\n\n"):
            fields = raw_pwd.replace('\n', ' ').split()
            password_list.append(Passport.from_field_list(fields))
    return password_list


def main():
    passwords = read_passports()
    print(sum([p.has_all_the_required_fields() for p in passwords]))
    print(sum([p.is_valid() for p in passwords]))


if __name__ == '__main__':
    main()
