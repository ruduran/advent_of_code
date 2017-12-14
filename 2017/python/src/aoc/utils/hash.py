from functools import reduce


class KnotHashCalculator(object):
    MARKS = 256

    def __init__(self, input_str=''):
        self.number_list = list(range(self.MARKS))
        self.current_position = 0
        self.skip_size = 0
        self.set_input(input_str)

    def set_input(self, input_str):
        self.lenghts = [ord(n) for n in input_str]
        self.lenghts += [17, 31, 73, 47, 23]

    def get_hash(self):
        for i in range(64):
            self.run_round()

        group_size = 16
        dense_list = []
        index = 0
        while index < len(self.number_list):
            stop = index + group_size
            dense_list.append(reduce(lambda i, j: int(i) ^ int(j),
                              self.number_list[index: stop]))
            index = stop

        return ''.join(map("{:02x}".format, dense_list))

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
