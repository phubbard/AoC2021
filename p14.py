from utils import get_data_lines
from collections import Counter


def score_counts(ctr: Counter):
    rc = Counter()
    for cur_key in ctr.keys():
        rc[cur_key[0]] += ctr[cur_key]

    return rc


if __name__ == '__main__':
    sample, full = get_data_lines(14)

    for dataset in [sample, full]:
        polymer = dataset[0]
        rules = {}
        for value in dataset[2:]:
            tokens = value.split(' -> ')
            old_token = tokens[0]
            new_tokens = [old_token[0] + tokens[1], tokens[1] + old_token[1]]
            rules[old_token] = new_tokens

    count_dict = Counter()
    for idx in range(len(polymer) - 1):
        count_dict.update([polymer[idx:idx + 2]])

    for idx in range(40):
        ncd = Counter()
        for key in count_dict.keys():
            for cur_out in rules[key]:
                ncd[cur_out] += count_dict[key]
        count_dict = ncd
    scores = score_counts(count_dict)
    scores.update([polymer[-1]])
    print(f'{scores=}')
    sorted_out = scores.most_common()
    print(f"{sorted_out=}")
    score = sorted_out[0][1] - sorted_out[-1][1]
    print(f"{score=}")

