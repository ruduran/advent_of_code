from collections import defaultdict
import operator
import re


CMP_OPERATORS = {
    '==': operator.eq,
    '!=': operator.ne,
    '>': operator.gt,
    '>=': operator.ge,
    '<': operator.lt,
    '<=': operator.le,
}


class BaseProcessor(object):
    def __init__(self, filename):
        self.filename = filename

        self.registers = defaultdict(int)

        re_string = '(?P<reg_op>[a-z]+) (?P<op>[a-z]+) (?P<num_op>-?\d+) if' \
                    ' (?P<reg_cmp>[a-z]+) (?P<cmp>[<>=!]+) (?P<num_cmp>-?\d+)'
        self.re_line = re.compile(re_string)

    def load_data(self):
        with open(self.filename) as f:
            for line in f:
                self.process_line(line.strip())

    def process_line(self, line):
        line_match = self.re_line.match(line)
        line_info = line_match.groupdict()
        cmp_func = self.get_cmp_func(line_info['cmp'])
        if cmp_func(self.registers[line_info['reg_cmp']],
                    int(line_info['num_cmp'])):
            inc = int(line_info['num_op'])
            if line_info['op'] == 'dec':
                inc = -inc

            self.registers[line_info['reg_op']] += inc

    def get_cmp_func(self, cmp_str):
        func = CMP_OPERATORS.get(cmp_str)
        if not func:
            raise Exception('Comparison not available {}'.format(cmp_str))

        return func
