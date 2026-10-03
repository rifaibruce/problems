"""
09 - Longest Consecutive Sequence   Target: 30 minutes (stretch problem)

An unsorted array of integers is given. Return the length of the longest run
of consecutive integers present in it. The numbers do not have to be adjacent
in the array.

Constraints:
  0 <= len(nums) <= 100000
  -10^9 <= nums[i] <= 10^9
  duplicates are allowed

Examples:
  ([100, 4, 200, 1, 3, 2],)     -> 4   (the run 1, 2, 3, 4)
  ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],) -> 9

Sorting solves this in O(n log n). The point of the problem is the O(n)
solution: think about which numbers are worth starting a count from, and how
you would recognise one in O(1).

--- WRITE YOUR PLAN HERE BEFORE YOU CODE ---



-------------------------------------------
"""
from harness import run_tests


def longest_consecutive(nums) -> int:
    pass


CASES = [
    (([100, 4, 200, 1, 3, 2],), 4),
    (([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],), 9),
    (([],), 0),
    (([1],), 1),
    (([1, 1, 1],), 1),
    (([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],), 7),
    (([10, 20, 30],), 1),
]

if __name__ == "__main__":
    run_tests(longest_consecutive, CASES)
