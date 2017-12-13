
class BaseProcessor(object):
    def __init__(self, filename):
        self.filename = filename
        self.firewall_layers = {}

    def load_firewall_conf(self):
        with open(self.filename) as f:
            for line in f:
                line_split = line.split(':')
                depth = int(line_split[0])
                layer_range = int(line_split[1])
                self.firewall_layers[depth] = layer_range

    def caught_at_depth(self, depth, time, lane):
        layer_range = self.firewall_layers.get(depth, 0)
        full_cycle = layer_range * 2 - 2
        scanner_pos_on_cycle = time % full_cycle
        if scanner_pos_on_cycle / layer_range <= 1:
            scanner_lane = scanner_pos_on_cycle
        else:
            scanner_lane = 2 * layer_range - scanner_pos_on_cycle
        return lane == scanner_lane
