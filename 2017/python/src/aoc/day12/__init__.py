
class BaseProcessor(object):
    def __init__(self, filename):
        self.filename = filename
        self.program_connections = {}

    def load_program_connections(self):
        with open(self.filename) as f:
            for line in f:
                line_split = line.split('<->')
                program = int(line_split[0])
                connections = {int(p) for p in line_split[1].split(',')}
                connections.discard(program)
                self.program_connections[program] = connections

    def programs_connected_with(self, program):
        found_connections = {program}
        conns_to_check = self.program_connections[program]
        while conns_to_check:
            connections_being_checked = conns_to_check.copy()
            for conn in connections_being_checked:
                if conn in found_connections:
                    continue

                found_connections.add(conn)
                next_connections = self.program_connections.get(conn, {})
                conns_to_check.update({c for c in next_connections
                                       if c not in found_connections})
                conns_to_check.discard(conn)

        return found_connections
