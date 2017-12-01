# Solutions for Advent of Code 2017 written in Python

## Setup

You'll need `virtualenv` to follow this instructions:
```bash
virtualenv -p python3.5 venv
. venv/bin/activate
pip install -U -r requirements.txt
python setup.py develop
deactivate
```

## Usage

You'll find the scripts to run on `venv/bin` with the format `dayXX_partX`. The input files can be found on `data/dayXX`. For instance, running the script for the second part of the first day can be done like:
```bash
./venv/bin/day1_part2 data/day1/input
```

## Puzzles

* [Day 1](http://adventofcode.com/2017/day/1)
