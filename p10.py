from utils import *


scoring_table = {
    ')': 3, ']': 57, '}': 1197, '>': 25137
}


def part_one(datalines):
    for line in datalines:
        counts = {}
        cl_map = {'>': '<', ')': '(', '}': '{', ']': '['}
        open_chars = ['<', '{', '[', '(']
        for x in open_chars:
            counts[x] = 0

        for character in line:
            if character in open_chars:
                counts[character] += 1
            else:
                open_char = cl_map[character]
                if counts[open_char] <= 0:
                    print(f'Error, got {character}')
                else:
                    counts[open_char] -= 1
        print(f'{counts=}')

if __name__ == '__main__':
    sample, full = get_data_lines(10)
    for cur_dataset in [sample]:
        part_one(cur_dataset)
