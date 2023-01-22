from utils import *

if __name__ == '__main__':
    sample, full = get_data_lines(7)
    for data in [sample, full]:
        parsed = data[0].split(',')
        parsed = [int(x) for x in parsed]
        pass
