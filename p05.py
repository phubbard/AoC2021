
from utils import *


def parse_lines(datalines):
    # return an array of (x1,y1,x2,y2) tuples
    rc = []
    for line in datalines:
        pairs = line.split('->')
        one_tokens = pairs[0].split(',')
        two_tokens = pairs[1].split(',')
        rc.append((int(one_tokens[0]), int(one_tokens[1]), int(two_tokens[0]), int(two_tokens[1])))
    return rc


def print_map(data2d):
    for row in data2d:
        rc = ''
        for character in row:
            if character == 0:
                rc += '.'
            else:
                rc += str(character)
        print(rc)


def reorder(command):
    # if left > right then swap so range works without step argument
    x1 = command[0]
    y1 = command[1]
    x2 = command[2]
    y2 = command[3]

    if x1 == x2:
        if y1 < y2:
            return command
        return (x1, y2, x2, y1)
    if x1 < x2:
        return command
    return (x2, y1, x1, y2)


def part_one(commands):
    num_rows = max(max(x[0], x[2]) for x in commands) + 1
    num_cols = max(max(x[1], x[3]) for x in commands) + 1
    dim = max(num_cols, num_rows)
    print(f'{len(commands)=} {num_cols=} {num_rows=}')

    data = make_2d_array(dim, dim)
    for command in commands:
        rcmd = reorder(command)
        col1 = rcmd[0]
        row1 = rcmd[1]
        col2 = rcmd[2]
        row2 = rcmd[3]
        if row1 == row2:
            for col in range(col1, col2 + 1):
                data[row1][col] += 1
        elif col1 == col2:
            for row in range(row1, row2 + 1):
                data[row][col1] += 1

    if num_cols < 80:
        print_map(data)

    danger_sum = 0
    for cur_row in range(num_rows):
        for cur_col in range(num_cols):
            if data[cur_row][cur_col] >= 2:
                danger_sum += 1

    print(f'{danger_sum=}')


if __name__ == '__main__':
    sample, full = get_data_lines(5)
    for commands in [sample, full]:
        part_one(parse_lines(commands))
