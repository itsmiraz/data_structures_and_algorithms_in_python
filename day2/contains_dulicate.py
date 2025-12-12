

# Given an integer array nums return true if any values apears at least twice in the array and return false if every element is distinct


from typing import List


class Solution:
    # Sorting First Try
    def hasDuplicateV1(nums: List[int]) -> bool:

        if len(nums) == 0:
            return False
        else:
            sorted_data = sorted(nums)

            for index, value in enumerate(sorted_data):
                if len(sorted_data) == 0:
                    return False
                if sorted_data.__len__() == index + 1:
                    return False
                elif value == sorted_data[index+1]:
                    return True
                else:
                    continue

# Brute Force
    def hasDuplicateV2(nums: List[int]) -> bool:

        for i in range(len(nums)):
            print(i)
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False


# neet code sorting

    def hasDuplicateV3(nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:  # Note here we are comparing the current value and the previous value the reason if in the array there is no duplicates in that case if i compare current and next value i will get an error or i need to a logic that if this a last value so it will ignore that
                return True
        return False


data = Solution.hasDuplicateV3(nums=[1, 2, 3, 4])

print(data)
