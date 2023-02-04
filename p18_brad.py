
from utils import get_data_lines

class Number:
    def __init__(self, value, hosting_pair):
        self.NUMBER_HOSTING_PAIR = pair

        self.__number_value         = value
        self.__current_left_number  = None
        self.__current_right_number = None

    def number_set_current_left(self, number_on_left):
        self.__current_left_number  = number_on_left

    def number_set_current_right(self, number_on_right):
        self.__current_right_number = number_on_right

    def number_current_neighbors(self):
        return (self.__current_left_number, self.__current_right_number)

    def __str__(self):
        return str(self.__number_value)


class Pair:
    def __init__(self, number_or_pair_left, number_or_pair_right):
        self.PAIR_LEFT_SIDE  = number_or_pair_left
        self.PAIR_RIGHT_SIDE = number_or_pair_right

        self.__current_depth = None


    def pair_normalize(self, parent_depth):
        """Reforge all links noted as 'current'"""
        leftmost_number   = None
        rightmost_number  = None
        right_of_leftmost = None
        left_of_rightmost = None
        self.__current_depth = parent_depth + 1
        if isinstance(self.PAIR_LEFT_SIDE, Pair):
            leftmost_number, right_of_leftmost = self.PAIR_LEFT_SIDE.pair_normalize(self.__current_depth)
        else:
            leftmost_number = self.PAIR_LEFT_SIDE
        if isinstance(self.PAIR_RIGHT_SIDE, Pair):
            left_of_rightmost, rightmost_number = self.PAIR_RIGHT_SIDE.pair_normalize(self.__current_depth)
        else:
            rightmost_number = self.PAIR_RIGHT_SIDE

        if right_of_leftmost and left_of_rightmost:
            right_of_leftmost.number_set_current_right(left_of_rightmost)
            left_of_rightmost.number_set_current_left(right_of_leftmost)
        elif right_of_leftmost:
            left_of_rightmost.number_set_current_right(rightmost_number)
            rightmost_number.number_set_current_left(left_of_rightmost)
        elif left_of_rightmost:
            right_of_leftmost.number_set_current_right(leftmost_number)
            leftmost_number.number_set_current_left(right_of_leftmost)
        else:
            leftmost_number.number_set_current_right(rightmost_number)
            rightmost_number.number_set_current_left(leftmost_number)

        return (leftmost_number, rightmost_number)

    def __str__(self):
        left  = str(self.PAIR_LEFT_SIDE)
        right = str(self.PAIR_RIGHT_SIDE)
        return "[" + left + "," + right + "]"


def add_pairs(pair_left, pair_right):
    new_pair = Pair(pair_left, pair_right)


def make_into_pair(a_tuple):
    pass


def construct_from_raw(raw_string):
    as_tuples = eval(raw_string.replace('[', '(').replace(']', ')'))


if __name__ == '__main__':
    sample, full = get_data_lines(18)

    for dataset, expected_a in [
                (sample, -1),
                (full,   -1),
            ]:
        print(f"{expected_a=}")

    raw_value = "[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]"

    print(f"{as_tuples=}")

