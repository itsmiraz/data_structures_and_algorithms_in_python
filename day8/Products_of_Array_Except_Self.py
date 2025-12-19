# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20

from typing import List


class Solution:
    def productExceptSelfV2(nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length

        for i in range(length):
            prod = 1
            for j in range(length):
                print(i, j)
                if nums[i] == nums[j] and i == j:

                    continue
                prod *= nums[j]

            res[i] = prod

        return res

    def productExceptSelf(nums: List[str]) -> List[str]:

        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postFix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postFix
            postFix *= nums[i]
        return res


test = Solution.productExceptSelf(["a", "b", "c", "d"])

print(test)
