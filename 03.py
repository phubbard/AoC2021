from utils import make_2d_array, get_column, get_data_lines

sample_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


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

    data = make_2d_array(num_rows, num_cols, '0')

    for row_idx, line in enumerate(data_lines):
        for col_idx, character in enumerate(line):
            data[row_idx][col_idx] = character

    return data_lines


def orchestrate(data):
    num_cols = len(data[0])

    gamma = ''
    epsilon = ''
    for idx in range(num_cols):
        cur_col = get_column(data, idx)
        g, e = most_common(cur_col)
        gamma += str(g)
        epsilon += str(e)

    g_int = int(gamma, 2)
    e_int = int(epsilon, 2)

    print(f'{gamma=} {epsilon=} {g_int=} {e_int=} {e_int * g_int=}')


if __name__ == '__main__':
    test_most_common()

    data = get_data_lines(sample_data, 3, use_sample=False)
    orchestrate(data)