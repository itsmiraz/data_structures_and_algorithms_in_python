

# Hashing in python

# Prestroing values into some datastructure like list/ dict/

from typing import List


class Solution:
    def isContainVales(nums=List[int], m=List[int]):

        hash_list = [0] * len(nums)

        for i in nums:
            hash_list[i] += 1

        return hash_list


test = Solution.isContainVales(
    nums=[1, 2, 3, 4, 4, 4, 4, 4, 3], m=[23, 4, 343])

print(test)
