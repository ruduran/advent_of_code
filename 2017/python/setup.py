import os
from setuptools import setup, find_packages

cwd = os.path.dirname(__file__)

setup(
    name='adventofcode',
    description='Advent of Code 2017 - Python 3',
    version='0.1',
    author='TODO',
    author_email='TODO',
    url='TODO',
    packages=find_packages('src'),
    install_requires=open(os.path.join(cwd, 'requirements.txt')).readlines(),
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
