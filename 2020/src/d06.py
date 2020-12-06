from typing import List, Set

from aoc2020.common import get_file_name


def read_answers() -> List[List[Set]]:
    answer_list = []
    with open(get_file_name()) as file:
        content = file.read()
        for raw_answer in content.split("\n\n"):
            group_answers = []
            for individual_answer in raw_answer.split('\n'):
                if individual_answer:
                    group_answers.append(set(individual_answer))
            answer_list.append(group_answers)
    return answer_list


def answers_any(group_answers: List[Set]) -> Set:
    return set.union(*group_answers)


def answers_all(group_answers: List[Set]) -> Set:
    return set.intersection(*group_answers)


def main():
    answers = read_answers()
    print(sum([len(answers_any(g)) for g in answers]))
    print(sum([len(answers_all(g)) for g in answers]))


if __name__ == '__main__':
    main()
