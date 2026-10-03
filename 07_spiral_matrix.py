"""
07 - Spiral Matrix                  Target: 35 minutes

An m x n matrix is given. Return a flat list of all its elements, read in
spiral order: left to right across the top row, down the right column, right
to left across the bottom row, up the left column, then inward and repeat.

Constraints:
  1 <= m, n <= 10
  -100 <= matrix[i][j] <= 100
  the matrix is not necessarily square

Example:
  [[1, 2, 3],
   [4, 5, 6],   ->  [1, 2, 3, 6, 9, 8, 7, 4, 5]
   [7, 8, 9]]

The traps are all in the single-row and single-column cases, where the same
cells can be visited twice. Test a 1x4 and a 4x1 before you trust it.

--- WRITE YOUR PLAN HERE BEFORE YOU CODE ---



-------------------------------------------
"""
from harness import run_tests


def spiral_order(matrix):
    pass


CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
     [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    (([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],),
     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    (([[1]],), [1]),
    (([[1, 2, 3, 4]],), [1, 2, 3, 4]),
    (([[1], [2], [3], [4]],), [1, 2, 3, 4]),
    (([[1, 2], [3, 4]],), [1, 2, 4, 3]),
    (([[1, 2], [3, 4], [5, 6]],), [1, 2, 4, 6, 5, 3]),
]

if __name__ == "__main__":
    run_tests(spiral_order, CASES)
