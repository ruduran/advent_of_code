class BaseProcessor(object):
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        with open(self.filename) as f:
            jump_list = [int(l) for l in f]
            return self.number_of_jumps_to_get_out(jump_list)

    def number_of_jumps_to_get_out(self, jump_list):
        index = 0
        jump_count = 0
        while index >= 0 and index < len(jump_list):
            jump = jump_list[index]
            jump_list[index] = self.updated_jump(jump)
            index += jump
            jump_count += 1
        return jump_count

    def updated_jump(self, jump):
        raise NotImplementedError()
