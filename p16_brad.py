
import collections

from utils import *

def log(string):
    print(f"P16: {string}")


HEX_TO_BIN = {
             '0': [0,0,0,0],
             '1': [0,0,0,1],
             '2': [0,0,1,0],
             '3': [0,0,1,1],
             '4': [0,1,0,0],
             '5': [0,1,0,1],
             '6': [0,1,1,0],
             '7': [0,1,1,1],
             '8': [1,0,0,0],
             '9': [1,0,0,1],
             'A': [1,0,1,0],
             'B': [1,0,1,1],
             'C': [1,1,0,0],
             'D': [1,1,0,1],
             'E': [1,1,1,0],
             'F': [1,1,1,1],
             }


def pop_n(the_deque, n):
    rv = 0
    for _ in range(n):
        rv = rv * 2 + the_deque.popleft()
    return rv


def pop_literal(the_deque):
    rv = 0
    while len(the_deque) >= 5:
        more_digits = 1 == pop_n(the_deque, 1)
        next_digit = pop_n(the_deque, 4)
        rv = rv * 16 + next_digit
        if not more_digits:
            return rv
    raise Exception("Unexpected trailer")


def parse(hex_string):
    as_binary = []
    for character in hex_string:
        as_binary += HEX_TO_BIN[character]

    as_deque = collections.deque(as_binary)
    log(f"packet_version={pop_n(as_deque, 3)}")
    log(f"packet_type_id={pop_n(as_deque, 3)}")
    log(f"packet_literal={pop_literal(as_deque)}")



if __name__ == '__main__':
    for hex_string, answer in [
                ('D2FE28', -1),
            ]:
        parse(hex_string)



