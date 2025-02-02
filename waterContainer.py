# 11. Container With Most Water
"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        index1 = 0
        index2 = length - 1
        current_max = -1

        while index1 < index2:
            current_max = max(
                current_max, min(height[index2], height[index1]) * (index2 - index1)
            )

            if height[index1] > height[index2]:
                index2 -= 1
            else:
                index1 += 1

        return current_max
