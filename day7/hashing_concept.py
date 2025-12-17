
# We have two arrays n and m we need print values from m array how times are present in the n array

# i <= n[i] <=10
# n can be have 10^8 element
# m can be have 10^8 element

# Another case
#  if we have a  n string of differetn characters
# and another m list  of of characters
#  we need find from m list whats the frequency of characters in the n str


from typing import List


class Solution:
    def findSimilarIntCount(m: List[int], n: List[str]):
        hash_list = [0] * 11

        for v in n:
            if v > 1 and v < 10:
                hash_list[v] += 1

        for num in m:
            if num < 1 or num > 10:
                return 0
            else:
                return [hash_list[num]]

    def findSimilarIntCountDict(m: List[int], n: List[str]):
        freq_dec = {}
        for v in n:
            if v > 1 and v < 10:
                freq_dec[v] = 1 + freq_dec.get(v, 0)

        for num in m:
            print(freq_dec.get(num, 0))

        # return freq_dec

    def findFreqStr(n=str, m=List[str]):
        # n will be all small letters
        # "a" < = s[i] <= 'z'

        hash_list = [0] * 27

        for ch in n:
            asciV = ord(ch)
            index = asciV - 97
            hash_list[index] += 1

        for ch in m:
            asciValue = ord(ch)
            index = asciValue - 97
            print(ch, hash_list[index])

    def findFreqStrCapitalSmall(n=str, m=List[str]):
        # n will be all small letters
        # "a" < = s[i] <= 'z'

        hash = {}

        for ch in n:
            hash[ch] = 1 + hash.get(ch, 0)

        for ch in m:
            print(ch, hash.get(ch, 0))
        # return hash
        # return hash_list


# test = Solution.findSimilarIntCountDict(
#     m=[6, 2, 43, 43, 43], n=[4, 5, 6, 6, 6, 6, 98])
test = Solution.findFreqStrCapitalSmall(
    m=['a', 'b', 'c'], n='av1223434221111113aaaaaas434343cdddaaa')
print(test)
