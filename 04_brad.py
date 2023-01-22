from copy import deepcopy
from utils import make_2d_array, get_column, get_data_lines
from utils_04 import is_bingo


DIMENSION = 5

class Board:

    def __init__(self, five_strings):
        raw_2d = []
        called_2d = []
        for line in five_strings:
            raw_2d.append([int(x) for x in line.split()])
            called_2d.append([0] * DIMENSION)

        self.__values = raw_2d
        self.__called = called_2d
        self.__score  = None

        assert len(self.__values)    == DIMENSION
        assert len(self.__values[2]) == DIMENSION
        assert len(self.__called)    == DIMENSION
        assert len(self.__called[2]) == DIMENSION

    def board_show(self, print_func):
        for row_index in range(DIMENSION):
            row = ""
            for col_index in range(DIMENSION):
                value  = self.__values[row_index][col_index]
                called = self.__called[row_index][col_index]
                pre  = ' '
                post = ' '
                if called > 0:
                    pre  = '<'
                    post = '>'
                entry = f"{pre}{value:02}{post} "
                row += entry
            print_func(row)

    def board_mark(self, drawn_number):
        for row_index in range(DIMENSION):
            for col_index in range(DIMENSION):
                value  = self.__values[row_index][col_index]
                if value == drawn_number:
                    self.__called[row_index][col_index] = 1


    def board_score(self, drawn_number):
        """Returns None if no bingo, board score otherwise."""

        if not is_bingo(self.__called):
            return None

        sum = 0
        for row_index in range(DIMENSION):
            for col_index in range(DIMENSION):
                value  = self.__values[row_index][col_index]
                called = self.__called[row_index][col_index]
                if not called:
                    sum += value
        score = sum * drawn_number
        self.__score = score
        return score

    def board_get_score(self):
        return self.__score

def part_one(data_2d):
    def _next(): return data_2d.pop(0)
    number_draw_list = [int(x) for x in _next().split(',')]
    board_list = []
    while len(data_2d) > 0:
        _next() # discard empty line
        board = Board([_next() for _ in range(DIMENSION)])
        board_list.append(board)

    print(f"Saw {len(board_list)} boards!")
    for drawn_number in number_draw_list:
        print(f"Next is -> {drawn_number}")
        for board in board_list:
            board.board_mark(drawn_number)

            score = board.board_score(drawn_number)
            if score is not None:
                board.board_show(print)
                print(f"SCORE IS {score}")
                return
    raise Exception("UNEXPECED NOT FOUNd")

def part_two(data_2d):
    def _next(): return data_2d.pop(0)
    number_draw_list = [int(x) for x in _next().split(',')]
    board_list = []
    completed_board_list = []
    while len(data_2d) > 0:
        _next() # discard empty line
        board = Board([_next() for _ in range(DIMENSION)])
        board_list.append(board)

    print(f"Saw {len(board_list)} boards!")
    for drawn_number in number_draw_list:

        board_list = list(filter(lambda x: x not in completed_board_list, board_list))

        print(f"Next is -> {drawn_number}")
        for board in board_list:
            board.board_mark(drawn_number)

            score = board.board_score(drawn_number)
            if score is not None:
                board.board_show(print)
                print(f"SCORE IS {score}")
                completed_board_list.append(board)

    last_score = completed_board_list[-1].board_get_score()
    print(f"There are {len(completed_board_list)} and last score is {last_score}")


               
        
        



if __name__ == '__main__':

    sample, full = get_data_lines(4)
    for step in [sample, full]:
        part_one(deepcopy(step))
        part_two(deepcopy(step))
