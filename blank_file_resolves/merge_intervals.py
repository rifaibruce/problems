# merge intervals 30 min


def merge_intervals(intervals):
    # Sort intervals by start
    # Init return list to empty array
    # For each interval in intervals I want to see if its mergable with the last one in return list
    # If it is mergable merge, update return list and move on
    # If not then add it to return list
    # return return list

    sorted_intervals = sorted(intervals)
    return_list = [[sorted_intervals[0][0], sorted_intervals[0][1]]]  # avoid aliasing

    for i in range(1, len(sorted_intervals)):
        first_interval = return_list[-1]
        second_interval = sorted_intervals[i]

        start_of_first_interval = first_interval[0]
        end_of_first_interval = first_interval[1]

        start_of_second_interval = second_interval[0]
        end_of_second_interval = second_interval[1]

        if start_of_second_interval <= end_of_first_interval:
            return_list[-1] = [
                min(start_of_first_interval, start_of_second_interval),
                max(end_of_first_interval, end_of_second_interval),
            ]
        else:
            return_list.append([start_of_second_interval, end_of_second_interval])

    return return_list


# when to merge, we have [1,2] [2,3]
# We know they have to merge to [1,3]
# So we can check if the start of the second interval is less than or equal to the end of the first interval
# If so we merge
# Find an example where this fails
# let us try flipping them
# [2,3] [1,2] We know they merge to [1,3] we check the start of the second interval which is 1, it is less than the end of the first interval so we decide to merge
# Ok so this works for this
# We want two intervals that merge or dont merge and where the start of the second interval is less than the end of the first
# [8,10] [6,7] Here the start of the second interval is less than or equal to the end of the first so it merges when we dont want it to merge
# But we sort so how does sorting affect this, it would become [6,7], [8, 10]
# Here the start of the second is not less than or greater than the first, ok so we dont merge ==> correct behaviour, I think sort guarantees this to work then


intervals_a = [[1, 2], [3, 4], [0, 10]]
intervals_b = [[1, 2], [1, 2], [8, 10]]
intervals_c = [[1, 2], [8, 10], [2, 3], [4, 5], [1, 4], [4, 10]]
intervals_d = [[1, 2]]

assert merge_intervals(intervals_a) == [[0, 10]]
assert merge_intervals(intervals_b) == [[1, 2], [8, 10]]
assert merge_intervals(intervals_c) == [[1, 10]]
assert merge_intervals(intervals_d) == [[1, 2]]
