from utils import get_data_lines

def log(string):
    print(f"P14: {string}")

def run_rules(polymer, rules):
    log(f"sstarting run_rules with {polymer=} and{rules=}")

    pairs = []
    for idx in range(len(polymer) - 1):
        pairs.append(polymer[idx] + polymer[idx + 1])

    new_polymer = polymer[0]
    
    for traverse_pair in pairs:
        insertion = ''
        for parent_pair, child in rules:
            log(f"given {traverse_pair=}, evaluate rule with {parent_pair}->{child}")
            if traverse_pair != parent_pair: continue
            if len(insertion) > 0: raise Exception("MNost bad")
            insertion = child
            break
        new_polymer += insertion
        new_polymer += traverse_pair[1]
        log(f"Now {new_polymer=}")

    return new_polymer




if __name__ == '__main__':
    sample, full = get_data_lines(14)
    sample_template = sample[0]
    sample_pi = []
    for idx, value in enumerate(sample[2:]):
        tokens = value.split(' -> ')
        sample_pi.append((tokens[0], tokens[1],))
    answ = run_rules(sample_template, sample_pi)
    assert answ == 'NCNBCHB'
