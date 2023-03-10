
# https://adventofcode.com/2021/day/3#part2

from copy import deepcopy
from utils import make_2d_array, get_column, get_data_lines


def most_common(array):
    array_sum = sum([int(x) for x in array])
    if array_sum >= (len(array) / 2):
        return 1, 0
    return 0, 1


def test_most_common():
    assert (most_common('011110011100') == (1, 0))
    assert (most_common('000111100100') == (0, 1))
    assert (most_common('101010101010') == (1, 0))
    assert (most_common('111111000000') == (1, 0))


def parse_lines(data_lines):
    num_cols = len(data_lines[0])
    num_rows = len(data_lines)

    array = make_2d_array(num_rows, num_cols, '0')

    for row_idx, line in enumerate(data_lines):
        for col_idx, character in enumerate(line):
            array[row_idx][col_idx] = character

    return data_lines


def part_one(data_2d):
    num_cols = len(data_2d[0])

    gamma = ''
    epsilon = ''
    for idx in range(num_cols):
        cur_col = get_column(data_2d, idx)
        g, e = most_common(cur_col)
        gamma += str(g)
        epsilon += str(e)

    g_int = int(gamma, 2)
    e_int = int(epsilon, 2)

    print(f'{gamma=} {epsilon=} {g_int=} {e_int=} {e_int * g_int=}')


def part_two(data_2d):
    o2_rating = co2_rating = 0
    num_cols = len(data_2d[0])

    o2_data = deepcopy(data_2d)
    co2_data = deepcopy(data_2d)

    for idx in range(num_cols):
        cur_col = get_column(o2_data, idx)
        a, b = most_common(cur_col)
        # Filter data - save only rows where the bit in the current column matches
        o2_data = list(filter(lambda x: int(x[idx]) == a, o2_data))
        # Done?
        if len(o2_data) == 1:
            o2_rating = int(o2_data[0], 2)
            break

    for idx in range(num_cols):
        cur_col = get_column(co2_data, idx)
        a, b = most_common(cur_col)
        co2_data = list(filter(lambda x: int(x[idx]) == b, co2_data))

        if len(co2_data) == 1:
            co2_rating = int(co2_data[0], 2)
            break

    print(f'{o2_rating=} {co2_rating=} {o2_rating * co2_rating=}')


if __name__ == '__main__':
    test_most_common()

    sample, full = get_data_lines(3)
    for step in [sample, full]:
        part_one(step)
        part_two(step)
