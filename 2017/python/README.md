# Solutions for Advent of Code 2017 written in Python

## Setup

You'll need `virtualenv` to follow this instructions:
```bash
virtualenv -p python3.5 venv
. venv/bin/activate
pip install -U -r requirements.txt -r test-requirements.txt
python setup.py develop
deactivate
```

## Usage

You'll find the scripts to run on `venv/bin` with the format `dayXX[_partX]`. The input files can be found on `data/dayXX`. For instance, running the script for the second part of the first day can be done like:
```bash
./venv/bin/day01_part2 data/day01/input
```

# Run tests and check code

```bash
. venv/bin/activate
flake8 src tests
nosetests
deactivate
```

## Puzzles

* [Day 1](http://adventofcode.com/2017/day/1)
* [Day 2](http://adventofcode.com/2017/day/2)
* [Day 3](http://adventofcode.com/2017/day/3)
* [Day 4](http://adventofcode.com/2017/day/4)
* [Day 5](http://adventofcode.com/2017/day/5)
* [Day 6](http://adventofcode.com/2017/day/6)
* [Day 7](http://adventofcode.com/2017/day/7)
* [Day 8](http://adventofcode.com/2017/day/8)
* [Day 9](http://adventofcode.com/2017/day/9)
* [Day 10](http://adventofcode.com/2017/day/10)
* [Day 11](http://adventofcode.com/2017/day/11)
