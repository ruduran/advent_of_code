import re
from typing import List

from aoc2020.common import get_file_name


MEM_ADDR = re.compile(r"^mem\[(?P<addr>\d+)\]")


class DockingComputer:
    def __init__(self):
        self._mem = {}
        self._and_mask = ~0
        self._or_mask = 0

    def init(self, instructions: List[str]) -> None:
        for instruction in instructions:
            dest, value = instruction.split(" = ")
            if dest == "mask":
                self.set_mask(value)
            else:
                mem_match = MEM_ADDR.match(dest)
                if mem_match:
                    mem_addr = int(mem_match["addr"])
                    value = int(value)
                    self.write_value(mem_addr, value)
                else:
                    raise Exception(f"Failed to parse mem addr {dest}")

    def get_checksum(self) -> int:
        return sum(self._mem.values())

    def set_mask(self, new_mask: str) -> None:
        and_mask = ""
        or_mask = ""
        for c in new_mask:
            if c == 'X':
                and_mask += "1"
                or_mask += "0"
            elif c == '1':
                and_mask += "1"
                or_mask += "1"
            elif c == '0':
                and_mask += "0"
                or_mask += "0"
            else:
                raise Exception(f"Invalid value on mask: {c} {new_mask}")

        self._and_mask = int(and_mask, 2)
        self._or_mask = int(or_mask, 2)

    def write_value(self, addr: int, value: int) -> None:
        value &= self._and_mask
        value |= self._or_mask
        self._mem[addr] = value


class DockingComputerV2(DockingComputer):
    def __init__(self):
        super().__init__()

        self._mask = "0" * 36
        self._mask_list = []

    def set_mask(self, new_mask: str) -> None:
        self._mask = new_mask

    def write_value(self, addr: int, value: int) -> None:
        generated_addrs = self.generate_addrs(addr)
        for addr in generated_addrs:
            self._mem[addr] = value

    def generate_addrs(self, addr: int) -> List[int]:
        return self._generate_addrs(f"{addr:036b}")

    def _generate_addrs(self, remaining_new_addr: str, generated: str = "") -> List[int]:
        remaining_mask = self._mask[len(generated):]
        for i, c in enumerate(remaining_mask):
            if c == '1':
                generated = generated + remaining_new_addr[:i]
                return self._generate_addrs(remaining_new_addr[i+1:], generated + "1")
            if c == 'X':
                generated = generated + remaining_new_addr[:i]
                return self._generate_addrs(remaining_new_addr[i+1:], generated + "0") + self._generate_addrs(remaining_new_addr[i+1:], generated + "1")

        return [int(generated + remaining_new_addr, 2)]


def read_instructions() -> List[str]:
    instruction = []
    with open(get_file_name()) as file:
        for line in file:
            if line:
                instruction.append(line.strip())

    return instruction


def main():
    instructions = read_instructions()

    computer = DockingComputer()
    computer.init(instructions)
    print(computer.get_checksum())

    computer_v2 = DockingComputerV2()
    computer_v2.init(instructions)
    print(computer_v2.get_checksum())


if __name__ == '__main__':
    main()
