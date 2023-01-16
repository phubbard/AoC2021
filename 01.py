
sample_data = """199
200
208
210
200
207
240
269
260
263"""
sample_answer = 7

DATAFILE = './data/1.txt'

import numpy as np

if __name__ == '__main__':
    if False:
        data = [int(x) for x in sample_data.split('\n')]
    else:
        data = open(DATAFILE, 'r').readlines()
        data = [int(x.strip()) for x in  data]
    sum = 0
    for idx in range(1, len(data)):
        if data[idx - 1] < data[idx]:
           sum += 1
    print(sum)

    gimp = np.array(data)
    wimp = gimp + np.roll(gimp,1) + np.roll(gimp,2)
    wimp = wimp[2:]
    serious = np.diff(wimp)
    print(len(np.where(serious> 0)[0]))

    pass
