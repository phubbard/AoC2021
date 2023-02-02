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


if __name__ == '__main__':
    sample, full = get_data_lines(17)
    for dataset in [sample, full]:
        print(parse_input(dataset[0]))