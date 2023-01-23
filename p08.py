from utils import *
from collections import Counter


if __name__ == '__main__':
    sample, full = get_data_lines(8)
    for raw in [sample, full]:
        unique = set()
        tracking = Counter()
        for cur_line in raw:
            # Input | output
            tokens = cur_line.split('|')
            output_tokens = tokens[1].strip().split(' ')
            for item in output_tokens:
                if len(item) in [2, 3, 4, 7]:
                    tracking.update([item])
        print(f'{tracking.total()=}')
