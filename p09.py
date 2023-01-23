from utils import *
import numpy as np


def low_point(npdata, row, col) -> bool:
    # Eight edge cases - edges and corners
    num_rows = npdata.shape[0]
    num_cols = npdata.shape[1]
    datum = npdata[row][col]

    # Easy case - interior point - four neighbors
    if 0 < row and row <= (num_rows - 2) and 0 < col and col <= (num_cols - 2):
        up = datum < npdata[row - 1][col]
        down = datum < npdata[row + 1][col]
        left = datum < npdata[row][col - 1]
        right = datum < npdata[row][col + 1]
        return (up and down and left and right)

    # Top corners - 2 to check
    if row == 0:
        if col == 0:
            return datum < npdata[row + 1][col] and datum < npdata[row][col + 1]
        elif col == num_cols - 1:
            return datum < npdata[row][col - 1] and datum < npdata[row + 1][col]

    # Bottom corners
    if row == num_rows - 1:
        if col == 0:
            return datum < npdata[row - 1][col] and datum < npdata[row][col + 1]
        elif col == num_cols - 1:
            return datum < npdata[row - 1][col] and datum < npdata[row][col - 1]

    # Have done all four corner and center already, so left or right edges are handled this way - three to check
    if col == 0:
        return datum < npdata[row - 1][col] and datum < npdata[row + 1][col] and datum < npdata[row][col + 1]
    if col == num_cols - 1:
        return datum < npdata[row - 1][col] and datum < npdata[row + 1][col] and datum < npdata[row][col - 1]

    # top and bottom edges - three to check
    if row == 0:
        return datum < npdata[row][col - 1] and datum < npdata[row][col + 1] and datum < npdata[row + 1][col]
    elif row == num_rows - 1:
        return datum < npdata[row][col - 1] and datum < npdata[row][col + 1] and datum < npdata[row - 1][col]


if __name__ == '__main__':
    sample, full = get_data_lines(9)
    for dataset in [sample, full]:
        num_rows = len(dataset)
        num_cols = len(dataset[0])
        data = make_2d_array(num_rows, num_cols)
        for row, line in enumerate(dataset):
            for col, char in enumerate(line):
                data[row][col] = int(char)
        npdata = np.array(data)

        npg = np.gradient(npdata)

        # Brute force method
        low_points = 0
        risk_total = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if low_point(npdata, row, col):
                    low_points += 1
                    risk_score = 1 + npdata[row][col]
                    risk_total += risk_score
                    # print(f'low at {row=},{col=} {npdata[row][col]=} {risk_score=}')
        print(f'{low_points=} {risk_total=}')
