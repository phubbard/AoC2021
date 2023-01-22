import math
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


def part_one(commands):
    num_rows = max(max(x[0], x[2]) for x in commands) + 1
    num_cols = max(max(x[1], x[3]) for x in commands) + 1
    dim = max(num_cols, num_rows)
    data = make_2d_array(dim, dim)
    print(f'{len(commands)=} {num_cols=} {num_rows=}')

    for rcmd in commands:
        if horizontal(rcmd):
            draw_horizontal(rcmd, data)
        elif vertical(rcmd):
            draw_vertical(rcmd, data)

    if num_cols < 80:
        print_map(data)

    danger_sum = 0
    for cur_row in range(num_rows):
        for cur_col in range(num_cols):
            if data[cur_row][cur_col] >= 2:
                danger_sum += 1

    print(f'{danger_sum=}')


def horizontal(rcmd) -> bool:
    col1 = rcmd[0]
    row1 = rcmd[1]
    col2 = rcmd[2]
    row2 = rcmd[3]
    return row2 == row1 and col2 != col1


def vertical(rcmd) -> bool:
    col1 = rcmd[0]
    row1 = rcmd[1]
    col2 = rcmd[2]
    row2 = rcmd[3]
    return col2 == col1 and row2 != row1


def draw_horizontal(rcmd, data2d):
    col1 = rcmd[0]
    row1 = rcmd[1]
    col2 = rcmd[2]
    row2 = rcmd[3]
    begin = min(col1, col2)
    end = max(col1, col2)
    for col in range(begin, end + 1):
        data2d[row1][col] += 1
    return data2d


def draw_vertical(rcmd, data2d):
    col1 = rcmd[0]
    row1 = rcmd[1]
    col2 = rcmd[2]
    row2 = rcmd[3]
    begin = min(row1, row2)
    end = max(row1, row2)
    for row in range(begin, end + 1):
        data2d[row][col1] += 1
    return data2d


def insert_line(rcmd, data2d):
    # Extract coordinates
    col1 = rcmd[0]
    row1 = rcmd[1]
    col2 = rcmd[2]
    row2 = rcmd[3]
    # Get differences
    dcol = col2 - col1
    drow = row2 - row1
    # Make sure it's not the same point ---otherwise gcd will fall over
    assert (dcol ** 2 + drow ** 2 > 0)
    g = math.gcd(dcol, drow)
    # Divide out by gcd so that we will step through the integer points on the line
    dgcol = int(dcol / g)
    dgrow = int(drow / g)
    # Confirming that everything is doing what is expected
    # print("Col delta: ", dcol, "\t Row delta: ", drow, "\t gcd:", g, "Simplified coords:", dgcol, dgrow)
    # Step through all fo the integer points between the two endpoints incrementing the data array
    for k in range(g + 1):
        data2d[row1 + k * dgrow][col1 + k * dgcol] += 1
    return data2d


def part_two(commands):
    num_rows = max(max(x[0], x[2]) for x in commands) + 1
    num_cols = max(max(x[1], x[3]) for x in commands) + 1
    dim = max(num_cols, num_rows)
    data = make_2d_array(dim, dim)
    print(f'{len(commands)=} {num_cols=} {num_rows=}')
    for command in commands:
        insert_line(command, data)

    if num_cols < 80:
        print_map(data)

    danger_sum = 0
    for cur_row in range(num_rows):
        for cur_col in range(num_cols):
            if data[cur_row][cur_col] >= 2:
                danger_sum += 1

    print(f'part two {danger_sum=}')


if __name__ == '__main__':
    sample, full = get_data_lines(5)
    for commands in [sample, full]:
        cmd_tuples = parse_lines(commands)
        part_one(cmd_tuples)
        part_two(cmd_tuples)
