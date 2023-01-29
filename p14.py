from utils import get_data_lines, find_permutations




if __name__ == '__main__':
    sample, full = get_data_lines(14)
    sample_template = sample[0]
    sample_pt = []
    for idx, value in enumerate(sample[2:]):
        tokens = value.split(' -> ')
        sample_pt.append((tokens[0], tokens[1],))

    full_pt = []
    for value in full[2:]:
        tokens = value.split(' -> ')
        full_pt.append((tokens[0], tokens[1]))

    unique_chars = set()
    for rule in sample_pt:
        unique_chars.update(rule[0][0])
        unique_chars.update(rule[0][1])
        unique_chars.update(rule[1])

    print(f'{len(list(unique_chars))=} {list(unique_chars)=}')
    perms = find_permutations(unique_chars, 4)
    print(f'{len(list(perms))=}')

    unique_chars = set()
    for rule in full_pt:
        unique_chars.update(rule[0][0])
        unique_chars.update(rule[0][1])
        unique_chars.update(rule[1])

    print(f'{len(list(unique_chars))=} {list(unique_chars)=}')
    perms = find_permutations(unique_chars, 8)
    print(f'{len(list(perms))=:,}')
