"""
03 - Longest Common Prefix          Target: 15 minutes

A list of strings is given. Return the longest string that every one of them
starts with. Return the empty string when they share no starting characters.

Constraints:
  1 <= len(strs) <= 200
  0 <= len(strs[i]) <= 200
  lowercase English letters only

Examples:
  (["flower", "flow", "flight"],) -> "fl"
  (["dog", "racecar", "car"],)    -> ""

Watch the edge cases: one string in the list, an empty string in the list,
and the case where one string is a prefix of all the others.

--- WRITE YOUR PLAN HERE BEFORE YOU CODE ---
I am given a list of strings that may or may not share a common prefix
They must all share this common prefix
If they do not share a common prefix I am to return the empty string

I am thinking of looping throught the list of strings and save the first string and for each string delete the characters that
are not shared and return that as the final string

(["dog", "racecar", "car"],)
string is dog
string is empty
if empty return

(["flower", "flow", "flight"],)
string is flower
string is flow
string is fl
return string

Ok so the algo is:
    Init answer_str to strings[0]
    for string in strings starting from index 1:
        answer_str = answer_str - string
        if answer_str == "":
            return answer_str
    return answer_str

Here the answer_str = answer_str - string (finding the common elements) takes O(n) so the whole algorithm takes O(n) time
Space complexity I feel will be less than O(n) since I am only defining one variable that is at worse the length of the longest word in the strings array

I am getting stump on finding one prefix between two strings
For example [flowers, flow] should return flow
So what I can do is build a string where for each char in flowers if it is in flow I append it to the string
but what about the fact that flowers is longer than flow, this will lead to an index error
Maybe I should sort the strings and use the shortest string as the metric to compare against

Ok let me simplify the problem to just find the common prefix between two strings
I am given a list of two strings [flower, flows] I need to return flow

I am thinking of converting them to a list both
I need to sort them by length first
[f,l,o,w,s]
[f,l,o,w,e,r]

I loop through the shorter list and if the other list has the same character I append it to a new list

I am unable to do this problem

Ok how about I sort by length and then I use the shortest string as the answer and delete each char that differs
Ok this gave me a solution where I just delete from the shortest string all of the chars not shared with other strings
Also I have to break out when I find a differing character to avoid any index problems
And having the answer_list be initialized to the first strings handles the case of only one string or empty string as the loop does not execute

Now for time complexity:
I have one main loop runing n times and a nested loop that runs at the worst case n times (like ["same", "same", "same"])
Thus the time complexity is O(n^2) + O(nlogn) (for the sort)
The space complexity
I create two memory structures, one is size n (the sorted list) and one is the size of the longest string so space complexity is O(n)
So total complexity is O(n^2 + nlogn) + O(n)
-------------------------------------------
"""

from harness import run_tests


def longest_common_prefix(strs) -> str:
    if len(strs) == 0:
        return ""
    sorted_strs_list = sorted(strs, key=lambda x: len(x))
    answer_list = list(sorted_strs_list[0])

    for i in range(1, len(sorted_strs_list)):
        for j in range(len(answer_list)):
            if answer_list[j] is not list(sorted_strs_list[i])[j]:
                del answer_list[j:]
                break
    return "".join(answer_list)


CASES = [
    ((["flower", "flow", "flight"],), "fl"),
    ((["dog", "racecar", "car"],), ""),
    ((["interspecies", "interstellar", "interstate"],), "inters"),
    ((["single"],), "single"),
    ((["ab", "a"],), "a"),
    ((["", "abc"],), ""),
    ((["same", "same", "same"],), "same"),
    (([],), ""),
]

if __name__ == "__main__":
    run_tests(longest_common_prefix, CASES)
