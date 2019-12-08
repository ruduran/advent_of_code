from common import get_file_name
from aoc.space_image_format import SpaceImageFormat


def main():
    image = SpaceImageFormat(width=25, height=6)

    with open(get_file_name()) as file:
        image_str = file.readline().strip()
        image.load_image(image_str)

    print("Checksum: {}".format(image.checksum()))
    image.render()


if __name__ == '__main__':
    main()
