2026-09-24

- Did: LCP, Two Sum (hint), started Valid Sudoku
- Stuck on: going from O(n²) to O(n) on Two Sum — kept
  reaching for a second pass instead of building the dict as I go
- Learned: dict lookup is O(1); enumerate over range(len(...))
- Re-solve: Two Sum blank on 9/26 and 10/1

2026-09-25

- Did valid sudoku first through only completing a search through rows and cols only
- Then used hints from claude to be able to search 3x3 boxes in the sudoku
- Made a mistake in complexity analysis where I generalized time complexity but not the space complexity

2026-09-26

- Resolved two-sum with O(n)
- Solved group_anagrams with O(n * m)
- Learned about the Counter subclass and the .get method to have it return a default value instead of a key error in a dict
- Learned when to use defaultdict and what to use it before
