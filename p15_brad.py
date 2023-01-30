from utils import get_data_lines

#
#   1 a 1 b 6
#   c   d   e
#   1 f 3 g 8
#   h   i   j
#   2 k 1 l 3
#
 
# EDGE A

#  https://networkx.guide/algorithms/shortest-path/dijkstra/

class Cave:
    def __init__(self, utils_2d_array):
        rows = len(utils_2d_array)
        cols = len(utils_2d_array[0])
        edges

        for row in range(rows - 1):
            for col in range(cols - 1):
                edge = ()

    def cave_build_nx_edges(self):
        pass


if __name__ == '__main__':
    sample_2d, full_2d = load_2d_arrays(15)

    for dataset, expected_a in [
                (sample_2d, 40),
                (full_2s,   -1),
            ]:
        print(f"{expected_a=}")
    print(f"Done")

