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
I am given a matrix which is a 2d array
I am to return a list containing the elemnts but in a spiral order meaning I go
left to right then down then left then up then right in the example given
I am given hints that the traps are all in the single row and single column cases where the same cells can be visited twice

[[1],                     [1,2,3,4]
 [2], ==> [1,2,3,4]                 ===> [1,2,3,4]
 [3],
 [4]]

So in the cases where we have one row or one column we can just put it in a list

[1,2,3]
[4,5,6] ->
[7,8,9]

1 (0,0) -> index 0
2 (0,1) -> index 1
3 (0,2) -> index 2
We then need to jump one column down
6 (1,2) -> index 3
We then need to jump one column down
9 (2,2) -> index 4
Ok so when index is == max_row we jump down
When index == max_col we go left
8 (2,1) -> index 5
7 (2,0) -> index 6
We need then to jump up one row
4 (1,0) -> index 7
Now we cannot go up again we need to know to go right
5 (1,1) -> index 8
Okay so if a number has index i == j it jumps 4 indexes starting from 0 in a 3x3 matrix

Ok so the cases where we need to jump are first when we reach max column this changes the direction to down
Then the next case to jump is when we reach max row this changes the direction to left
Then the next case to jump is when we reach the 0th col this changes the direction to up
For the final jump it is when going up but we already visited the row so we go right again

Ok so we need a way to track which indexes where visited before, I am thinking of using a hash table to store the visited indexes

ok so the indexes we want to go through are 
(0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (2,0), (1,0), (1,1)

row -> col -> reverse row -> reverse col -> row -> col -> reverse row -> reverse col -> row

I need an algo like this:
init visited_hash = {}
init final_array = []

for row, line in enumerate(matrix):
    for col, num in enumerate(line):
        if [row,col] in visited_hash:
            continue
        if row == 0:
            visited_hash[num] = [row, col]
            final_array.append(num)
        if row == 1:
            

-------------------------------------------
"""
from harness import run_tests


def spiral_order(matrix):



CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    (
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],),
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    ),
    (([[1]],), [1]),
    (([[1, 2, 3, 4]],), [1, 2, 3, 4]),
    (([[1], [2], [3], [4]],), [1, 2, 3, 4]),
    (([[1, 2], [3, 4]],), [1, 2, 4, 3]),
    (([[1, 2], [3, 4], [5, 6]],), [1, 2, 4, 6, 5, 3]),
]

if __name__ == "__main__":
    run_tests(spiral_order, CASES)
