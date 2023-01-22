from utils import *

if __name__ == '__main__':
    sample, full = get_data_lines(7)
    for tag, data, best_position, best_cost in [
                ("sample", sample,   2,      37),
                ("real",   full,   342,  351901),
            ]:
        parsed = data[0].split(',')
        parsed = [int(x) for x in parsed]
        print(f"{tag}: count is {len(parsed)}")
        min_extent = min(parsed)
        max_extent = max(parsed)
        print(f"{tag}: {min_extent=}")
        print(f"{tag}: {max_extent=}")

        min_cost   = None
        min_target = None
        for test_target in range(min_extent, max_extent + 1):
            total_cost = 0
            for crab_start in parsed:
                cost = abs(crab_start - test_target)
                total_cost += cost
                # print(f"{crab_start=} yields {total_cost=}")
            if min_cost is None or total_cost < min_cost:
                min_cost = total_cost
                min_target = test_target
                print(f"at {min_target=} better cost is {min_cost=}")
           
        found_best_cost = min_cost
        found_best_target = min_target         
        print(f"Lowest cost is {found_best_cost} found at {found_best_target}")
        if found_best_cost != best_cost:
            raise Exception("YOU SHALL NOT PASS")



