import argparse


def get_file_name():
    parser = argparse.ArgumentParser(description='AoC')
    parser.add_argument('file', help='input file')
    args = parser.parse_args()
    return args.file
