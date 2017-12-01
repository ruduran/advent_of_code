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
            'day1_part1 = aoc.day1.part1:main',
            'day1_part2 = aoc.day1.part2:main',
        ],
    }
)
