import asyncio
from collections import defaultdict, Counter
from typing import List

from .intcode.intcode_computer import IntcodeComputer


class ArcadeCabinet:
    def __init__(self, free_play=False):
        self._queue_to_processor = asyncio.Queue()
        self._queue_from_processor = asyncio.Queue()
        self._processor = IntcodeComputer(input_queue=self._queue_to_processor, output_queue=self._queue_from_processor)

        self._free_play = free_play

        self._screen_matrix = defaultdict(int)

        self._ball_pos = 0
        self._paddle_pos = 0
        self._score = 0

    def load_game(self, program: List[int]):
        if self._free_play:
            program = [2] + program[1:]
        self._processor.load_memory(program)

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._run())

    def get_num_of_blocks(self) -> int:
        elements_per_type = Counter(self._screen_matrix.values())
        return elements_per_type[2]

    def get_score(self) -> int:
        return self._score

    async def _run(self):
        processor_task = asyncio.create_task(self._processor.run_async())
        arcade_task = asyncio.create_task(self._play())

        await processor_task
        await arcade_task

    async def _play(self):
        while True:
            x: int = await self._queue_from_processor.get()
            if x is None:
                break

            y: int = await self._queue_from_processor.get()
            tile_id: int = await self._queue_from_processor.get()

            if x == -1:
                self._score = tile_id
                continue

            if tile_id == 3:
                self._paddle_pos = x
            elif tile_id == 4:
                self._ball_pos = x
                self._queue_to_processor.put_nowait(self._get_joystick_movement())

            self._screen_matrix[(x, y)] = tile_id

    def _get_joystick_movement(self) -> int:
        if self._ball_pos > self._paddle_pos:
            return 1

        if self._ball_pos < self._paddle_pos:
            return -1

        return 0
