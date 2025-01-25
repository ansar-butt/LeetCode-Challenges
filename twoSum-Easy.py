# 1. Two Sum
""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice. """


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMaps = {}
        index = -1
        for each in nums:
            index += 1
            if each in numMaps and each * 2 == target:
                return [numMaps[each], index]
            else:
                numMaps[each] = index

        num1 = -9999
        num2 = -9999

        for each in numMaps.keys():
            num1 = each
            if (target - num1) in numMaps and not target - num1 == num1:
                num2 = numMaps[num1]
                num1 = numMaps[target - num1]
                break

        return [num1, num2]
