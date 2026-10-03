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



-------------------------------------------
"""
from harness import run_tests


def merge(intervals):
    pass


CASES = [
    (([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
    (([[1, 4], [4, 5]],), [[1, 5]]),
    (([[1, 4], [0, 4]],), [[0, 4]]),
    (([[1, 4], [2, 3]],), [[1, 4]]),          # fully contained
    (([[5, 6], [1, 2]],), [[1, 2], [5, 6]]),  # unsorted input, no overlap
    (([[1, 1]],), [[1, 1]]),
    (([[1, 10], [2, 3], [4, 5], [6, 7]],), [[1, 10]]),
]

if __name__ == "__main__":
    run_tests(merge, CASES, normalize=sorted)
