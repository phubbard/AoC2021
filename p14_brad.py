
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

def run_bigger_rules(polymer, rules, chunk_size):
    first_character = polymer[0]
    chunks = []
    while len(polymer) >= chunk_size:
        chunk = polymer[0:chunk_size]
        polymer = polymer[chunk_size:]
        chunks.append(chunk)
    chunks.append(polymer)

    new_polymer = first_character
    for chunk in chunks:
        result = rules.get(chunk, chunk)
        new_polymer += result[1:]
    return new_polymer


sample_distinct = {'C': True, 'H': True, 'B': True, 'N': True}

full_distinct = {'H': True, 'K': True, 'P': True, 'S': True, 'B': True, 'V': True, 'C': True, 'F': True, 'N': True, 'O': True}

if __name__ == '__main__':
    sample, full = get_data_lines(14)
    for dataset, expected in [
                (sample, 2188189693529),
            #    (full, -1),
                ]:
        sample_template = dataset[0]
        sample_pi = {}
        for idx, value in enumerate(dataset[2:]):
            tokens = value.split(' -> ')
            sample_pi[tokens[0]] = tokens[1]
            
        for manual_permute in [
                'CCC', 'CCH', 'CCB', 'CCN',
                'CHC', 'CHH', 'CHB', 'CHN',
               ]:
            resultant = run_rules(manual_permute, sample_pi)
            sample_pi[manual_permute] = resultant

        for step in range(3):
            old_template = run_rules(sample_template, sample_pi)
            new_template = run_bigger_rules(sample_template, sample_pi, 3)
            log(f"{step=}  {old_template=} {new_template=}")

            sample_template = old_template

        counter = collections.Counter(sample_template)
        sorted_out = counter.most_common()
        log(f"{sorted_out=}")
        score = sorted_out[0][1] - sorted_out[-1][1]
        log(f"{score=}")
        # assert score == expected


