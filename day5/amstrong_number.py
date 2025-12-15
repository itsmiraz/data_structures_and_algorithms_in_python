

# armstrong number

class Solution:
    def isArmstrongNumber(n: int) -> bool:
        temp = n
        nod = len(str(n))
        total = 0

        while temp > 0:
            ld = temp % 10

            total += (ld ** nod)
            temp = temp//10

        if total == n:
            return True
        else:
            return False


test = Solution.isArmstrongNumber(n=16344)
print(test)
