from utils import get_data_lines


def parse_input(dataline):
    # Return a dict of the target area
    rc = {'x': [], 'y': []}

    tokens = dataline.split(' ')
    xtok = tokens[2].split('..')
    ytok = tokens[3].split('..')
    rc['x'] = [int(xtok[0][2:]), int(xtok[1].removesuffix(','))]
    rc['y'] = [int(ytok[0][2:]), int(ytok[1].removesuffix(','))]
    return rc


def in_target(x, y, target) -> bool:
    return x in range(target['x'][0], target['x'][1] + 1) and y in range(target['y'][0], target['y'][1] + 1)


def test_in_target():
    target = {'x': [20, 30], 'y': [-10, -5]}
    assert in_target(20, -10, target)
    assert in_target(30, -5, target)
    assert in_target(30, -10, target)
    assert in_target(20, -5, target)
    assert not in_target(0, 0, target)


def passed_target(x, y, target):
    if x > target['x'][1]:
        return True
    if y < min(target['y']):
        return True
    return False


def fire_probe(xvel: int, yvel: int, target: dict) -> tuple:
    # Given an initial x, y and target, return max Y reached if we hit the target during a step
    xpos = 0
    ypos = 0
    max_y = 0
    step = 0
    hit_target = False

    while not passed_target(xpos, ypos, target):
        # print(f'Step begins {xpos=} {ypos=} {xvel=} {yvel=} {step=}')
        xpos += xvel
        ypos += yvel
        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        yvel -= 1
        max_y = max(max_y, ypos)
        if in_target(xpos, ypos, target):
            # print(f'Hit at {step=} {xpos=} {ypos=} {target=}')
            hit_target = True
            break
        step += 1

    return max_y, hit_target


def part_one(target):
    best_height = 0
    best_params = []
    for x_vel in range(1, 100):
        for y_vel in range(-200, 200):
            cur_height, hit = fire_probe(x_vel, y_vel, target)
            if cur_height > best_height and hit:
                best_params = [x_vel, y_vel, cur_height]
                best_height = cur_height

    print(f'{best_params=}')


def part_two(target):
    count = 0
    for x_vel in range(1, 100):
        for y_vel in range(-200, 200):
            _, hit = fire_probe(x_vel, y_vel, target)
            if hit:
                # print(f'{x_vel}, {y_vel}')
                count += 1

    print(f'{count=}')


if __name__ == '__main__':
    test_in_target()
    sample, full = get_data_lines(17)
    for dataset in [sample, full]:
        target = parse_input(dataset[0])
        part_one(target)
        part_two(target)
