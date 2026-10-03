"""
02 - Two Sum                Target: 15 minutes

An array of integers nums and an integer target are given. Return the two
indices whose values add up to target. Exactly one such pair exists, and you
may not use the same index twice. Return the indices in any order.

Constraints:
  2 <= len(nums) <= 10000
  -10^9 <= nums[i] <= 10^9
  -10^9 <= target <= 10^9
  exactly one valid answer exists

Examples:
  ([2, 7, 11, 15], 9) -> [0, 1]
  ([3, 2, 4], 6)      -> [1, 2]
  ([3, 3], 6)         -> [0, 1]

Aim for one pass, O(n) time. If you write the nested loop first, keep it and
then improve it -- but note the improvement in your plan.

--- WRITE YOUR PLAN HERE BEFORE YOU CODE ---
I am given an array of integers and a target
I want to find which two elements of the array add up to the target
My time complexity goal is O(n), this means I need to go through the array only once

I am thinking of going through the array and calculating the difference between the element and the target
I will then save this element in a dict (hash table) with the value being the index of the element
But before saving it I will check if the difference already exists in the hash then I just return the index of the current elment
and the hashed index

algo is like this:
    init empty dict
    for num in nums:
        diff = target - num
        if diff in dict:
            return [dict[diff], indexofnum]
        dict[elem] = index

Time complexity: The work we are doing is going through the array so O(n) where n is the length of the array and a hash lookup
which is constant time O(1) so the time complexity is O(n)

Space complexity: We are creating a hash table with in the worst case n keys (when the target is made up of the first and last elements
) so space complexity is O(n) where n is the length of the array
-------------------------------------------
"""

from harness import run_tests


def two_sum(nums, target):
    elem_dict = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in elem_dict:
            return [elem_dict[diff], i]
        elem_dict[num] = i


CASES = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
    (([-1, -2, -3, -4, -5], -8), [2, 4]),
    (([0, 4, 3, 0], 0), [0, 3]),
    (([1, 2], 3), [0, 1]),
    (([-(10**9), 10**9], 0), [0, 1]),
]

if __name__ == "__main__":
    # index order does not matter, so compare as sorted pairs
    run_tests(two_sum, CASES, normalize=sorted)
