from __future__ import annotations

import argparse

from argparse import Namespace
from dataclasses import dataclass, field
from typing import Generator, Iterable, Optional, Tuple


@dataclass
class Node:
    name: str
    parent: Optional[Node] = None


@dataclass
class File(Node):
    size: int = 0


@dataclass
class Directory(Node):
    elements: dict[str, Node] = field(default_factory=dict)


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def get_terminal_output(file: str) -> Generator[str, None, None]:
    with open(file) as f:
        for line in f:
            if data := line.rstrip():
                yield data


def run(lines: Iterable[str]) -> Directory:
    filesystem = Directory(name="/")
    cursor: Optional[Node] = None
    for line in lines:
        if line.startswith("$"):
            match line[2:].split():
                case ["cd", "/"]:
                    cursor = filesystem
                case ["cd", ".."]:
                    cursor = cursor.parent
                case ["cd", name]:
                    if name not in cursor.elements:
                        cursor.elements[name] = Directory(name=name, parent=cursor)
                    cursor = cursor.elements[name]
        else:
            match line.split():
                case ["dir", name]:
                    if name not in cursor.elements:
                        cursor.elements[name] = Directory(name=name, parent=cursor)
                case [size, name]:
                    cursor.elements[name] = File(name=name, size=int(size), parent=cursor)

    return filesystem


def _dirs_with_sizes(dir: Directory, path: str) -> Tuple[int, dict]:
    total_size = 0
    dirs_with_sizes = {}
    for element in dir.elements.values():
        if isinstance(element, Directory):
            dir_path = path + element.name + "/"
            size, sub_dirs_with_sizes = _dirs_with_sizes(element, dir_path)
            dirs_with_sizes.update(sub_dirs_with_sizes)
            dirs_with_sizes[dir_path] = size
            total_size += size
        else:
            total_size += element.size

    return total_size, dirs_with_sizes


def get_dirs_with_sizes(filesystem: Directory) -> dict:
    size, sub_dirs_with_sizes = _dirs_with_sizes(filesystem, path="/")
    sub_dirs_with_sizes[filesystem.name] = size
    return sub_dirs_with_sizes


def main():
    args = parse_arguments()
    filesystem = run(get_terminal_output(args.filename))
    dirs_with_sizes = get_dirs_with_sizes(filesystem)
    sizes_under_100000 = [size for size in dirs_with_sizes.values() if size < 100000]
    print(sum(sizes_under_100000))

    total_used_size = dirs_with_sizes["/"]
    available_space = 70000000 - total_used_size
    size_needed = 30000000 - available_space
    deletion_candidates = [size for size in dirs_with_sizes.values() if size >= size_needed]
    print(min(deletion_candidates))


if __name__ == "__main__":
    main()
