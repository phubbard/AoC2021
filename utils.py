
def clean_lines(input_lines):
    # Remove newlines and such that fuck up the parser
    return [x.strip() for x in input_lines]


def make_2d_array(num_rows, num_cols, fill=0):
    # Create and allocate a 2D array. Copypasta from SO with edits.
    return [[fill] * num_cols for _ in range(num_rows)]


def get_column(data, col_idx):
    # No way to extract a column without numpy so Just Deal.
    return [row[col_idx] for row in data]


def get_data_lines(problem_number):
    # Return a tuple of (sample data, full data)
    # Based on the problem number. Normal
    # pattern is to have line-specific parsers that operate on the return from this.
    sample_file = f'./data/{problem_number}s.txt'
    data_file = f'./data/{problem_number}.txt'

    sample_data = clean_lines(open(f'./data/{problem_number}s.txt', 'r').readlines())
    full_data = clean_lines(open(f'./data/{problem_number}.txt', 'r').readlines())
    return (sample_data, full_data)