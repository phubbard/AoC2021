from utils import *

def print_map(data2d):
    for row in data2d:
        rc = ''
        for character in row:
            rc += str(character)
        print(rc)


if __name__ == '__main__':
    sample, full = load_2d_arrays(11)
    print_map(sample)

    print_map(full)