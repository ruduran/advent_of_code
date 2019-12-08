from collections import defaultdict
from typing import List, Tuple


class OrbitMap:
    def __init__(self):
        self._map = defaultdict(set)

    def load_orbit_map(self, individual_orbits_list: List[Tuple[str, str]]):
        for orbited, orbiter in individual_orbits_list:
            self._map[orbited].add(orbiter)

    def transfers(self, o1, o2):
        path_to_o1 = self._get_path_to(o1)
        path_to_o2 = self._get_path_to(o2)

        path_diff = set(path_to_o1) ^ set(path_to_o2)
        return len(path_diff) - 2

    def _get_path_to(self, destination, start_from="COM"):
        orbiters = self._map[start_from]
        for orbiter in orbiters:
            if orbiter == destination:
                return [orbiter]

            path = self._get_path_to(destination, orbiter)
            if path:
                return path + [orbiter]

        return []

    def get_total_number_or_orbits(self):
        return self._get_total_number_of_orbits("COM", 0)

    def _get_total_number_of_orbits(self, start_from, distance_to_the_origin):
        orbits_num = distance_to_the_origin

        orbiters = self._map[start_from]
        for orbiter in orbiters:
            orbits_num += self._get_total_number_of_orbits(orbiter, distance_to_the_origin+1)

        return orbits_num
