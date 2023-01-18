from copy import deepcopy
from utils import make_2d_array, get_column, get_data_lines


def most_common(array):
    array_sum = sum([int(x) for x in array])
    if array_sum >= (len(array) / 2):
        return 1, 0
    return 0, 1


def test_most_common():
    assert (most_common('011110011100') == (1, 0))


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

    local_data = deepcopy(data_2d)

    for idx in range(num_cols):
        cur_col = get_column(data_2d, idx)
        a, b = most_common(cur_col)
        # Filter data - save only rows where the bit in the current column matches
        # TODO use filter?

        # Do the converse using b - co2 scrubber rating
        # TODO


if __name__ == '__main__':
    test_most_common()

    for step in [True, False]:
        data = get_data_lines(3, use_sample=step)
        part_one(data)
        part_two(data)
