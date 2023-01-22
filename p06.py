from utils import *
import numpy as np


if __name__ == '__main__':
    sample, full = get_data_lines(6)
    for data in [sample, full]:
        parsed = data[0].split(',')
        parsed = np.array([int(x) for x in parsed])

        v,c = np.unique(parsed, return_counts=True)
        tracker = np.zeros(9)
        for idx, count in zip(v,c):
            tracker[idx] = count

        pass