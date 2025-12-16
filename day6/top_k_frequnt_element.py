

from typing import List


class Solution:
    def topKFrequent(nums: List[int], k: int) -> List[int]:

        hash = {}
        for i in nums:
            hash[i] = 1 + hash.get(i, 0)

        # Sort the hash based on the values
        sorted_data = dict(
            sorted(hash.items(), key=lambda item: item[1], reverse=True))
        # Convert into list with the keys
        final_list = list(sorted_data.keys())

        res = []
        for i in range(0, k):
            res.append(final_list[i])
        # and return the  k amount of values
        return res


# sorting

    def topKElementV2(nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            hash[i] = 1 + hash.get(i, 0)

        arr = []

        for num, cnt in hash.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


test = Solution.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2)

print(test)
