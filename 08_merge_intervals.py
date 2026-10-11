"""
08 - Merge Intervals                Target: 30 minutes

A list of intervals is given, each as [start, end]. Merge every pair that
overlaps and return the resulting list of non-overlapping intervals.
Intervals that only touch at an endpoint, such as [1, 4] and [4, 5], count as
overlapping and must be merged.

Constraints:
  1 <= len(intervals) <= 10000
  start <= end
  0 <= start, end <= 10^5
  the input is NOT sorted

Examples:
  ([[1, 3], [2, 6], [8, 10], [15, 18]],) -> [[1, 6], [8, 10], [15, 18]]
  ([[1, 4], [4, 5]],)                    -> [[1, 5]]

The first line of your plan should say what you do to the input before you
start merging anything.

--- WRITE YOUR PLAN HERE BEFORE YOU CODE ---
I am given an array of arrays with each inner array being made up of two numbers
that specify a range. I want to return an array of arrays that has the ranges
merged as in if two ranges are touching or inside of each other return the
complete range.

I am thinking first of how sorting might help me because if I can sort it then I can go in order, but how to sort?
Should I sort by the first number in the range?
Let me go through an example first ([[1,4], [4,5]]) => I first go through the array and find that the first array starts at 1 and
ends at 4. Then I see the second array with the start is 4 and end at 5. So now I know that that the interval should start at 1 and end at 5.

But here if I know the minimum is 1 and the maximum is 5 I can just create this interval to be [1,5]
Now if I go through the array and save the results in a hash table can I benefit?

But what would I save to the hash. I do not know actually.

Okay so other than that how do I actually identify this myself, I see the first array and think that I remember that it is starts
at 1 and ends at 4. I then see the second array and remember that it starts at 4 and ends at 5. Now I know that 1 is less than 4 so I know
that I can have an interval [1,4] I then know that 5 is greater than 4 the end of the first interval so I know that the interval should be
[1,5]

So the algo goes:
    go through the array and read the arrays
    I save the start of the first array
    I then save the end of the first array
    I move on to the next array
    I save the start of the second array
    I save the end of the second array
    I then find the minimum of the start and use it as the start of the new interval
    I then find the max of the ends and use it as the end of the new interval
    I return the final interval

But this works for two intervals that are connected or nested

Let us try it on intervals that are not connected or nested like ([2, 6], [8, 10])
    start of the first array is 2
    end of the first array is 6
    start of second array is 8
    end of second array is 10
    the minimum of the starts is 2
    the maximum of the ends is 10
    I return [2, 10]
    But this is wrong because the intervals are not connected and thus cannot be merged I should have returned [2,6] [8,10]

Ok so for them to be merged the end of the first array needs to be greater than or equal to the start of the second
so the algo goes now:
    go through the array and read the arrays
    I save the start of the first array
    I then save the end of the first array
    I move on to the next array
    I save the start of the second array
    I save the end of the second array
    check if the end of the first array is greater than or equal to the start of the second array:
        if it is continue the algo
        if not return both intervals
    I then find the minimum of the start and use it as the start of the new interval
    I then find the max of the ends and use it as the end of the new interval
    I return the final interval
now for the example [2,6] [8,10]
    start of the first array is 2
    end of the first array is 6
    start of second array is 8
    end of second array is 10
    the end of the first array is 6 not greater than or equal to the start of the second array
    I return [2, 6] [8, 10]

Ok that is correct but now let us try it for the original [1,4] [4,5]
    start of the first array is 1
    end of the first array is 4
    start of the second array is 4
    end of the second array is 5
    end of first array is greater than or equal to the start of the second array we continue
    the min of the starts is 1
    the max of the ends is 5
    I return [1, 5]

Ok what about nested like [2,3] [1,5]
    start of the first array is 2
    end of the first array is 3
    start of the second array is 1
    end of the second array is 5
    end of the first array is 3 greater than or equal to 1 so we continue
    the min of the starts is 1
    the max of the ends is 5
    I return [1,5]

Ok so the algo works for two arrays

how can I extend it? I am thinking of using a recursive approach where I do the first two arrays and use the merged interval from that
but what if the first two arrays do not create a merged interval then I do not gain anything
Ok what if I go through all the arrays and save the starts and the ends into two arrays

so if I get an input like [2,6] [8, 10] [1,4] [4,5] I know I should return [1, 6] [8, 10]
When I go through the main array I get two arrays [2, 8, 1, 4] [6, 10, 4, 5]

Okay let us try sorting this input by the first element
so the input becomes [1,4] [2,6] [4,5] [8,10]
If I am to run my algo then I first return [1,6] and have [4,5] and [8,10]
I should then return [1,6] and have to try it with [8,10] and return [1,6] [8,10]

Ok so the algo should go like this
    init result_list to empty list
    sort the big array by the first element in each sub array
    go through the sorted array
        if result_list is empty:
            run algorithm on the first two subarrays
            append result to result array
        if not
            run algorithm on the current input and the last element in result list
            append result to result list
    return result list

ok so given an input of [2, 6] [8, 10] [1,4] [4,5] [2,3]
    result_list = []
    sorted_array = [[1,4], [2,6], [2,3], [4,5], [8,10]]
    going through sorted array
        currently in [1,4]
        result_list is empty
            the start of the first array is 1
            the end of the first array is 4
            the start of the second array is 2
            the end of the second array 6
            the end of the first array is greater than or equal to the start of the second array we continue
            the min of the starts is 1
            the max of the ends is 6
            append to result list [1, 6]

        move on, currently in [2,6]                     #we should find a way to skip this work
            result_list last element is [1, 6]
                the start of the first array is 2
                the end of the first array is 6
                the start of the second array is 1
                the end of the second array is 6
                end of the first array is greater than or equal to the start of the second array we continue
                we get [1, 6], since it is in the result list we should continue

        currently in [2,3]
            result_list last element is [1, 6]
                the start of the first array is 2
                the end of the first array is 3
                the start of the second array is 1
                the end of the second array is 6
                end of the first array is geq than the second array we continue
                min of starts is 1
                max of ends is 6
                we get [1,6]
                it is in result_list we continue
        currently in [4, 5]
            result_list last element is [1,6]
                same thing goes and we continue
        currently in [8, 10]
            result_list last element is [1,6]
                start of first array is 8
                end of the first array is 10
                start of second array is 1
                end of the second array 6
                end of first array is greater than or equal to start of the second array
                we continue ##this is a bug we need to make sure that when comparing with the result list that the two
                arrays are considered in order
        so we need to create a helper function that takes two arrays and returns the result and in that helper function
        we make sure to sort which one to consider first

Ok for time and space complexity
I am sorting so we have O(nlogn) for the sorting then I loop for size of
the array of intervals so that is O(n) so the total time complexity is O(nlogn)
The space complexity is O(n) since I am creating a result_list with a worst case of all
intervals not overalapping
-------------------------------------------
"""

from harness import run_tests


def merge(intervals):
    result_list = []
    sorted_intervals = sorted(intervals)

    result_list.append([sorted_intervals[0][0], sorted_intervals[0][1]])

    for i in range(1, len(sorted_intervals)):
        last_merged = result_list[-1]
        current = sorted_intervals[i]

        end_of_first_interval = last_merged[1]

        start_of_second_interval = current[0]
        end_of_second_interval = current[1]

        if end_of_first_interval >= start_of_second_interval:
            result_list[-1][1] = max(end_of_first_interval, end_of_second_interval)
        else:
            result_list.append([current[0], current[1]])

    return result_list


CASES = [
    (([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
    (([[1, 4], [4, 5]],), [[1, 5]]),
    (([[1, 4], [0, 4]],), [[0, 4]]),
    (([[1, 4], [2, 3]],), [[1, 4]]),  # fully contained
    (([[5, 6], [1, 2]],), [[1, 2], [5, 6]]),  # unsorted input, no overlap
    (([[1, 1]],), [[1, 1]]),
    (([[1, 10], [2, 3], [4, 5], [6, 7]],), [[1, 10]]),
]

if __name__ == "__main__":
    run_tests(merge, CASES, normalize=sorted)
