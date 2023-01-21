
from utils import get_data_lines
import numpy as np


if __name__ == '__main__':
    sample, full = get_data_lines(1)
    data = [int(x) for x in full]
    running_sum = 0
    for idx in range(1, len(data)):
        if data[idx - 1] < data[idx]:
           running_sum += 1
    print(running_sum)

    gimp = np.array(data)
    wimp = gimp + np.roll(gimp,1) + np.roll(gimp,2)
    wimp = wimp[2:]
    serious = np.diff(wimp)
    print(len(np.where(serious > 0)[0]))

