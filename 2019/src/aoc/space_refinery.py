from collections import defaultdict
from math import ceil
from typing import Dict, List


class SpaceRefinery:
    def __init__(self):
        self._reactions: Dict[str, Dict] = {}

    def parse_reactions(self, input_data: List[str]):
        for reaction_str in input_data:
            consume_str, produce_str = reaction_str.split(" => ")
            output_chemical, output_quantity = self._parse_chemical_str(produce_str)
            input_chemicals = [self._parse_chemical_str(c) for c in consume_str.split(",")]
            self._reactions[output_chemical] = {"inputs": input_chemicals, "output_quantity": output_quantity}

    def get_ore_needed_for_fuel(self, fuel_units: int = 1) -> int:
        quantities_needed = defaultdict(int, [(r, c*fuel_units) for r, c in self._reactions["FUEL"]["inputs"]])
        reactors_needed = set(quantities_needed) - {"ORE"}
        while reactors_needed:
            reactor = reactors_needed.pop()
            quantity = quantities_needed[reactor]

            if quantity > 0:
                reactor_info: Dict = self._reactions[reactor]
                generated_quantity = reactor_info["output_quantity"]

                num_of_reaction_needed = ceil(quantity / generated_quantity)
                quantities_needed[reactor] -= generated_quantity * num_of_reaction_needed

                reactors_needed_for_reaction = reactor_info["inputs"]
                for r, q in reactors_needed_for_reaction:
                    quantities_needed[r] += q * num_of_reaction_needed

                reactors_needed = set(quantities_needed) - {"ORE"}

        return quantities_needed["ORE"]

    def get_fuel_produced_with(self, num_of_ores: int):
        min_f = num_of_ores // self.get_ore_needed_for_fuel(1)
        max_f = min_f * 2
        while self.get_ore_needed_for_fuel(max_f) < num_of_ores:
            min_f = max_f
            max_f *= 2

        while min_f < max_f:
            middle = 1 + (max_f + min_f) // 2
            ores_for_middle = self.get_ore_needed_for_fuel(middle)
            if ores_for_middle <= num_of_ores:
                min_f = middle
            else:
                max_f = middle - 1

        return min_f

    @staticmethod
    def _parse_chemical_str(chemical_str: str):
        quantity, name = chemical_str.strip().split(" ")
        return name, int(quantity)
