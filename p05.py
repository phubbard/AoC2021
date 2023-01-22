
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


def draw_upright_diagonal(rcmd, data2d):
    col1 = rcmd[0]
    row1 = rcmd[1]
    col2 = rcmd[2]
    row2 = rcmd[3]
    assert row1 > row2
    assert col2 > col1

    for idx in range(col1, col2 + 1):
        row = row1 - idx
        data2d[row][idx] += 1

    return data2d


def draw_downright_diagonal(rcmd, data2d):
    col1 = rcmd[0]
    row1 = rcmd[1]
    col2 = rcmd[2]
    row2 = rcmd[3]
    assert row1 < row2
    assert col1 < col2

    for idx in range(row1, row2 + 1):
        data2d[idx][col1 + idx] += 1
    return data2d


def draw_diagonal(rcmd, data2d):
    col1 = rcmd[0]
    row1 = rcmd[1]
    col2 = rcmd[2]
    row2 = rcmd[3]

    if row1 < row2 and col1 < col2:
        # Down and to the right
        return draw_downright_diagonal(rcmd, data2d)
    if row1 > row2 and col1 < col2:
        # Up and to the right
        return draw_upright_diagonal(rcmd, data2d)
    if row1 > row2 and col1 < col2:
        # down and to the left
        return draw_upright_diagonal((col2, row2, col1, row1), data2d)
    if row1 > row2 and col1 > col2:
        # up and to the left
        return draw_downright_diagonal((col2, row2, col1, row1), data2d)
    pass


def part_two(commands):
    num_rows = max(max(x[0], x[2]) for x in commands) + 1
    num_cols = max(max(x[1], x[3]) for x in commands) + 1
    dim = max(num_cols, num_rows)
    data = make_2d_array(dim, dim)
    print(f'{len(commands)=} {num_cols=} {num_rows=}')
    for command in commands:
        if horizontal(command):
            draw_horizontal(command, data)
        elif vertical(command):
            draw_vertical(command, data)
        else:
            draw_diagonal(command, data)
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
    for commands in [sample]:
        cmd_tuples = parse_lines(commands)
        part_one(cmd_tuples)
        part_two(cmd_tuples)
