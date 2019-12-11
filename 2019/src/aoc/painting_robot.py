import asyncio
from collections import defaultdict
from typing import List

from aoc.space_image_format import SpaceImageFormat

from .intcode.intcode_computer import IntcodeComputer

INCLINATIONS = {
    '^': {0: '<', 1: '>'},
    '<': {0: 'v', 1: '^'},
    '>': {0: '^', 1: 'v'},
    'v': {0: '>', 1: '<'}
}

MOVEMENTS = {
    '^': (0, -1),
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1)
}


class PaintingRobot:
    def __init__(self, initial_color=0):
        self._board = defaultdict(int)
        self._queue_to_brain = asyncio.Queue()
        self._queue_from_brain = asyncio.Queue()
        self._brain = IntcodeComputer(self._queue_to_brain, self._queue_from_brain)

        self._location = (0, 0)
        self._board[self._location] = initial_color
        self._current_inclination = '^'

    def load_program(self, program: List[int]):
        self._brain.load_memory(program)

    def get_painted_cells(self):
        return self._board.keys()

    def get_board_as_image(self) -> SpaceImageFormat:
        points = self._board.keys()
        min_x = min(points, key=lambda p: p[0])[0]
        max_x = max(points, key=lambda p: p[0])[0]
        min_y = min(points, key=lambda p: p[1])[1]
        max_y = max(points, key=lambda p: p[1])[1]
        dense_image = []
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                dense_image.append(str(self._board[(x, y)]))

        image = SpaceImageFormat(width=abs(max_x-min_x)+1, height=abs(max_y-min_y)+1)
        image.load_image(''.join(dense_image))
        return image

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._run())

    async def _run(self):
        brain_task = asyncio.create_task(self._brain.run_async())
        body_task = asyncio.create_task(self._body_loop())

        await brain_task
        await body_task

    async def _body_loop(self):
        keep_looping = True
        while keep_looping:
            color = self._board[self._location]
            self._queue_to_brain.put_nowait(color)

            new_color = await self._queue_from_brain.get()
            if new_color is None:
                keep_looping = False
                continue

            self._board[self._location] = new_color

            turn = await self._queue_from_brain.get()
            self._current_inclination = INCLINATIONS[self._current_inclination][turn]
            self._location = tuple(map(sum, zip(self._location, MOVEMENTS[self._current_inclination])))
