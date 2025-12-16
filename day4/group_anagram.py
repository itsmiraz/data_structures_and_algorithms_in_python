# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

from typing import List
from collections import defaultdict


# {
# {a:1,b:3}: [abbb, babb]

# }


# New things here
# - ord Function that retruns a unicode value for a single string

class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())


test = Solution.groupAnagrams(
    strs=["act", "pots", "tops", "cat", "stop", "hat"])

print(test)
