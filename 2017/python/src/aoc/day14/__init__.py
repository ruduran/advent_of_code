from aoc.utils.hash import KnotHashCalculator


class BaseProcessor(object):
    SIZE = 128

    def __init__(self, filename):
        self.filename = filename
        self.key_string = None

    def load_input(self):
        with open(self.filename) as f:
            self.key_string = f.readline().strip()

    def get_disk_status(self):
        disk_status = []
        for row in range(self.SIZE):
            row_str = '{}-{}'.format(self.key_string, row)
            self.hash_calculator = KnotHashCalculator(row_str)
            row_hash = self.hash_calculator.get_hash()
            binary = self.hexa_to_bin(row_hash)
            disk_status.append(binary)
        return disk_status

    def hexa_to_bin(self, hexa):
        return list(bin(int(hexa, 16))[2:].zfill(self.SIZE))
