import argparse
from argparse import Namespace


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


def read_raw_calibration_values(data: list[str]) -> list[list[int]]:
    return [[int(c) for c in line if c.isdigit()] for line in data]


def replace_first_and_last(text: str, to_replace: dict[str, str]) -> str:
    first_occurrence = {text.find(c): c for c in to_replace if c in text}
    if first_occurrence:
        position_to_replace = min(first_occurrence)
        first_digit_to_replace = first_occurrence[min(first_occurrence)]
        replacement = to_replace[first_digit_to_replace]
        text = text[0:position_to_replace] + replacement + text[position_to_replace+1:]

        last_occurrence = {text.rfind(c): c for c in to_replace if c in text}
        if last_occurrence:
            position_to_replace = max(last_occurrence)
            last_digit_to_replace = last_occurrence[position_to_replace]
            replacement = to_replace[last_digit_to_replace]
            text = text[0:position_to_replace] + replacement + text[position_to_replace+1:]

    return text


def replace_spelled_out_digits(data: list[str]) -> list[str]:
    to_replace = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    return [replace_first_and_last(line, to_replace) for line in data]


def main():
    args = parse_arguments()
    file_content = read_raw_file(args.filename)
    raw_calibration_values = read_raw_calibration_values(file_content)
    calibration_values = [v[0]*10 + v[-1] for v in raw_calibration_values if v]
    print(sum(calibration_values))

    replaced_content = replace_spelled_out_digits(file_content)
    raw_calibration_values = read_raw_calibration_values(replaced_content)
    calibration_values = [v[0] * 10 + v[-1] for v in raw_calibration_values]
    print(sum(calibration_values))


if __name__ == "__main__":
    main()
