import re
from collections import defaultdict
from typing import Dict, Optional, Set

from aoc2020.common import get_file_name


class BidirectionalWeightedGraph:
    def __init__(self):
        self._dict = defaultdict(dict)
        self._inverse_dict = defaultdict(dict)

    def get(self, key: str) -> Optional[Dict[str, int]]:
        return self._dict.get(key, {})

    def inverse(self, key: str) -> Optional[Dict[str, int]]:
        return self._inverse_dict.get(key, {})

    def add(self, orig: str, dest: str, weight: int):
        self._dict[orig][dest] = weight
        self._inverse_dict[dest][orig] = weight


CONTAINING_BAG_RE = re.compile(r"(?P<number>\d+) (?P<bag>[ a-z]+) bag.*")


def read_rules() -> BidirectionalWeightedGraph:
    rules = BidirectionalWeightedGraph()
    with open(get_file_name()) as file:
        for line in file:
            if line:
                (bag, content) = line.split(" bags contain ")
                if not content.startswith("no"):
                    containing_bags = content.split(", ")
                    for containing_bag in containing_bags:
                        bag_match = CONTAINING_BAG_RE.match(containing_bag)
                        if bag_match:
                            rules.add(bag, bag_match["bag"], int(bag_match["number"]))

    return rules


def get_bags_that_can_contain(rules: BidirectionalWeightedGraph, bag: str) -> Set[str]:
    found_bags = set()
    new_bags = {bag}
    while new_bags:
        found_bags = found_bags.union(new_bags)
        current_bags = new_bags
        new_bags = set()
        for current_bag in current_bags:
            new_bags = new_bags.union(rules.inverse(current_bag).keys())

    found_bags.remove(bag)

    return found_bags


def get_num_of_contained_bags(rules: BidirectionalWeightedGraph, bag: str) -> int:
    num_contained = 0
    subbags = rules.get(bag)
    for subbag, num in subbags.items():
        num_contained += num
        num_contained += num * get_num_of_contained_bags(rules, subbag)
    return num_contained


def main():
    rules = read_rules()
    containing_bags = get_bags_that_can_contain(rules, "shiny gold")
    print(len(containing_bags))
    num_of_contained_bags = get_num_of_contained_bags(rules, "shiny gold")
    print(num_of_contained_bags)


if __name__ == '__main__':
    main()
