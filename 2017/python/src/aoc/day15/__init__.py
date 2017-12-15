import re


class Generator(object):
    def __init__(self, mult_factor, div_factor):
        self.value = 0
        self.mult = mult_factor
        self.div = div_factor
        self.multiple_of = None

    def set_value(self, value):
        self.value = value

    def set_multiple_of_condition(self, multiple_of):
        self.multiple_of = multiple_of

    def get_next(self):
        self.generate_next_value()
        if self.multiple_of is not None:
            while self.value % self.multiple_of != 0:
                self.generate_next_value()
        return self.value

    def generate_next_value(self):
        self.value = (self.value * self.mult) % self.div


class BaseProcessor(object):
    BITS_TO_COMPARE = 16

    def __init__(self, filename):
        self.filename = filename
        self.generator = {
            'A': Generator(16807, 2147483647),
            'B': Generator(48271, 2147483647),
        }

    def load_start_values(self):
        with open(self.filename) as f:
            regex = re.compile('Generator (\w) starts with (\d+)')
            for line in f:
                match = regex.match(line)
                name = match.group(1)
                num = int(match.group(2))
                self.generator[name].set_value(num)

    def get_eq_count(self, iterations):
        count = 0
        for i in range(iterations):
            value_a = self.generator['A'].get_next()
            bits_a = value_a % 2**self.BITS_TO_COMPARE

            value_b = self.generator['B'].get_next()
            bits_b = value_b % 2**self.BITS_TO_COMPARE
            if bits_a == bits_b:
                count += 1
        return count
