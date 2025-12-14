
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.
from typing import List


class Solution:
    # Brute Force
    def twoSum(nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # Second Way using hashmap
    def twoSum(nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i

        return


test = Solution.twoSum(nums=[2, 5, 5, 11], target=10)
print(test)
