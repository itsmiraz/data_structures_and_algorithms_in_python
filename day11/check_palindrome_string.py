"""
Valid Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"
Input: s = "was it a car or a cat i saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.
"""


class Solution:
    def isPalindrome22(s: str) -> bool:
        newStr = ''

        for i in s:
            if i.isalnum():
                newStr += i
        reversed = ''
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                reversed += s[i]
        return reversed.lower() == newStr.lower()

    def isPalindrome(self, s: str):
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


sol = Solution()
test = sol.isPalindrome('race a car')
print(test)
