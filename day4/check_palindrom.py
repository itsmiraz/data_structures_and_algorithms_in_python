# check palindrome


class Solution:
    def isPalindrome(n: int) -> bool:
        num = n
        result = 0

        while num > 0:
            ld = num % 10
            result = (result*10)+ld
            num = num//10

        return n == result


result = Solution.isPalindrome(n=121)
print(result)
