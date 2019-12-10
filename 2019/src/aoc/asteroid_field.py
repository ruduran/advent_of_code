from typing import Iterable, Tuple

ASTEROID_CHAR = '#'


class AsteroidField:
    def __init__(self):
        self._asteroids = {}

    def load(self, data: Iterable[Iterable[str]]):
        for y, line in enumerate(data):
            for x, cell in enumerate(line):
                if cell == ASTEROID_CHAR:
                    self._asteroids[(x, y)] = None

        for asteroid in self._asteroids:
            self._asteroids[asteroid] = self.get_asteroids_in_sight_from(asteroid)

    def get_asteroids_in_sight_from(self, origin_asteroid: Tuple[int, int]) -> set:
        asteroids_in_sight = set()
        o_x, o_y = origin_asteroid
        for asteroid in self._asteroids:
            if origin_asteroid == asteroid:
                continue

            x, y = asteroid
            d_x = abs(x - o_x)
            d_y = abs(y - o_y)

            visible = True
            if d_x == 0:
                min_y = min(o_y, y)
                for i in range(1, d_y):
                    n_y = min_y + i
                    if (o_x, n_y) in self._asteroids:
                        visible = False
                        continue
            else:
                if o_x < x:
                    base_x = o_x
                    base_y = o_y
                    proportion = (y - o_y)/d_x
                else:
                    base_x = x
                    base_y = y
                    proportion = (o_y - y)/d_x

                for i in range(1, d_x):
                    n_x = base_x + i
                    n_y = base_y + i*proportion
                    if n_y.is_integer() and (n_x, n_y) in self._asteroids:
                        visible = False
                        continue
            if visible:
                asteroids_in_sight.add(asteroid)

        return asteroids_in_sight

    def get_best_asteroid(self):
        best_asteroid = max(self._asteroids, key=lambda a: len(self._asteroids.get(a)))
        return best_asteroid, self._asteroids[best_asteroid]

    def destroy(self, asteroids_to_destroy: Iterable[Tuple[int, int]]):
        for asteroid in asteroids_to_destroy:
            del self._asteroids[asteroid]
