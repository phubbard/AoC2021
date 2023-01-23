from utils import *

scoring_table = {
    ')': 3, ']': 57, '}': 1197, '>': 25137
}


def part_one(datalines):
    pass


if __name__ == '__main__':
    sample, full = get_data_lines(10)
    for cur_dataset in [sample, full]:
        part_one(cur_dataset)
