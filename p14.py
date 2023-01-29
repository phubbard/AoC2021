from utils import get_data_lines, find_permutations


def run_rules(polymer, rules):
    for rule in rules:
        loc = polymer.find(rule[0])
        if loc >= 0:
            print(f'Applying {rule=} to {polymer=}')
            polymer = polymer[:loc] + rule[1] + polymer[loc:]

    return polymer


if __name__ == '__main__':
    sample, full = get_data_lines(14)
    sample_template = sample[0]
    sample_pi = []
    for idx, value in enumerate(sample[2:]):
        tokens = value.split(' -> ')
        sample_pi.append((tokens[0], tokens[1],))
    answ = run_rules(sample_template, sample_pi)

    assert answ == 'NCNBCHB'
