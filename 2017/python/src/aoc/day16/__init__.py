class BaseProcessor(object):

    def __init__(self, filename):
        self.filename = filename
        self.instructions = []
        self.programs = [chr(ord('a') + i) for i in range(16)]

    def load_instructions(self):
        with open(self.filename) as f:
            line = f.readline().strip()
            self.instructions = line.split(',')

    def run_instructions(self):
        for instruction in self.instructions:
            self.run(instruction)

    def run(self, instruction):
        inst_type = instruction[0]
        if inst_type == 's':
            spin_size = int(instruction[1:])
            self.programs = self.programs[-spin_size:] + self.programs[:-spin_size]
        elif inst_type == 'x':
            pos_split = instruction[1:].split('/')
            pos_a = int(pos_split[0])
            pos_b = int(pos_split[1])
            self.programs[pos_a], self.programs[pos_b] = self.programs[pos_b], self.programs[pos_a]
        elif inst_type == 'p':
            pos_a = self.programs.index(instruction[1])
            pos_b = self.programs.index(instruction[3])
            self.programs[pos_a], self.programs[pos_b] = self.programs[pos_b], self.programs[pos_a]
