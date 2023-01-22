from copy import deepcopy
from utils import make_2d_array, get_column, get_data_lines


def is_bingo(data_2d) -> bool:
    num_rows = len(data_2d)
    num_cols = len(data_2d[0])
    assert num_cols == num_rows

    for idx in range(num_rows):
        num_true = sum(data_2d[idx])
        if num_true >= num_cols:
            return True

    for idx in range(num_cols):
        current_col = get_column(data_2d, idx)
        num_true = sum(current_col)
        if num_true >= num_rows:
            return True

    # diag_one = [data_2d[x][x] for x in range(num_rows)]
    # num_true = sum(diag_one)
    # if num_true >= num_rows:
    #     return True
    # 
    # diag_two = [data_2d[(num_rows - x) - 1][x] for x in range(num_rows)]
    # num_true = sum(diag_two)
    # if num_true >= num_rows:
    #     return True

    return False


def test_is_bingo():
    arr = [
        [0, 0, 1],
        [0, 0, 1],
        [1, 0, 1]
    ]
    assert is_bingo(arr)
    arr = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 0, 0]
    ]
    assert is_bingo(arr)
    arr = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    assert is_bingo(arr)
    arr = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    assert is_bingo(arr)
    arr = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert not is_bingo(arr)



def part_one(data_2d):
    print("Not started!")

def part_two(data_2d):
    print("Not started!")


if __name__ == '__main__':
    test_is_bingo()

    sample, full = get_data_lines(4)
    for step in [sample, full]:
        part_one(step)
        part_two(step)
