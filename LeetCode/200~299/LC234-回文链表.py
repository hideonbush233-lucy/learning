# 请判断一个链表是否为回文链表。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        if nums == nums[::-1]:
            return True
        else:
            return False
