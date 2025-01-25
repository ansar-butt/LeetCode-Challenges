# 2. Add Two Numbers
"""You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself."""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        index = 0
        num1 = 0
        num2 = 0

        node = l1
        while node != None:
            num1 += node.val * 10**index
            node = node.next
            index += 1

        index = 0
        node = l2
        while node != None:
            num2 += node.val * 10**index
            node = node.next
            index += 1

        num_sum = num1 + num2
        if num_sum == 0:
            return ListNode(0)
        else:
            prev = None
            string = str(num_sum)
            while len(string):
                val = string[0]
                string = string[1:]
                node = ListNode(val, prev)
                prev = node
            return prev
