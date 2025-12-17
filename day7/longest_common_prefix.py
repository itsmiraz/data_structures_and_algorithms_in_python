# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

from typing import List


class Solution(object):
    def longestCommonPrefix(strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):  # first word's indexes
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

    def longestCommonPrefix(strs: List[str]) -> str:

        longest = min(strs, key=len)
        length = len(longest)

        for i in range(length):
            for j in strs:
                if longest[i] != j[i]:
                    return longest[:i]
        return longest


test = Solution.longestCommonPrefix(strs=["flower", "flow", "flight"])

print(test)
