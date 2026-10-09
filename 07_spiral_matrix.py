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

After reviewing a hint I found out that I need to not use a nested matrix but rather loop over m*n
Then use tuples to specifiy direction (using them as direction vectors) and add the direction I want to go
I then need to loop through the matrix and for each index decide where will it move next, so I need to extract the row and col
of the index I am in, how do I do that?

Maybe I have two variables one is the current position initialized to (0, 0) and current direction that should be initialized
to (0, 1). Then I loop through each element and check against current position to see if I need to change direction or not

So algo goes something like this:
Init answer_list to empty list
Init direction set to set of directions for right, down, left, up
Init current postion to (0,0)
Init current_direction to set[0]
Init row num to number of rows
Init col num to number of cols
Init size to row num * col num

for the total size of the matrix:
    If current_position == (0, 0) and value not in answer_list:
        answer_list.append(value)
    If current_position[1] == num of cols:
        current_direction = direction_list[1]
    If current_position[0] == num of rows:
        current_direction = direction_list[2]
    If current_position[1] == 0:
        current_direction = direction_list[3]
    If current_direction == (0,1) and we value up is visited:
        current_direction = direction_list[0]
    answer_list.append(value)
    current_position += current_direction
-------------------------------------------
"""

from harness import run_tests


def spiral_order(matrix):
    answ_list = []
    visited_set = set()
    dir_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0

    curr_row = 0
    curr_col = 0

    row_num = len(matrix)
    col_num = len(matrix[0])
    size_of_matrix = row_num * col_num

    for i in range(size_of_matrix):
        dir_r, dir_c = dir_list[dir_idx]

        answ_list.append(matrix[curr_row][curr_col])
        visited_set.add((curr_row, curr_col))

        next_r, next_c = curr_row + dir_r, curr_col + dir_c

        if (
            not (0 <= next_r < row_num and 0 <= next_c < col_num)
            or (next_r, next_c) in visited_set
        ):
            dir_idx = (dir_idx + 1) % 4
            dir_r, dir_c = dir_list[dir_idx]
            next_r, next_c = curr_row + dir_r, curr_col + dir_c

        curr_row, curr_col = next_r, next_c

    return answ_list


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
    ((([[1], [2], [3], [4], [5]],)), ([1, 2, 3, 4, 5])),
    (
        (([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],)),
        ([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ),
]

if __name__ == "__main__":
    run_tests(spiral_order, CASES)
