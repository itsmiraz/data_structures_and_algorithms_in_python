
# sum of 1 to n [parameterzed way]


class Solution:
    @staticmethod
    def sumOf1_TON(sum, i, n):
        if i > n:
            print(sum)
            return
        Solution.sumOf1_TON(sum+i, i+1, n)


# test = Solution.sumOf1_TON(0, 1, 10)

# sum of 1 to n [functional recursion]


class Solution2:
    @staticmethod
    def func(n):
        if n == 1:
            return 1
        return n + Solution2.func(n-1)


test = Solution2.func(10)
print(test)
