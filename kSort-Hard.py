# 23. Merge k Sorted Lists
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = [each for each in lists]

        total_heads = len(heads)
        current_heads = 0

        head = None
        curr_node = head

        while total_heads > current_heads:
            min_head = 9999999999
            min_head_index = -1
            curr_index = -1

            for each in heads:
                curr_index += 1
                if each and each.val < min_head:
                    min_head = each.val
                    min_head_index = curr_index

            if min_head_index > -1:
                node = ListNode(min_head)
                if not head:
                    head = node
                    curr_node = head
                else:
                    curr_node.next = node
                    curr_node = curr_node.next

                heads[min_head_index] = heads[min_head_index].next
                if heads[min_head_index] == None:
                    current_heads += 1
            else:
                current_heads = total_heads

        return head
