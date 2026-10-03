"""
01 - Valid Anagram          Target: 15 minutes

Two strings are given, s and t. Return True when t uses exactly the same
letters as s, each the same number of times, in any order. Otherwise
return False.

Constraints:
  1 <= len(s), len(t) <= 50000
  both strings contain lowercase English letters only

Examples:
  ("anagram", "nagaram") -> True
  ("rat", "car")         -> False

Follow-up once it works: what changes if the input may contain any Unicode
character?

--- WRITE YOUR PLAN HERE BEFORE YOU CODE ---
    I need to find if two words are anagrams
    one way I already know is to sort and compare
    I can use a python set to do this easily

    I found that if using a set I get into the problem of when two strings are made up of the same characters but
    the count of the chars are different

    I would rather then either build a hash that counts each char and then compare the counts
    Or sort the strings and compare them

    I will go with the sort method

    Time and space complexity
    We use the sorted method twice so in the worst case time complexity is O(nlogn)
    Space complexity is O(n) as I am creating two new structures to hold the sorted strings


-------------------------------------------
"""

from harness import run_tests


def is_anagram(s: str, t: str) -> bool:
    char_count_dict_s = {}
    char_count_dict_t = {}

    for char in s:
        char_count_dict_s[char] = 0
    for char in t:
        char_count_dict_t[char] = 0

    for char in s:
        char_count_dict_s[char] += 1
    for char in t:
        char_count_dict_t[char] += 1
    if char_count_dict_t == char_count_dict_s:
        return True
    return False


CASES = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("a", "a"), True),
    (("a", "ab"), False),
    (("aacc", "ccac"), False),
    (("aabbcc", "abcabc"), True),
    (("ab", "ba"), True),
    ((" ", " "), True),
]

if __name__ == "__main__":
    run_tests(is_anagram, CASES)
