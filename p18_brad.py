from utils import get_data_lines



if __name__ == '__main__':
    sample, full = get_data_lines(18)

    for dataset, expected_a in [
                (sample, -1),
                (full,   -1),
            ]:
        print(f"{expected_a=}")
    print(f"Done")

