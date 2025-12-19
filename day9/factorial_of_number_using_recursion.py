# factorial of a number


class Solution:
    @staticmethod
    def get_factorials(num: int):
        print(num)
        if num == 1 or num == 1:
            return 1

        return num * Solution.get_factorials(num-1)


test = Solution.get_factorials(4)

print(test)
