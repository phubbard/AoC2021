from utils import *
from collections import Counter


def interference_stats(a, b):
    aonly = [x for x in a if x not in b]
    bonly = [x for x in b if x not in a]
    both = [x for x in a if x in b]
    return ''.join(aonly), ''.join(both), ''.join(bonly)


def get_numbers(slist):
    nd = {}
    # Put in 1,7,4, and 8
    temp = [x for x in slist if len(x) == 2]
    assert (len(temp) == 1)
    nd[1] = temp[0]

    temp = [x for x in slist if len(x) == 3]
    assert (len(temp) == 1)
    nd[7] = temp[0]

    temp = [x for x in slist if len(x) == 4]
    assert (len(temp) == 1)
    nd[4] = temp[0]

    temp = [x for x in slist if len(x) == 7]
    assert (len(temp) == 1)
    nd[8] = temp[0]

    # print(nd)
    # Next up we grind it against 1.
    for s in slist:
        tracer = interference_stats(s, nd[1])
        a = len(tracer[0])
        b = len(tracer[1])
        c = len(tracer[2])
        if (a == 5) and (b == 1) and (c == 1):
            nd[6] = s
        if (a == 3) and (b == 2) and (c == 0):
            nd[3] = s

    # print(nd)
    # Now only look at the strings that are left!
    left = [x for x in slist if x not in nd.values()]
    # print(left)
    # Grinding the remainder against 4
    for s in left:
        tracer = interference_stats(s, nd[4])
        a = len(tracer[0])
        b = len(tracer[1])
        c = len(tracer[2])
        if (a == 2) and (b == 4) and (c == 0):
            nd[9] = s
        if (a == 2) and (b == 3) and (c == 1):
            nd[5] = s
        if (a == 3) and (b == 2) and (c == 2):
            nd[2] = s
        if (a == 3) and (b == 3) and (c == 1):
            nd[0] = s

    return nd


def process_line(input_line):
    tokens = input_line.split('|')
    input_tokens = tokens[0].strip().split(' ')
    output_tokens = tokens[1].strip().split(' ')
    input_dict = get_numbers(input_tokens)
    magic_decoder = {}
    for current_key in input_dict:
        v = input_dict[current_key]
        v = ''.join(sorted(v))
        magic_decoder[v] = current_key

    temp = [''.join(sorted(x)) for x in output_tokens]
    return 1000 * magic_decoder[temp[0]] + 100 * magic_decoder[temp[1]] + 10 * magic_decoder[temp[2]] + magic_decoder[temp[3]]


if __name__ == '__main__':
    sample, full = get_data_lines(8)
    for raw in [sample, full]:
        tracking = Counter()
        total = 0
        for cur_line in raw:
            # This encapsulates part two
            cur_number = process_line(cur_line)
            total += cur_number
            # Input | output - this is part one
            tokens = cur_line.split('|')
            output_tokens = tokens[1].strip().split(' ')
            for item in output_tokens:
                if len(item) in [2, 3, 4, 7]:
                    tracking.update([item])
        print(f'part one {tracking.total()=}')
        print(f'part two {total=}')