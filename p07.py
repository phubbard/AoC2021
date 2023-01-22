from utils import *
import numpy as np


def fuel_allocation(data1d, location):
    return np.abs(np.array(data1d) - location).sum()

def part_one(data1d):
    num_pts = len(data1d)
    average = sum(data1d) / num_pts
    print(f'{average=} {num_pts=}')

    total_fuel = 0
    for crab in data1d:
        total_fuel += abs(crab - average)
    print(f'{total_fuel=}')


if __name__ == '__main__':
    sample, full = get_data_lines(7)
    for data in [sample, full]:
        parsed = data[0].split(',')
        parsed = [int(x) for x in parsed]
        part_one(parsed)
        print(np.array(parsed).mean())
        for i in range(7):
            print(i, fuel_allocation(parsed,i))

