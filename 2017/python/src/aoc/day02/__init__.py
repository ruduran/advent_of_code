class BaseProcessor(object):
    def __init__(self, filename):
        self.filename = filename

    def calculate_checksum(self):
        with open(self.filename) as f:
            file_data = []
            for line in f:
                line_numbers = [int(c) for c in line.split('\t')]
                file_data.append(line_numbers)

            return self._calc_checksum(file_data)

    def _calc_checksum(self, file_data):
        raise NotImplementedError()
