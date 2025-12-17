
from typing import List


class Solution:
    def encode(strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str((len(i))) + "&" + i
        return res

    def decode(s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "&":
                j += 1
            print(j)
            length = int(s[i:j])
            i = j + 1
            j = i + length
            print(i, j)
            res.append(s[i:j])
            i = j
        return res


# encodeRes = Solution.encode(["neet", "code", "love", "you"])
decodeRes = Solution.decode("4&neet4&code4&love3&you")
print(decodeRes)

test = "4&neet"
print(test[2:6])
