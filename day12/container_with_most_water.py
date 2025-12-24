"""
Container With Most Water
You are given an integer array heights where heights[i] represents the height of the 

  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""

from typing import List


class Solution:

    def maxArea(self, heights: List[int]) -> int:
        print(heights)
        res = 0
        l, r = 0, len(heights)-1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res


sol = Solution()
test = sol.maxArea([2, 2, 2])
print(test)
