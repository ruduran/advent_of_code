from asyncio import Queue, run, create_task
from itertools import permutations
from typing import Tuple, List

from common import get_file_name
from aoc.intcode.intcode_computer import IntcodeComputer


async def get_amps_output(program: List[int]):
    async def try_with(phase_settings: Tuple[int]):
        queues = [Queue() for _ in range(5)]
        for i in range(5):
            await queues[i].put(phase_settings[i])
            if i == 0:
                await queues[i].put(0)
        tasks = []
        for i in range(5):
            amp = IntcodeComputer(queues[i], queues[(i+1) % 5])
            amp.load_memory(program)
            tasks.append(create_task(amp.run_async()))

        for t in tasks:
            await t
        value = await queues[0].get()
        return value

    phase_settings_permutations = permutations(range(5))
    return max([await try_with(phase_settings) for phase_settings in phase_settings_permutations])


async def main():
    with open(get_file_name()) as file:
        memory_str = file.readline()
        program = [int(d) for d in memory_str.strip().split(",")]
        print(await get_amps_output(program))


if __name__ == '__main__':
    run(main())
