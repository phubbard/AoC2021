
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
            while len(sub_packet) >= 6:
                parse_packet_from_binary(sub_packet, stats)
            log(f"REMAINDER COUNT IS -> {len(sub_packet)}")
        else:
            length_in_packets = pop_n(the_deque, 11)
            log(f"Saw operator packet count {packet_version=}/{packet_type_id=}->{length_in_packets=}")
            for x in range(length_in_packets):
                log(f"Cracking subpacket {x}...")
                parse_packet_from_binary(the_deque, stats)


DATA_FROM_FILE = '420D74C3088043390499ED709E6EB49A5CC4A3A3898B7E0F44011C4CC48AC0119D049B0C500265EB8F615900180910C88129B2F0007C61C4B7F74ED7396B20020A44A4C014D005E5A72E274B4E5C4B96CC3793410078C01D82F1DA08180351661AC1920042A3CC578BA6008F802138D93352B9CFCEF61D3009A7D2268D254925569C02A92D62BF108D52C1B3E4B257B57FAE5C54400A84840267880311D23245F1007A35C79848200C4288FF0E8C01194A4E625E00A4EFEF5F5996486C400C5002800BFA402D3D00A9C4027B98093D602231C00F001D38C009500258057E601324C00D3003D400C7003DC00A20053A6F1DBDE2D4600A6802B37C4B9E872B0E44CA5FF0BFB116C3004740119895E6F7312BCDE25EF077700725B9F2B8F131F333005740169A7F92EFEB3BC8A21998027400D2CDF30F927880B4C62D6CDFFD88EB0068D2BF019A8DAAF3245B39C9CFA1D2DF9C3DB9D3E50A0164BE2A3339436993894EC41A0D10020B329334C62016C8E7A5F27C97D0663982D8EB23C5282529CDD271E8F100AE1401AA80021119E3A4511006E1E47689323585F3AEBF900AEB2B6942BD91EE8028000874238AB0C00010B8D913220A004A73D789C4D54E24816301802538E940198880371AE15C1D1007638C43856C00954C25CD595A471FE9D90056D60094CEA61933A9854E9F3801F2BBC6131001F792F6796ACB40D036605C80348C005F64F5AC374888CA42FD99A98025319EB950025713656F202200B767AB6A30E802D278F81CBA89004CD286360094FC03A7E01640245CED5A3C010100660FC578B60008641C8B105CC017F004E597E596E633BA5AB78B9C8F840C029917C9E389B439179927A3004F003511006610C658A200084C2989D0AE67BD07000606154B70E66DC0C01E99649545950B8AB34C8401A5CDA050043D319F31CB7EBCEE14'

if __name__ == '__main__':
    for hex_string, answer in [
                ('D2FE28',                          -1),
                ('38006F45291200',                  -1),
                ('EE00D40C823060',                  -1),
                ('8A004A801A8002F478',              16),
                ('620080001611562C8802118E34',      12),
                ('C0015000016115A2E0802F182340',    23),
                ('A0016C880162017C3686B18A3D4780',  31),
                (DATA_FROM_FILE,                   895),
            ]:
        log(f"STARTING -> {hex_string=}")
        stats = parse_packet_from_hex(hex_string)
        output = stats.stats_get_sum_of_versions()
        log(f"CONCLUDED WITH {output=}")
        if answer > 0:
            if answer != output:
                raise Exception("DOOMY")

        log(f"")



