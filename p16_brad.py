
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


class Stats:
    def __init__(self):
        self.__version_sum = 0

    def stats_saw_version(self, packet_version):
        self.__version_sum += packet_version

    def stats_get_sum_of_versions(self):
        return  self.__version_sum


def parse_packet_from_hex(hex_string):
    as_binary = []
    for character in hex_string:
        as_binary += HEX_TO_BIN[character]
    as_deque = collections.deque(as_binary)
    stats = Stats()
    parse_packet_from_binary(as_deque, stats)
    return stats


def parse_packet_from_binary(the_deque, stats):
    packet_version = pop_n(the_deque, 3)
    stats.stats_saw_version(packet_version)
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
            parse_packet_from_binary(sub_packet, stats)
        else:
            length_in_packets = pop_n(the_deque, 11)
            log(f"Saw operator packet count {packet_version=}/{packet_type_id=}->{length_in_packets=}")
            for x in range(length_in_packets):
                log(f"Cracking subpacket {x}...")
                parse_packet_from_binary(the_deque, stats)


if __name__ == '__main__':
    for hex_string, answer in [
                ('D2FE28',                         -1),
                ('38006F45291200',                 -1),
                ('EE00D40C823060',                 -1),
                ('8A004A801A8002F478',             16),
                ('620080001611562C8802118E34',     12),
                ('C0015000016115A2E0802F182340',   23),
                ('A0016C880162017C3686B18A3D4780', 31),


            ]:
        log(f"STARTING -> {hex_string=}")
        stats = parse_packet_from_hex(hex_string)
        output = stats.stats_get_sum_of_versions()
        log(f"CONCLUDED WITH {output=}")
        log(f"")



