import os
from setuptools import setup, find_packages

cwd = os.path.dirname(__file__)

setup(
    name='adventofcode',
    description='Advent of Code 2017 - Python 3',
    version='0.1',
    url='https://github.com/ruduran/advent_of_code/',
    packages=find_packages('src'),
    install_requires=open(os.path.join(cwd, 'requirements.txt')).readlines(),
    tests_require=open(os.path.join(cwd, 'test-requirements.txt')).readlines(),
    package_dir={
        '': 'src',
    },
    entry_points={
        'console_scripts': [
            'day01_part1 = aoc.day01.part1:main',
            'day01_part2 = aoc.day01.part2:main',
            'day02_part1 = aoc.day02.part1:main',
            'day02_part2 = aoc.day02.part2:main',
            'day03_part1 = aoc.day03.part1:main',
            'day04_part1 = aoc.day04.part1:main',
            'day04_part2 = aoc.day04.part2:main',
            'day05_part1 = aoc.day05.part1:main',
            'day05_part2 = aoc.day05.part2:main',
            'day06 = aoc.day06:main',
            'day07_part1 = aoc.day07.part1:main',
            'day07_part2 = aoc.day07.part2:main',
            'day08_part1 = aoc.day08.part1:main',
            'day08_part2 = aoc.day08.part2:main',
            'day09 = aoc.day09:main',
            'day10_part1 = aoc.day10.part1:main',
            'day10_part2 = aoc.day10.part2:main',
        ],
    }
)
