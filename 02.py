
sample_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


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
    if False:
        data = sample_data.split('\n')
    else:
        inp_data = open('./data/2.txt', 'r').readlines()
        data = [x.strip() for x in inp_data]

    part_one(data)
    part_two(data)
