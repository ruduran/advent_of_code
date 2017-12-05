import argparse


def get_file_name(msg='Advent of Code 2010'):
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('file', help='input file')
    args = parser.parse_args()
    return args.file
