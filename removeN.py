# 19. Remove Nth Node From End of List
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Memory: Beats 100%
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(node):
            if not node.next:
                return 1
            pos = helper(node.next)
            if pos == index:
                node.next = node.next.next
                return pos + 1
            else:
                return pos + 1

        index = n
        position = helper(head)
        if position == index:
            head = head.next
        return head
