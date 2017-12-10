class BaseProcessor(object):
    MARKS = 256

    def __init__(self, filename):
        self.filename = filename
        self.number_list = list(range(self.MARKS))
        self.lenghts = []
        self.current_position = 0
        self.skip_size = 0

    def process(self):
        raise NotImplementedError()

    def load_lenghts(self):
        raise NotImplementedError()

    def run_round(self):
        for lenght in self.lenghts:
            if lenght <= self.MARKS:
                self.reverse(lenght)
                self.current_position += lenght + self.skip_size
                self.current_position %= self.MARKS
                self.skip_size += 1

    def reverse(self, lenght):
        if lenght <= 1:
            return

        start = self.current_position
        end = self.current_position + lenght
        to_reverse = self.number_list[start:end]
        if len(to_reverse) < lenght:
            end %= self.MARKS
            to_reverse += self.number_list[0:end]

        reversed_list = to_reverse[::-1]

        if start + len(reversed_list) > self.MARKS:
            division = self.MARKS - start
            self.number_list[start:self.MARKS] = reversed_list[0:division]
            self.number_list[0:end] = reversed_list[division:]
        else:
            self.number_list[start:end] = reversed_list
