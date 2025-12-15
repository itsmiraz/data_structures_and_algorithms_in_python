

# Print all the factorials of an given number
from math import sqrt


class Solution:

    # TC -> O(n)
    # SC -> o(k) k woud the total num of factorials
    def get_factorials(num: int) -> bool:

        result = []

        for i in range(1, num+1):
            print(i)
            # print(f'{num % i}')
            if num % i == 0:
                result.append(i)

        return result

    def get_factorials_v2(num: int) -> bool:
        return
    # just take the half of the num

    def get_factorial_v3(num: int) -> bool:
        result = []
        for i in range(1, int(sqrt(num))+1):
            if num % i == 0:
                result.append(i)
                if num // i != i:
                    result.append(num//i)
        result.sort()
        return result


test = Solution.get_factorial_v3(15)
print(test)
