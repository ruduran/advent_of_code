from collections import Counter
from typing import Tuple


class SpaceImageFormat:
    def __init__(self, width: int, height: int):
        self._image = []
        self._width = width
        self._height = height

    def load_image(self, data: str):
        image_size = len(data)
        layer_size = self._width * self._height
        assert (image_size % layer_size) == 0, "The image doesn't fit a whole number of layers"

        num_of_layers = image_size // layer_size
        for i in range(num_of_layers):
            self._image.append(data[i*layer_size:(i+1)*layer_size])

    def checksum(self) -> int:
        layer_counts = [Counter(layer) for layer in self._image]
        layer_with_fewer_zeros = min(layer_counts, key=lambda c: c['0'])
        return layer_with_fewer_zeros['1'] * layer_with_fewer_zeros['2']

    def render(self):
        pixels = zip(*self._image)
        image = ''.join(map(self._pixel_value, pixels)).replace('0', ' ').replace('1', '█')
        for h in range(self._height):
            print(image[h*self._width:(h+1)*self._width])

    @staticmethod
    def _pixel_value(pixel_tuple: Tuple) -> str:
        for p in pixel_tuple:
            if p != '2':
                return p

        return '2'
