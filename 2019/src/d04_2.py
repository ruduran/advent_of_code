from typing import List, Iterator

from common import get_file_name


def main():
    with open(get_file_name()) as file:
        input_range_string = file.readline()
        range_start, range_end = input_range_string.strip().split('-')

        possible_passwords: set = _get_possible_passwords(range_start, range_end)
        print(len(possible_passwords))


def _get_possible_passwords(range_start: str, range_end: str) -> set:
    range_start_digits = [int(d) for d in range_start]
    range_end_digits = [int(d) for d in range_end]
    discovered_passwords = _build_possible_passwords(range_start_digits,
                                                     range_end_digits,
                                                     length=6,
                                                     consecutives_needed=True)
    return set(discovered_passwords)


def _build_possible_passwords(range_start: List[int],
                              range_end: List[int],
                              length: int,
                              consecutives_needed: bool,
                              prev_digit: int = None,
                              range_skip: int = None) -> Iterator[str]:
    built_passwords = set()

    min_digit = max(range_start[0], prev_digit) if prev_digit is not None else range_start[0]
    available_range = range(min_digit, range_end[0]+1)

    if length == 1:
        if consecutives_needed:
            built_passwords = {prev_digit} if prev_digit in available_range and prev_digit != range_skip else set()
        else:
            built_passwords = set(str(d) for d in available_range if d != range_skip)
    else:
        for d in available_range:
            if length == 2 and consecutives_needed and d != prev_digit:
                built_passwords.add(''.join([str(d)]*2))
            else:
                subpass_need_consecutives = (consecutives_needed and d != prev_digit) or d == range_skip
                subpass_min_range = range_start[1:] if d == range_start[0] else [0]*(length-1)
                subpass_max_range = range_end[1:] if d == range_end[0] else [9]*(length-1)
                if d == range_skip or consecutives_needed and not subpass_need_consecutives:
                    subpass_range_skip = d
                else:
                    subpass_range_skip = None
                subpasswords = _build_possible_passwords(subpass_min_range,
                                                         subpass_max_range,
                                                         length=length-1,
                                                         consecutives_needed=subpass_need_consecutives,
                                                         prev_digit=d,
                                                         range_skip=subpass_range_skip)
                subpasswords_set = {str(d)+p for p in subpasswords}
                built_passwords |= subpasswords_set

    yield from built_passwords


if __name__ == '__main__':
    main()
