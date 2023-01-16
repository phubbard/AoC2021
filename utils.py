
def clean_lines(input_lines):
    return [x.strip() for x in input_lines]


def make_2d_array(num_rows, num_cols, fill=0):
    # Create and allocate a 2D array. Copypasta from SO with edits.
    return [[fill] * num_cols for _ in range(num_rows)]


def get_column(data, col_idx):
    # No way to extract a column without numpy so Just Deal.
    return [row[col_idx] for row in data]
