"""
05 - Group Anagrams                 Target: 25 minutes

A list of strings is given. Group together the strings that are rearrangements
of each other, and return the groups as a list of lists. The groups may come
back in any order, and the strings within a group may be in any order.

Constraints:
  1 <= len(strs) <= 10000
  0 <= len(strs[i]) <= 100
  lowercase English letters only

Example:
  (["eat", "tea", "tan", "ate", "nat", "bat"],)
    -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Think about what all members of a group have in common, and how you would
turn that into a dictionary key. There is more than one workable key.

--- WRITE YOUR PLAN HERE BEFORE YOU CODE ---

Ok I am given a list of strings
I need to find which of those strings are anagrams of each other and group them into sublists
I then need to join the sublists into a list and return a list of lists

I am given a hint to look for something that all of the strings have in common and think about how that can be a dict key

I am thinking that maybe all anagrams are going to have the same length so I know that each sublist of anagrams is going to be
made up of the same length strings, is this what I should be thinking of as keys to the dict

Also I am thinking that each entry in the dict will be used to create the sublists, so the algorithm will need to build up the dict
and then at the end build up the list of lists from the dict entries

I could also have the keys of the dict be the sorted string since each anagram is going to be the same string when sorted

Claude told me previously that using a counter would lead to O(n) instead of O(nlogn) that is used in the sorting method in
01_valid_anagram

What does it mean by a counter though? I think it means to use a dict to count the number of chars in each string

Ok so I think I can go for each string in the list and group them by length in a dict

I then for each string I have a dict that counts the number of chars

Or maybe I create a dict for each string and have it have the counts of each letter in there and then use this dict as a key in the
bigger dict to hold the list of strings that have the same dict count and then use that to create the list of lists

Ok so the alog would be:
    init empty global dict
    init empty answers list
    for str in strs:
        init counter_dict to a dict with chars as keys and zeroes as the values for each key
        for char in str:
            counter_dict[char] += 1
        global_dict[counter_dict] = str
    collapse each key value into a list and add it to answers list

This algo looks like it will need O(n * m) time complexity where n is the length of the strs array and m is the length of the string
being looped over

For the space complexity I will need a dict that will have at the worst case n different entries (where all of the strings are not anagrams)
Same goes for the answers list I would at worst have n different lists in answers list
I also create a counter dict for each string so n dicts that have m entries so the O(n) for the global dict, O(n) for the answers list
then I will have n * O(m) for the counter dicts

I discovered that I cannot use a dict as a key in another dict, I can change the dict into an unhashable type and then use it as
a key

Actual time complexity is still O(n * m) since frozenset is O(n)
Actual space complexity is O(n * m) also since we are creating n counter_dicts that hold m keys

-------------------------------------------
"""

from harness import run_tests
from collections import Counter, defaultdict


def group_anagrams(strs):
    global_dict = defaultdict(list)
    for str_to_check in strs:
        counter = Counter(str_to_check)
        global_dict[frozenset(counter.items())].append(str_to_check)
    return list(global_dict.values())


CASES = [
    (
        (["eat", "tea", "tan", "ate", "nat", "bat"],),
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
    ),
    (([""],), [[""]]),
    ((["a"],), [["a"]]),
    ((["abc", "bca", "cab"],), [["abc", "bca", "cab"]]),
    ((["ab", "cd", "ef"],), [["ab"], ["cd"], ["ef"]]),
    ((["", "", "b"],), [["", ""], ["b"]]),
]


def normalize(groups):
    # group order and within-group order do not matter
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    run_tests(group_anagrams, CASES, normalize=normalize)
