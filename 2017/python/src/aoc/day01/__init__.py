class BaseProcessor(object):
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        with open(self.filename) as f:
            line = f.readline().strip()
            numbers = [int(c) for c in line]
            return self.process_number_list(numbers)

    def process_number_list(self, numbers):
        raise NotImplementedError()
