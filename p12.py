
import collections

from utils import *
from copy import deepcopy

def log(line):
    print(f"P12: {line}")


MAGIC_START_CAVE = 'start'
MAGIC_END_CAVE   = 'end'


class Link:
    def __init__(self, cave_from, cave_to):
        self.LINK_FROM = cave_from
        self.LINK_TO   = cave_to

    def link_does_not_involve(self, cave):
        if self.LINK_FROM == cave: return False
        if self.LINK_TO   == cave: return False
        return True


class Cave:
    def __init__(self, name):
        self.CAVE_NAME     = name
        self.CAVE_IS_SMALL = name == name.lower()

    def cave_is_not(self, other_cave):
        return self != other_cave


class Warren:
    def __init__(self, optional_deepcopy_warren, optional_remove_cave):
        remove_cave = None
        if optional_remove_cave and optional_remove_cave.CAVE_IS_SMALL:
            remove_cave = optional_remove_cave

        if optional_deepcopy_warren:
            self.__caves = [cave for cave in optional_deepcopy_warren.__caves if cave.cave_is_not(remove_cave)]
            self.__links = [link for link in optional_deepcopy_warren.__links if link.link_does_not_involve(remove_cave)]
        else:
            self.__caves = []
            self.__links = []
    
    def warren_add_link(self, name_a, name_b):
        cave_a = self.warren_locate_named(name_a)
        cave_b = self.warren_locate_named(name_b)
        self.__links += [Link(cave_a, cave_b), Link(cave_b, cave_a)]

    def warren_locate_named(self, name):
        for cave in self.__caves:
            if name == cave.CAVE_NAME: return cave
        cave = Cave(name)
        self.__caves += [cave]
        return cave

    def warren_list_connected_caves(self, cave):
        rv = collections.OrderedDict()
        for link in self.__links:
            if link.LINK_FROM == cave:
                rv[link.LINK_TO] = True
        return rv.keys()


class Path:
    def __init__(self, optional_preceeding_path, next_cave):
        caves = optional_preceeding_path.__sequence if optional_preceeding_path else []
        self.__sequence = [cave for cave in caves] + [next_cave]

    def path_get_last_cave(self):
        return self.__sequence[-1]

    def __str__(self):
        return ",".join(cave.CAVE_NAME for cave in self.__sequence)


if __name__ == '__main__':
    sample, full = get_data_lines(12)
    for raw_lines, expected_answer in [
                (sample, 226),
                (full,   -1),
            ]:
        initial_warren = Warren(None, None)
        for line in raw_lines:
            cave_list = line.split('-')
            initial_warren.warren_add_link(cave_list[0], cave_list[1])
        start_cave = initial_warren.warren_locate_named(MAGIC_START_CAVE)
        end_cave   = initial_warren.warren_locate_named(MAGIC_END_CAVE)
        start_path = Path(None, start_cave)
        candidate_warrens = collections.OrderedDict() # Path: Warren
        candidate_warrens[start_path] = initial_warren

        completed_paths = []

        while True:
            log(f"in this lap there are {len(candidate_warrens)}")

            if len(candidate_warrens) == 0: break
            working_warrens = candidate_warrens
            candidate_warrens = collections.OrderedDict() # Path: Warren
            for a_path, a_warren in working_warrens.items():
                last_cave = a_path.path_get_last_cave()
                next_caves = a_warren.warren_list_connected_caves(last_cave)
                for next_cave in next_caves:
                    next_path = Path(a_path, next_cave)
                    if next_cave == end_cave:
                        completed_paths += [next_path]
                        log(f"{next_path}")
                    else:
                        next_warren = Warren(a_warren, next_cave)
                        candidate_warrens[next_path] = next_warren
        log(f"Path count is {len(completed_paths)}")


        


