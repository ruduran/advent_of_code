import re


class BaseProcessor(object):
    def __init__(self, filename):
        self.filename = filename

        self.programs_without_parent = set()
        self.programs = {}
        self.root = None

        re_string = '(?P<name>[a-z]+) \((?P<weight>\d+)\)' \
                    '( -> (?P<children>[a-z]+(, [a-z]+)*))?'
        self.program_re = re.compile(re_string)

    def add_program(self, program_str):
        match = self.program_re.match(program_str)
        if not match:
            return  # TODO: Exception?

        prog_info = match.groupdict()
        prog_info['weight'] = int(prog_info['weight'])
        if prog_info.get('children'):
            children = prog_info.get('children')
            prog_info['children'] = [c.strip() for c in children.split(',')]
        else:
            prog_info['children'] = []

        name = prog_info['name']
        self.programs[name] = prog_info
        self.programs_without_parent.add(name)

    def structure_towers(self):
        for program in self.programs.values():
            children = program['children']
            children_with_info = {k: self.programs[k] for k in children}
            program['children'] = children_with_info
            for child_name in children:
                self.programs_without_parent.remove(child_name)

    def load_data(self):
        with open(self.filename) as f:
            for line in f:
                self.add_program(line.strip())

        self.structure_towers()

        if len(self.programs_without_parent) == 1:
            root_name = self.programs_without_parent.pop()
            self.root = self.programs[root_name]
        else:
            raise Exception("Multiple bottom programs found")
