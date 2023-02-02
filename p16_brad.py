
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


def pop_subpacket_bits(the_deque, bits):
    rv = []
    for _ in range(bits):
        rv.append(the_deque.popleft())
    return collections.deque(rv)


def parse_packet_from_hex(hex_string):
    as_binary = []
    for character in hex_string:
        as_binary += HEX_TO_BIN[character]
    as_deque = collections.deque(as_binary)
    parse_packet_from_binary(as_deque)


def parse_packet_from_binary(the_deque):
    packet_version = pop_n(the_deque, 3)
    packet_type_id = pop_n(the_deque, 3)
    if packet_type_id == 4:
        packet_literal = pop_literal(the_deque)
        log(f"Saw literal {packet_version=}/{packet_type_id=}->{packet_literal=}")
    else:
        length_type_id = pop_n(the_deque, 1)
        if length_type_id == 0:
            length_in_bits = pop_n(the_deque, 15)
            log(f"Saw operator bit count {packet_version=}/{packet_type_id=}->{length_in_bits=}")
            sub_packet = pop_subpacket_bits(the_deque, length_in_bits)
            parse_packet_from_binary(sub_packet)
        else:
            length_in_packets = pop_n(the_deque, 11)
            log(f"Saw operator packet count {packet_version=}/{packet_type_id=}->{length_in_packets=}")
            for x in range(length_in_packets):
                log(f"Cracking subpacket {x}...")
                parse_packet_from_binary(the_deque)


if __name__ == '__main__':
    for hex_string, answer in [
                ('D2FE28',            -1),
                ('38006F45291200',    -1),
                ('EE00D40C823060',    -1),
            ]:
        log(f"STARTING -> {hex_string=}")
        parse_packet_from_hex(hex_string)
        log(f"")



