# problems

Algorithm and data-structure practice in Python. Each file contains the
problem statement, my written plan and reasoning, the solution, and its tests,
including the dead ends, since how I got to the answer matters as much as the
answer.

## Running

Each file runs on its own. Keep `harness.py` in the same folder:

```
python 01_valid_anagram.py
```

The harness prints how many tests passed and, for any failure, the input, the
expected output, and what the function actually returned.

## How I work each problem

1. Write the plan in the docstring before writing any code.
2. Time-box the attempt. If I use a hint, I note it and re-solve the problem
   from a blank file two days and one week later.
3. Add my own edge cases, such as empty input, duplicates, and size limits,
   beyond the given tests.
4. State time and space complexity, with every variable defined.

## Progress

| # | Problem | Approach | Time | Space |
| --- | --- | --- | --- | --- |
| 01 | Valid Anagram | Sort and compare | O(n log n) | O(n) |
| 02 | Two Sum | One pass, value-to-index dictionary | O(n) | O(n) |
| 03 | Longest Common Prefix | Trim the shortest string at the first mismatch | O(m·k) | O(k) |
| 04 | Valid Sudoku | One pass with row, column, and box sets | O(1) fixed board; O(n²) for n×n | O(1) fixed; O(n²) for n×n |
| 05 | Group Anagrams | Character-count key, `frozenset` of `Counter` items | O(n·m) | O(n·m) |
| 06 | Rotate Image | Transpose in place, then reverse each row | O(n²) | O(1) |
| 07 | Spiral Matrix | | | |
| 08 | Merge Intervals | | | |
| 09 | Longest Consecutive Sequence | | | |

Variables: n is the number of elements or strings, m is string length,
k is the length of the shortest string. For grids, n is the side length.
