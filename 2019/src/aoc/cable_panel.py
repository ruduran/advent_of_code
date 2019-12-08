class CablePanel:
    def __init__(self):
        self._collisions = []
        self._cables = []

    def add_cable(self, cable_definition):
        cable_sections = []

        x, y = 0, 0
        sections = cable_definition.split(',')
        for section in sections:
            initial_coord = (x, y)

            displacement = int(section[1:])
            if section[0] == 'R':
                x += displacement
            elif section[0] == 'L':
                x -= displacement
            elif section[0] == 'U':
                y += displacement
            elif section[0] == 'D':
                y -= displacement

            final_coord = (x, y)

            section_coords = (initial_coord, final_coord)

            self.find_collisions(section_coords)

            cable_sections.append(section_coords)

        self._cables.append(cable_sections)

    def _find_collision(self, section, section2):
        ((x1, y1), (x2, y2)) = section
        ((nx1, ny1), (nx2, ny2)) = section2

        if nx1 == nx2:
            if min(x1, x2) <= nx1 <= max(x1, x2):
                int_x = nx1
                if min(ny1, ny2) <= y1 <= max(ny1, ny2):
                    int_y = y1
                    return int_x, int_y
        else:
            if min(y1, y2) <= ny1 <= max(y1, y2):
                int_y = ny1
                if min(nx1, nx2) <= x1 <= max(nx1, nx2):
                    int_x = x1
                    return int_x, int_y

    def find_collisions(self, section_coords):
        """ It is assumed that there are no diagonal sections and cables running on the same coords """
        for cable in self._cables:
            for section in cable:
                collision = self._find_collision(section, section_coords)
                if collision:
                    self._record_collision(collision)

    def _record_collision(self, collision):
        if collision != (0, 0):
            self._collisions.append(collision)

    def _get_distance(self, point, orig=(0, 0)):
        x, y = point
        orig_x, orig_y = orig
        return abs(x - orig_x) + abs(y - orig_y)

    def get_closest_collision_distance(self):
        min_distance = None
        for collision in self._collisions:
            distance = self._get_distance(collision)
            if not min_distance or distance < min_distance:
                min_distance = distance

        return min_distance

    def _get_distance_on_cable(self, point):
        distance = 0
        for cable in self._cables:
            current_point = (0, 0)
            for section in cable:
                collision = self._find_collision((point, point), section)
                if collision:
                    distance += self._get_distance(current_point, collision)
                    break
                else:
                    new_point = section[1]
                    distance += self._get_distance(current_point, new_point)
                    current_point = new_point
        return distance

    def get_closest_collision_distance_on_cable(self):
        min_distance = None
        for collision in self._collisions:
            distance = self._get_distance_on_cable(collision)
            if not min_distance or distance < min_distance:
                min_distance = distance

        return min_distance
