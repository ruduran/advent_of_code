from collections import defaultdict
from typing import List


class MemoryAccessError(Exception):
    pass


class Memory:
    def __init__(self):
        self._memory = defaultdict(int)

    def load_memory(self, memory: List[int]) -> None:
        for k, value in enumerate(memory):
            self._memory[k] = value

    def get_memory_position(self, position: int) -> int:
        try:
            return self._memory[position]
        except IndexError as e:
            raise MemoryAccessError(e)

    def set_memory_position(self, position: int, value: int) -> None:
        try:
            self._memory[position] = value
        except IndexError as e:
            raise MemoryAccessError(e)
