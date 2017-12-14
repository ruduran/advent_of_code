from aoc.utils.hash import KnotHashCalculator


class BaseProcessor(KnotHashCalculator):

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def load_lenghts(self):
        raise NotImplementedError()
