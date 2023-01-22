from utils import *

if __name__ == '__main__':
    sample, full = get_data_lines(7)
    for tag, data, best_linear_cost, best_gauss_cost in [
                ("sample", sample,     37,       168),
                ("real",   full,   351901, 101079875),
            ]:
        parsed = data[0].split(',')
        parsed = [int(x) for x in parsed]
        print(f"{tag}: count is {len(parsed)}")
        min_extent = min(parsed)
        max_extent = max(parsed)
        print(f"{tag}: {min_extent=}")
        print(f"{tag}: {max_extent=}")

        min_linear_cost   = None
        min_linear_target = None
        min_gauss_cost    = None
        min_gauss_target  = None
        for test_target in range(min_extent, max_extent + 1):
            total_linear_cost = 0
            total_gauss_cost = 0

            for crab_start in parsed:
                distance = abs(crab_start - test_target)
                linear_cost = distance
                total_linear_cost += linear_cost
                gauss_cost = int(distance * (distance + 1) / 2)
                total_gauss_cost += gauss_cost
                # print(f"{crab_start=} yields {total_linear_cost=}")
            if min_linear_cost is None or total_linear_cost < min_linear_cost:
                min_linear_cost = total_linear_cost
                min_linear_target = test_target
                # print(f"at {min_linear_target=} better cost is {min_linear_cost=}")
            if min_gauss_cost is None or total_gauss_cost < min_gauss_cost:
                min_gauss_cost = total_gauss_cost
                min_gauss_target = test_target
                # print(f"at {min_gauss_target=} better cost is {min_gauss_cost=}")

        found_best_linear_cost   = min_linear_cost
        found_best_linear_target = min_linear_target

        found_best_gauss_cost   = min_gauss_cost
        found_best_gauss_target = min_gauss_target

        print(f"Lowest linear cost is {found_best_linear_cost} found at {found_best_linear_target}")
        print(f"Lowest gauss cost is {found_best_gauss_cost} found at {found_best_gauss_target}")
        if found_best_linear_cost != best_linear_cost:
            raise Exception("YOU SHALL NOT PASS")
        if found_best_gauss_cost != best_gauss_cost:
            raise Exception("YOU SHALL NOT GAUSS PASS")



