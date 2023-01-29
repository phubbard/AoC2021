
import collections

from utils import get_data_lines

def log(string):
    print(f"P14: {string}")

def run_rules(polymer, rules):
    # log(f"sstarting run_rules with {polymer=} and{rules=}")

    pairs = []
    for idx in range(len(polymer) - 1):
        pairs.append(polymer[idx] + polymer[idx + 1])

    new_polymer = polymer[0]
    
    for traverse_pair in pairs:
        found = rules.get(traverse_pair, None)
        if found:
            new_polymer += found
        new_polymer += traverse_pair[1]
        #log(f"Now {new_polymer=}")

    return new_polymer




if __name__ == '__main__':
    sample, full = get_data_lines(14)
    for dataset, expected in [
                (sample, 2188189693529),
                (full, -1),
                ]:
        sample_template = dataset[0]
        sample_pi = {}
        for idx, value in enumerate(dataset[2:]):
            tokens = value.split(' -> ')
            sample_pi[tokens[0]] = tokens[1]
            
        for step in range(40):
            log(f"{step=}")
            sample_template = run_rules(sample_template, sample_pi)

        counter = collections.Counter(sample_template)
        sorted_out = counter.most_common()
        log(f"{sorted_out=}")
        score = sorted_out[0][1] - sorted_out[-1][1]
        log(f"{score=}")
        assert score == expected


