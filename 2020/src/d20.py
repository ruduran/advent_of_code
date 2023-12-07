import re
from typing import List, Optional, Tuple
from aoc2020.common import get_file_name


class Tile:
    def __init__(self, id: int, raw: List[str]):
        self._id = id
        self._raw = raw
        self._recalculate_borders()

    def _recalculate_borders(self):
        self._borders = [
            self._raw[0],
            ''.join([line[-1] for line in self._raw]),
            ''.join(self._raw[-1]),
            ''.join([line[0] for line in self._raw])
        ]

    def __repr__(self) -> str:
        newline = "\n"
        return f"{self._id}\n{newline.join(line for line in self._raw)}\n{self._borders}"

    def rotate(self, num=1):
        rotations = num % 4
        for _ in range(rotations):
            self._raw = [''.join(line[col] for line in self._raw) for col in reversed(range(len(self._raw)))]
            self._recalculate_borders()

    def flip_x(self):
        self._raw = list(reversed(self._raw))
        self._recalculate_borders()

    def flip_y(self):
        self._raw = [''.join(reversed(line)) for line in self._raw]
        self._recalculate_borders()

    @property
    def id(self) -> int:
        return self._id

    @property
    def borders(self) -> List[str]:
        return self._borders

    @property
    def content_without_border(self) -> List[str]:
        return [line[1:-1] for line in self._raw[1:-1]]


#                   #
# #    ##    ##    ###
#  #  #  #  #  #  #
SEA_MONSTER_L1 = re.compile("..................#")
SEA_MONSTER_L2 = re.compile("#....##....##....###")
SEA_MONSTER_L3 = re.compile(".#..#..#..#..#..#")


class MainImage(Tile):
    def get_num_of(self, char: str = '#') -> int:
        return sum([line.count(char) for line in self._raw])

    def get_roughness(self) -> int:
        total_num_of_hashtags = self.get_num_of('#')
        hashtags_per_monsters = 15

        num_monsters = 0
        for _ in range(4):
            num_monsters = self._find_num_monsters()
            if num_monsters:
                break

            self.flip_x()
            num_monsters = self._find_num_monsters()
            if num_monsters:
                break

            self.flip_y()
            num_monsters = self._find_num_monsters()
            if num_monsters:
                break
            else:
                self.rotate()

        if not num_monsters:
            num_monsters = self._find_num_monsters()
        return total_num_of_hashtags - num_monsters * hashtags_per_monsters

    def _find_num_monsters(self) -> int:
        num_found = 0
        for i in range(len(self._raw) - 2):
            for j in range(len(self._raw[0]) - 20):
                if SEA_MONSTER_L1.match(self._raw[i][j:]) and SEA_MONSTER_L2.match(self._raw[i+1][j:]) and SEA_MONSTER_L3.match(self._raw[i+2][j:]):
                    num_found += 1
        return num_found


def read_tiles() -> List[Tile]:
    tiles = []
    with open(get_file_name()) as file:
        tuple_id = None
        raw_tuple = []
        for line in file:
            line = line.strip()
            if not line:
                tiles.append(Tile(tuple_id, raw_tuple))
                tuple_id = None
                raw_tuple = []
            elif tuple_id is None:
                tuple_id_split = line.strip().split(' ')
                tuple_id = int(tuple_id_split[-1][:-1])
            else:
                raw_tuple.append(line)
        tiles.append(Tile(tuple_id, raw_tuple))

    return tiles


def _find_valid_intersection(tile: Tile, other: Tile) -> Optional[Tuple[int, int]]:
    intersection = set(tile.borders) & set(other.borders)
    if intersection:
        for common_border in list(intersection):
            border_num_in_existing = tile.borders.index(common_border)
            border_num_in_new = other.borders.index(common_border)
            if (border_num_in_new - border_num_in_existing) % 4 == 2:
                return border_num_in_existing, border_num_in_new

    return None


def find_valid_intersection(tile: Tile, other: Tile) -> Optional[Tuple[int, int]]:
    for _ in range(4):
        intersection = _find_valid_intersection(tile, other)
        if intersection:
            return intersection

        other.flip_x()
        intersection = _find_valid_intersection(tile, other)
        if intersection:
            return intersection

        other.flip_y()
        intersection = _find_valid_intersection(tile, other)
        if intersection:
            return intersection
        else:
            other.rotate()

    return _find_valid_intersection(tile, other)


def arranged_tiles(tiles: list[Tile]) -> List[List[Tile]]:
    num_tiles = len(tiles)
    arranged_tiles: List[List[Optional[Tile]]] = [[None for _ in range(num_tiles)] for _ in range(num_tiles)]
    min_x = num_tiles//2
    min_y = num_tiles//2
    max_x = num_tiles//2
    max_y = num_tiles//2
    arranged_tiles[min_x][min_y] = tiles[0]
    remaining_tiles = {tile.id: tile for tile in tiles[1:]}

    while remaining_tiles:
        for x, line in enumerate(arranged_tiles):
            for y, tile in enumerate(line):
                if tile:
                    for n_tile_id in list(remaining_tiles.keys()):
                        n_tile = remaining_tiles[n_tile_id]
                        intersection = find_valid_intersection(tile, n_tile)

                        if intersection:
                            border_num_in_existing, _ = intersection
                            if border_num_in_existing == 0:
                                n_x = x - 1
                                arranged_tiles[n_x][y] = n_tile
                                min_x = min(min_x, n_x)
                            elif border_num_in_existing == 1:
                                n_y = y + 1
                                arranged_tiles[x][n_y] = n_tile
                                max_y = max(max_y, n_y)
                            elif border_num_in_existing == 2:
                                n_x = x + 1
                                arranged_tiles[n_x][y] = n_tile
                                max_x = max(max_x, n_x)
                            elif border_num_in_existing == 3:
                                n_y = y - 1
                                arranged_tiles[x][n_y] = n_tile
                                min_y = min(min_y, n_y)

                            del remaining_tiles[n_tile_id]

    return [[arranged_tiles[x][y] for y in range(min_y, max_y+1)] for x in range(min_x, max_x+1)]


def join_tiles(arranged_tile_matrix: List[List[Tile]]) -> MainImage:
    main_tile_raw = []
    for row in arranged_tile_matrix:
        main_tile_raw.extend(''.join(line) for line in zip(*[tile.content_without_border for tile in row]))
    return MainImage(0, main_tile_raw)


def main():
    tiles = read_tiles()
    arranged = arranged_tiles(tiles)
    print(arranged[0][0].id * arranged[0][-1].id * arranged[-1][0].id * arranged[-1][-1].id)

    main_tile = join_tiles(arranged)
    print(main_tile)
    print(main_tile.get_roughness())


if __name__ == '__main__':
    main()
