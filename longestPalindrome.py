# 5. Longest Palindromic Substring
"""
Given a string s, return the longest palindromic substring in s.
"""


# Memory: Beats 100%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(string: str) -> bool:
            strLength = len(string)
            for x in range(0, strLength // 2):
                if string[x] != string[strLength - x - 1]:
                    return False
            return True

        substr = ""
        for i in range(0, len(s)):
            for j in range(len(s), 0, -1):
                if len(substr) > j - i:
                    break
                if isPalindrome(s[i:j]):
                    substr = s[i:j]

        return substr
