from dataclasses import dataclass
from math import prod
from typing import List

from aoc2020.common import get_file_name


@dataclass
class BusInfo:
    id: int
    num: int


@dataclass
class ShuttleSearchInput:
    earliest_ts: int
    bus_list: List[BusInfo]


def read_input() -> ShuttleSearchInput:
    with open(get_file_name()) as file:
        earliest_ts = int(file.readline().strip())
        bus_list = file.readline().strip().split(',')
        bus_info_list = []
        for i, bus_id in enumerate(bus_list):
            if bus_id != 'x':
                bus_info = BusInfo(id=int(bus_id), num=i)
                bus_info_list.append(bus_info)

        return ShuttleSearchInput(earliest_ts, bus_info_list)


# Copied (and slightly improved) from https://rosettacode.org/wiki/Chinese_remainder_theorem
def chinese_remainder(n, a):
    sum = 0
    product = prod(n)
    for n_i, a_i in zip(n, a):
        p = product // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % product


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def main():
    shuttles_input = read_input()

    best_id = None
    smaller_wait = None
    for bus in shuttles_input.bus_list:
        wait_time = (bus.id - shuttles_input.earliest_ts) % bus.id
        if smaller_wait is None or wait_time < smaller_wait:
            smaller_wait = wait_time
            best_id = bus.id
    print(best_id*smaller_wait)

    print(chinese_remainder(
        [bus.id for bus in shuttles_input.bus_list],
        [bus.id - bus.num for bus in shuttles_input.bus_list]
    ))


if __name__ == '__main__':
    main()
