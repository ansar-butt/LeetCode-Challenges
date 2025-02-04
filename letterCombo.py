# 17. Letter Combinations of a Phone Number
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

from typing import List


# Memory: Beats 100%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(digit, string):
            if len(digit) == 1:
                for each in mapping[digit]:
                    combos.append(string + each)
            else:
                for each in mapping[digit[0]]:
                    helper(digit[1:], string + each)

        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) == 0:
            return []

        combos = []
        helper(digits, "")

        return combos
