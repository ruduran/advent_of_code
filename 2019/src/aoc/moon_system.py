from copy import deepcopy
from functools import reduce
from itertools import chain
from math import gcd
from typing import List, Iterable, Tuple


def lcd(a: int, b: int) -> int:
    return a*b//gcd(a, b)


def ilcd(number_list: Iterable[int]) -> int:
    return reduce(lcd, number_list)


class MoonSystem:
    def __init__(self, moon_list: List[List[int]] = None):
        self._moon_velocity_list: List = [(deepcopy(p), [0, 0, 0]) for p in moon_list] if moon_list else {}

    def get_total_energy(self) -> int:
        total_energy = 0
        for position, velocity in self._moon_velocity_list:
            total_energy += sum(map(abs, position)) * sum(map(abs, velocity))

        return total_energy

    def iterate(self, times: int = 1):
        for i in range(times):
            self._apply_gravities()
            self._move()

    def find_period(self) -> int:
        first_occurrence = 0
        axis_statuses = [{self._build_axis_status(a): 0} for a in range(3)]
        period = [0]*3

        i = 1
        while not all(period):
            self.iterate()

            for a in range(3):
                if not period[a]:
                    status = self._build_axis_status(a)
                    if status in axis_statuses[a]:
                        first_occurrence = axis_statuses[a][status]
                        period[a] = i - first_occurrence
                    else:
                        axis_statuses[a][status] = i

            i += 1

        return ilcd(period) + first_occurrence

    def _build_axis_status(self, axis_num: int) -> Tuple:
        return tuple(chain([(p[axis_num], v[axis_num]) for p, v in self._moon_velocity_list]))

    def _apply_gravities(self):
        for position, velocity in self._moon_velocity_list:
            position_tuples = zip(*[p for p, _ in self._moon_velocity_list])
            for i, a in enumerate(position_tuples):
                velocity_change = 0
                for p in a:
                    if p > position[i]:
                        velocity_change += 1
                    if p < position[i]:
                        velocity_change -= 1

                velocity[i] += velocity_change

    def _move(self):
        for position, velocity in self._moon_velocity_list:
            for i, (p, v) in enumerate(zip(position, velocity)):
                position[i] = p + v
