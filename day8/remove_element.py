class Solution(object):
    def removeElement(nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


test = Solution.removeElement(nums=[3, 2, 2, 3, 2], val=3)

print(test)
