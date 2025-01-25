# 32. Longest Valid Parentheses
"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        longest_sub = 0
        curr = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif len(stack) > 0 and s[i] == ")" and not s[stack[-1]] == ")":
                stack.pop()
            else:
                stack.append(i)

        for i in range(len(stack)):
            if stack[i] - curr > longest_sub:
                longest_sub = stack[i] - curr
            curr = stack[i]

        if len(stack) and len(s) - stack[-1] > longest_sub:
            longest_sub = len(s) - stack[-1]

        if not len(stack):
            return len(s)
        if longest_sub % 2 == 1:
            return longest_sub - 1
        return longest_sub
