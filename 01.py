
from utils import get_data_lines

import numpy as np

if __name__ == '__main__':
    data_lines = get_data_lines(1, use_sample=False)
    data = [int(x) for x in data_lines]
    sum = 0
    for idx in range(1, len(data)):
        if data[idx - 1] < data[idx]:
           sum += 1
    print(sum)

    gimp = np.array(data)
    wimp = gimp + np.roll(gimp,1) + np.roll(gimp,2)
    wimp = wimp[2:]
    serious = np.diff(wimp)
    print(len(np.where(serious > 0)[0]))

