
from typing import List


class Solution:
    def storeFrequency_in_dict(nums: List[int], ):

        hash = {}
        for i in nums:
            hash[i] = 1 + hash.get(i, 0)
        return hash
