
from utils import get_data_lines

def part_one(data):
    horizontal = depth = aim = 0
    for line in data:
        tokens = line.split(' ')
        value = int(tokens[1])
        match tokens[0]:
            case 'forward':
                horizontal += value
            case 'down':
                depth += value
            case 'up':
                depth -= value
            case _:
                assert(False)
    print(f'{horizontal=} {depth=} {horizontal * depth=}')


def part_two(data):
    horizontal = depth = aim = 0
    for line in data:
        tokens = line.split(' ')
        value = int(tokens[1])
        match tokens[0]:
            case 'forward':
                horizontal += value
                depth += (aim * value)
            case 'down':
                aim += value
            case 'up':
                aim -= value
            case _:
                assert(False)
    print(f'{horizontal=} {depth=} {aim=} {horizontal * depth=}')


if __name__ == '__main__':
    for i in [True, False]:
        data = get_data_lines(2, use_sample=i)
        part_one(data)
        part_two(data)
