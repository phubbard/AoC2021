import collections

from utils import *

A = 'a'
B = 'b'
C = 'c'
D = 'd'
E = 'e'
F = 'f'
G = 'g'

NUMBER_OF_SEGMENTS = 7
NUMBER_OF_DIGITS = 10

ALL_SEGMENTS_IN_ORDER = [ A, B, C, D, E, F, G ]

seven_segment_canonical = {
        0: set([ A, B, C,    E, F, G ]),      # SHARE 0,6,9
        1: set([       C,       F    ]), # UNIQUE 2
        2: set([ A,    C, D, E,    G ]),   # SHARE 2,3,5
        3: set([ A,    C, D,    F, G ]),   # SHARE 2,3,5
        4: set([    B, C, D,    F,   ]), # UNIQUE 4
        5: set([ A, B,    D,    F, G ]),   # SHARE 2,3,5
        6: set([ A, B,    D, E, F, G ]),      # SHARE 0,6,9
        7: set([ A,    C,       F    ]), # UNIQUE 3
        8: set([ A, B, C, D, E, F, G ]), # UNIQUE 8
        9: set([ A, B, C, D,    F, G ]),      # SHARE 0,6,9
      }


#######################
# FROM https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
#
# Python function to print permutations of a given list
def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 
 
# Driver program to test above function
data = list('123')
for p in permutation(data):
    print (p)


total_found = 0
for p in permutation(ALL_SEGMENTS_IN_ORDER):
    total_found +=1
    if total_found < 6: print(f" a sample one is {p}")
print(f"Found {total_found=}")


class Hypothesis:
    def __init__(self, segment_list):
        assert len(segment_list) == NUMBER_OF_SEGMENTS
        retain_map = collections.OrderedDict()
        for idx, segment in enumerate(ALL_SEGMENTS_IN_ORDER):
            retain_map[segment] = segment_list[idx]

        self.__map = retain_map
        print(f"given map {segment_list=} the map is {self.__map}")

    def hypothesis_generate(self, number):
        unmapped = seven_segment_canonical[number]
        print(f"{unmapped=}")
        rv = [self.__map[x] for x in unmapped]
        print(f"at first {rv=}")
        rv.sort()
        print(f"after sort {rv=}")
        rv = ''.join(rv)
        print(f"after string {rv=}")
        return rv


if __name__ == '__main__':
    sample, full = get_data_lines(7)
    
    for x in range(NUMBER_OF_DIGITS):
        total_illuminated = len(seven_segment_canonical[x])
        print(f"{total_illuminated} segments in digit {x}")

    remaining_hypotheses = []
    for p in permutation(ALL_SEGMENTS_IN_ORDER):
        remaining_hypotheses += [Hypothesis(p)]

    print(f"count remaining is {len(remaining_hypotheses)}")

    try_decode = 'bdg'

    hypotheses_could_be_7 = []
    for h in remaining_hypotheses:
        generated_7 = h.hypothesis_generate(7)
        print(f"{h=} generates {generated_7=}")
        if try_decode == generated_7:
            hypotheses_could_be_7 += [h]

    print(f"count remaining is {len(hypotheses_could_be_7)}")



