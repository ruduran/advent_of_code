import asyncio
from typing import Dict, List, Callable
from operator import add, mul

from .memory import Memory, MemoryAccessError


OPCODES_WITH_2_PARAMS = {1, 2, 5, 6, 7, 8}
OPCODES_WITH_1_PARAMS = {4}
OPCODES_WITH_DESTINATION = {1, 2, 3, 7, 8}


class IntcodeComputer:
    def __init__(self, input_queue: asyncio.Queue = None, output_queue: asyncio.Queue = None):
        self._cursor = 0
        self._memory = Memory()
        self._input_queue = input_queue
        self._output_queue = output_queue

    def load_memory(self, program: List[int]):
        self._cursor = 0
        self._memory.load_memory(program)

    def get_memory_position(self, position: int) -> int:
        return self._memory.get_memory_position(position)

    def _set_memory_position(self, position: int, value: int) -> None:
        self._memory.set_memory_position(position, value)

    def run(self):
        asyncio.run(self.run_async())

    async def run_async(self):
        """Execute the currently loaded program starting from the beginning"""
        while await self.run_instruction():
            pass

    async def run_instruction(self) -> bool:
        try:
            instruction_info = self._get_next_instruction()
            return await self._run_instruction(instruction_info)
        except StopIteration:
            return False
        except MemoryAccessError as e:
            print("Couldn't read the next memory addr: {}".format(e))
            return False

    def _get_next_instruction(self) -> Dict:
        raw_opcode = self._get_next_memory_value()
        opcode = raw_opcode % 100
        param_modes = raw_opcode // 100
        param_mode1 = param_modes % 10
        param_mode2 = (param_modes // 10) % 10

        instruction_info = {
            "opcode": opcode,
        }

        if opcode in OPCODES_WITH_1_PARAMS | OPCODES_WITH_2_PARAMS:
            instruction_info["param1"] = self._get_param(param_mode1)

        if opcode in OPCODES_WITH_2_PARAMS:
            instruction_info["param2"] = self._get_param(param_mode2)

        if opcode in OPCODES_WITH_DESTINATION:
            instruction_info["destination"] = self._get_next_memory_value()

        return instruction_info

    def _get_param(self, param_mode: int) -> int:
        value = self._get_next_memory_value()
        if param_mode == 0:
            return self.get_memory_position(value)
        elif param_mode == 1:
            return value
        else:
            raise NotImplementedError("Unsupported param mode '{}'".format(param_mode))

    def _get_next_memory_value(self) -> int:
        value = self._memory.get_memory_position(self._cursor)
        self._cursor += 1
        return value

    async def _run_instruction(self, instruction_info: Dict):
        opcode = instruction_info["opcode"]
        operation = self._get_operation(opcode)
        if operation:
            value = await operation(instruction_info)
            return value if value is not None else True
        else:
            raise NotImplementedError("Unsupported Opcode '{}'".format(opcode))

    def _get_operation(self, opcode: int) -> Callable:
        return {
            1: self._add,
            2: self._multiplication,
            3: self._input,
            4: self._output,
            5: self._jump_if_true,
            6: self._jump_if_false,
            7: self._less_than,
            8: self._equals,
            99: self._exit
        }.get(opcode)

    async def _add(self, instruction_info: Dict) -> None:
        await self._in_memory_op(add, instruction_info)

    async def _multiplication(self, instruction_info: Dict) -> None:
        await self._in_memory_op(mul, instruction_info)

    async def _in_memory_op(self, op: Callable, instruction_info: Dict) -> None:
        param1 = instruction_info["param1"]
        param2 = instruction_info["param2"]
        destination = instruction_info["destination"]

        result = op(param1, param2)

        self._set_memory_position(destination, result)

    async def _input(self, instruction_info: Dict) -> None:
        destination = instruction_info["destination"]

        if self._input_queue:
            value = await self._input_queue.get()
        else:
            value = int(input("Input: "))

        self._set_memory_position(destination, value)

    async def _output(self, instruction_info: Dict) -> None:
        value = instruction_info["param1"]

        if self._output_queue:
            await self._output_queue.put(value)
        else:
            print(value)

    async def _jump_if_true(self, instruction_info: Dict) -> None:
        if instruction_info["param1"]:
            self._cursor = instruction_info["param2"]

    async def _jump_if_false(self, instruction_info: Dict) -> None:
        if not instruction_info["param1"]:
            self._cursor = instruction_info["param2"]

    async def _less_than(self, instruction_info: Dict) -> None:
        param1 = instruction_info["param1"]
        param2 = instruction_info["param2"]
        destination = instruction_info["destination"]

        value = 1 if param1 < param2 else 0

        self._set_memory_position(destination, value)

    async def _equals(self, instruction_info: Dict) -> None:
        param1 = instruction_info["param1"]
        param2 = instruction_info["param2"]
        destination = instruction_info["destination"]

        value = 1 if param1 == param2 else 0

        self._set_memory_position(destination, value)

    @staticmethod
    async def _exit(_):
        return False
