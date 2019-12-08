from unittest import TestCase

from .memory import Memory, MemoryAccessError


class TestMemory(TestCase):
    def setUp(self) -> None:
        self.memory = Memory()

    def test_load_memory(self):
        # given
        program = [1, 0, 0, 3, 99]

        # when
        self.memory.load_memory(program)

        # then
        self.assertListEqual(program, self.memory._memory)

    def test_get_memory_position(self):
        # given
        program = [1, 0, 0, 3, 99]
        self.memory.load_memory(program)

        # when -> then
        for i, value in enumerate(program):
            self.assertEqual(value, self.memory.get_memory_position(i))

    def test_get_memory_position_raises_exception(self):
        # given
        self.memory.load_memory([])

        # when -> then
        with self.assertRaises(MemoryAccessError):
            self.memory.get_memory_position(0)

    def test_set_memory_position(self):
        # given
        new_value = 99
        program = [1, 0, 0, 3, 99]
        self.memory.load_memory(program)

        # when
        self.memory.set_memory_position(0, new_value)

        # then
        self.assertEqual(new_value, self.memory.get_memory_position(0))

    def test_set_memory_position_raises_exception(self):
        # given
        self.memory.load_memory([])

        # when -> then
        with self.assertRaises(MemoryAccessError):
            self.memory.set_memory_position(0, 0)
