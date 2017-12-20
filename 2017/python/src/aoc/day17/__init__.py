from tqdm import tqdm


class BaseProcessor(object):

    def __init__(self, filename):
        self.filename = filename
        self.buffer = [0]
        self.buffer_len = 1
        self.steps = 0
        self.pos = 0

    def load_steps(self):
        with open(self.filename) as f:
            self.steps = int(f.readline())

    # TODO: Refactor and improve interface
    def run(self, times, search_for_next_of):
        search_for_pos = 0
        for i in tqdm(range(1, times+1)):
            self.move(self.steps)
            self.pos += 1
            self.buffer_len += 1
            if i == search_for_next_of:
                search_for_pos = self.pos
            if i <= search_for_next_of:
                self.buffer.insert(self.pos, i)
            else:
                if self.pos <= search_for_pos + 1:
                    self.buffer.insert(self.pos, i)
                    if self.pos <= search_for_pos:
                        search_for_pos += 1

    def move(self, steps):
        self.pos = (self.pos + steps) % self.buffer_len
