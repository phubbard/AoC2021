from utils import *
import numpy as np


def iterate_day(tracking):
    new_track = np.zeros_like(tracking)
    for idx in range(1, len(tracking)):
        new_track[idx - 1] = tracking[idx]
    new_track[6] = new_track[6] + tracking[0]
    new_track[len(tracking) - 1] += tracking[0]
    return new_track


def get_fish(tracking):
    return tracking.sum()


if __name__ == '__main__':
    sample, full = get_data_lines(6)
    for data in [sample, full]:
        parsed = data[0].split(',')
        parsed = np.array([int(x) for x in parsed])

        v, c = np.unique(parsed, return_counts=True)
        tracker = np.zeros(9)
        for idx, count in zip(v, c):
            tracker[idx] = count

        # Check for 18 days the sample
        for i in range(256):
            # print(i, tracker)
            tracker = iterate_day(tracker)
        print(f"After {i} days: {get_fish(tracker)}")
