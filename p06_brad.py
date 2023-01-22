from utils import *


class School:
    def __init__(self, initial_comma_state_string):
        states = [int(x) for x in initial_comma_state_string.split(",")]
        self.__states = states
        self.__day    = 0

    def school_pass_day(self):
        next_states = []
        new_states  = []
        for state in self.__states:
            if state == 0:
                next_states += [6]
                new_states  += [8]
            else:
                next_states += [state - 1]

        self.__day += 1
        self.__states = next_states + new_states
        # print("After %02s days: %s" % (self.__day, self.__states))

    def school_get_total(self):
        return len(self.__states)



if __name__ == '__main__':
    sample, full = get_data_lines(6)
    for label, data, days, expected_total in [
                 ("First_test",  sample, 18, 26),
                 ("Second_test", sample, 80, 5934),
                 ("Real_data",   full,   80, 361169),
                 ("Real_data",   full,  256, -1),
          ]:
        print(f"STARTING {label}")
        school = School(data[0])
        for day in range(days):
            print(f"Now day {day}")
            school.school_pass_day()
        found_total = school.school_get_total()
        print(f"  {expected_total=} and {found_total=}")
        if expected_total != found_total:
            raise Exception("ALAS!")
        

        
