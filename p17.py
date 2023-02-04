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


def in_target(x: int, y: int, tgt: dict) -> bool:
    in_x = (min(tgt['x']) <= x <= max(tgt['x']))
    in_y = (min(tgt['y']) <= y <= max(tgt['y']))
    return in_x and in_y


def test_in_target():
    samp_tgt = {'x': [20, 30], 'y': [-10, -5]}
    assert in_target(20, -10, samp_tgt)
    assert in_target(30, -5, samp_tgt)
    assert in_target(30, -10, samp_tgt)
    assert in_target(20, -5, samp_tgt)
    assert not in_target(0, 0, samp_tgt)


def passed_target(x, y, tgt):
    if x > max(tgt['x']):
        return True
    if y < min(tgt['y']):
        return True
    return False


def fire_probe(xvel: int, yvel: int, fire_target: dict) -> tuple:
    # Given an initial x, y and target, return max Y reached if we hit the target during a step
    xpos = 0
    ypos = 0
    max_y = 0
    step = 0
    hit_target = False

    while not passed_target(xpos, ypos, fire_target):
        # print(f'Step begins {xpos=} {ypos=} {xvel=} {yvel=} {step=}')
        xpos += xvel
        ypos += yvel
        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        yvel -= 1
        max_y = max(max_y, ypos)
        if in_target(xpos, ypos, fire_target):
            # print(f'Hit at {step=} {xpos=} {ypos=} {target=}')
            hit_target = True
            break
        step += 1

    return max_y, hit_target


def part_one(target_p1):
    best_height = 0
    best_params = []
    for x_vel in range(1, 100):
        for y_vel in range(-200, 200):
            cur_height, hit = fire_probe(x_vel, y_vel, target_p1)
            if cur_height > best_height and hit:
                best_params = [x_vel, y_vel, cur_height]
                best_height = cur_height

    print(f'{best_params=}')


def part_two(my_target):
    count = 0
    for x_vel in range(1, 500):
        for y_vel in range(-200, 200):
            _, hit = fire_probe(x_vel, y_vel, my_target)
            if hit:
                # print(f'{x_vel}, {y_vel}')
                count += 1

    print(f'{count=}')


if __name__ == '__main__':
    test_in_target()
    sample, full = get_data_lines(17)
    for dataset in [sample, full]:
        target = parse_input(dataset[0])
        print(f'{target=}')
        part_one(target)
        part_two(target)
