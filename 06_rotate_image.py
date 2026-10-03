"""
06 - Rotate Image                   Target: 30 minutes

An n x n matrix of integers is given. Rotate it 90 degrees clockwise, in
place. Do not allocate another matrix; change the one you were given and
return None.

Constraints:
  1 <= n <= 20
  -1000 <= matrix[i][j] <= 1000

Example:
  [[1, 2, 3],        [[7, 4, 1],
   [4, 5, 6],   ->    [8, 5, 2],
   [7, 8, 9]]         [9, 6, 3]]

Do a 3x3 and a 4x4 on paper first and watch where each element lands. There
is a two-step way to do this using operations you already know.

--- WRITE YOUR PLAN HERE BEFORE YOU CODE ---
I am given a matrix which is a 2d array of dimention n
I want to modify this matrix without creating a new matrix such that the matrix is rotated 90 degrees
clockwise

Examples: 1 (0,0) --> (0, 2)
          2 (0,1) --> (1, 2)
          3 (0,2) --> (2, 2)
          4 (1,0) --> (0, 1)
          5 (1,1) --> (1, 1)
          6 (1,2) --> (2, 1)
          7 (2,0) --> (0, 0)
          8 (2,1) --> (1, 0)
          9 (2,2) --> (2, 0)
Ok so one thing is constant that the column becomes the row for each one
And the column is the max_col - row

Since I cannot allocate another matrix I would need to track the indexes for all the elements
as I am going through the matrix and then go again and put each element at the right place
I am thinking of using a hash to keep track of the indexes as a list so 1 in our example would be
{1: [0,2],
            }
So the algo looks like this:
Init empty hash
init max_col = len(matrix) - 1
for row in matrix:
    for col in matrix:
        hash[matrix[row][col]] = [col, max_col - row]

for number in hash:
    row = hash[number][0]
    col = hash[number][1]

    matrix[row][col] = number

return None

Time complexity is O(n^2) Since we go through each element in the matrix
Space complexity is O(n^2) since we create a dict that has one entry for each entry in the matrix

Ok so I did not consider the case of duplicate entries and also I should not be allocating an index
the size of a matrix so I need to change my approach

Ok I got a hint from Claude I can split the operation into two steps
1. Transpose the matrix
2. Reverse the matrix rows

It is telling me though to check for the transpose whether each pair of cells gets swapped
once or twice

Also how do I transpose the matrix without losing the elments that were in the
index I am moving to

[[1,2,3],       [[1,4,7],
 [4,5,6], ===>   [2,5,8],
 [7,8,9]]        [3,6,9]]

Ok so for transposing a matrix what are we doing?
each row becomes a col, and each col becomes a row
so step by step on our example we are at 0,0 which has 1 its new index is 0,0
0,1 has 2 its new index will be 1,0 but we have 4 at 1,0 4 will become 0,1 so we can do both at the same time

ok so we can skip over diagonals in our transpose as it doesn't matter and for the rest we save the number in a temp buffer
and do two operations

Algo for transpose is:
for row, line in enumerate(matrix):
    for col, number in enumerate(line):
        if row == col:
            continue;
        temp = matrix[col][row]
        matrix[col][row] = number
        matrix[row][col] = temp

[[1,2,3],       [[1,2,3],       [[1,4,3],       [[1,4,7],     [[1,2,7],
 [4,5,6], ==>    [4,5,6], ===>   [2,5,6], ===>   [2,5,6], ==>  [4,5,6], BUG
 [7,8,9]]        [7,8,9]]        [7,8,9]]        [3,8,9]]      [3,8,9]]

But this has a bug because it reverses its own effects as it goes through the matrix
I guess this is the hint claude was warning about
Well once we go through a row we know we are done modifying it so maybe we can use that
like once we have 1,4,7 now our row becomes 1 > 0 so we know any modification with row less than 1 is wrong
We also know that col 0 is done too so maybe if the current row is greater than the col we continue

Ok so Time complexity is O(n^2) assuming row.reverse() takes O(n)
Space complexity is O(1)
-------------------------------------------
"""

from harness import run_tests


def rotate(matrix) -> None:
    for row, line in enumerate(matrix):
        for col, number in enumerate(line):
            if row == col or row > col:
                continue
            temp = matrix[col][row]
            matrix[col][row] = number
            matrix[row][col] = temp
    for row in matrix:
        row.reverse()

    return None


CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    (([[1]],), [[1]]),
    (([[1, 2], [3, 4]],), [[3, 1], [4, 2]]),
    (
        ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],),
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    ),
    (([[0, 0], [0, 0]],), [[0, 0], [0, 0]]),
    (([[5, 1, 9], [5, 1, 9], [13, 3, 6]],), [[13, 5, 5], [3, 1, 1], [6, 9, 9]]),
]

if __name__ == "__main__":
    # the answer is the mutated input, not the return value
    run_tests(rotate, CASES, mutates=True)
