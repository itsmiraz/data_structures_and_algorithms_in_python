
# GIVEN TWO STRING S AND T return true if t is an anagram of s , and false otherwise


class Solution:
    def isAnagram(s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for i in s:
            if hash1.get(i):
                hash1[i] += 1
            else:
                hash1[i] = 1
        for i in t:
            if hash2.get(i):
                hash2[i] += 1
            else:
                hash2[i] = 1

        if hash1 == hash2:
            return True
        else:
            return False

    def isAnagramV2(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

    def isAnagramV3(s: str, t: str) -> bool:

        return sorted(s) == sorted(t)


test = Solution.isAnagramV3(s='test', t='test')
print(test)
