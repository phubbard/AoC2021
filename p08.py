from utils import *

num_lit = {
    0: 6, 1: 2, 2: 6, 3: 6, 4: 4, 5: 6, 6: 7, 7: 3, 8: 7, 9: 6
}

if __name__ == '__main__':
    sample, full = get_data_lines(8)
    for raw in [sample, full]:
        unique = set()
        for cur_line in raw:
            # Input | output
            tokens = cur_line.split('|')
            output_tokens = tokens[1].strip().split(' ')
            for item in output_tokens:
                if len(item) in [2, 3, 4, 7]:
                    unique.add(item)
        print(f'{len(unique)=}')
