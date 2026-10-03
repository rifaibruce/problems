"""
04 - Valid Sudoku                   Target: 30 minutes

A 9x9 grid is given as a list of lists of single characters. Filled cells hold
the characters "1" through "9"; empty cells hold ".". Decide whether the grid
as it stands breaks any Sudoku rule:

  - no digit repeats within a row
  - no digit repeats within a column
  - no digit repeats within any of the nine 3x3 boxes

Only the filled cells matter. The grid does not have to be solvable, and you
are not asked to solve it.

Constraints:
  the grid is always 9 x 9
  every cell is a digit "1"-"9" or "."

Useful fact: the 3x3 box containing row r and column c has index
  (r // 3) * 3 + c // 3
Work out why that formula holds before you use it.

--- WRITE YOUR PLAN HERE BEFORE YOU CODE ---
    I am thinking of simplifying the problem to first just check for rows and cols
    I have nine rows and nine cols
    They are represented in a list of lists where each nested list is a row
    [[], [], []
     [], [], []
     [], [], []]
    So if I was to check each row I would need a nested loop that goes through each nested list and checks for duplicates
    And if I was to check each col I would also need a nested loop that goes through each list but instead of checking for the
    numbers in the same list I would need to compare the jth index for different lists

    To first simplify the problem let me first just check for duplicates in the rows
    Algo:
        for row in grid:
            for num in row:
                init empty hash
                if num in hash:
                    return false
                else:
                    hash[num] = 1
    Now we decide to handle columns the algorithm will be the same but now we will look at the columns

    This is working for 6/7 tests I am still not testing for the duplicate in the 3x3 box currently the time complexity is O(n * m) where n is
    the number of rows and m is the number of cols and since the grid is 9x9 it is O(n^2)
    The space complexity is going to be O(n^2) too since in the worst case where I have to go through the whole board and each number is unique
    I will have to fill in the dict with the all of the numbers and since it is twice it is O(2n^2) for space and O(2n^2) for time

    To check each 3x3 box I think I will have to use this formula
    (r // 3) * 3 + c // 3
    But the hint says that the 3x3 grid containing the row r and col c has the index given by this formula but does that mean indexes out
    of the board like box 1,2,3,4,5,6,7,8,9

    Another hint I got from claude was that I would need 9 live dicts for each box

    ----------------------------------------------------------
    Now I completed the question and collapsed the three loops into one, the loop is a nested loop so the time complexity is O(n^2)
    I create three lists that have 9 sets with each set having a maximum of 9 elements so space complexity I assume is constant so O(1)
    For the complexity I should have noticed that since the problem space is a constant 9x9 board then both time complexity and space complexity
    are constant ---> O(1)

    For a generalized nxn board:
    There is a nested loop so the time complexity is O(n^2)
    We set up 3 lists with n sets that hold n elements so also the space complexity is O(n^2)

-------------------------------------------
"""

from harness import run_tests


def is_valid_sudoku(board) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for row, line in enumerate(board):
        for col, num in enumerate(line):
            if num == ".":
                continue
            box_index = (row // 3) * 3 + col // 3
            if num in rows[row]:
                return False
            rows[row].add(num)
            if num in cols[col]:
                return False
            cols[col].add(num)
            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)

    return True


def make(rows):
    return [list(r) for r in rows]


VALID = make(
    [
        "53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79",
    ]
)

# first cell changed 5 -> 8, which collides with the 8 in column 0
COLUMN_CLASH = make(
    [
        "83..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79",
    ]
)

EMPTY = make(["." * 9 for _ in range(9)])


def empty_with(cells):
    grid = make(["." * 9 for _ in range(9)])
    for r, c, v in cells:
        grid[r][c] = v
    return grid


CASES = [
    ((VALID,), True),
    ((COLUMN_CLASH,), False),
    ((EMPTY,), True),
    ((empty_with([(0, 0, "1"), (0, 8, "1")]),), False),  # row clash
    ((empty_with([(0, 0, "1"), (8, 0, "1")]),), False),  # column clash
    ((empty_with([(0, 0, "1"), (1, 1, "1")]),), False),  # box clash
    ((empty_with([(0, 0, "1"), (1, 3, "1")]),), True),  # different box, row, column
]

if __name__ == "__main__":
    run_tests(is_valid_sudoku, CASES)
