# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 直接按照描述实现
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        if length == 1:
            return head
        if k>=length:
            k = k%length
        if k == 0:
            return head
        pre = head
        for i in range(length-k-1):
            pre = pre.next
        new_head = pre.next
        cur = new_head
        for j in range(k-1):
            cur = cur.next
        cur.next = head
        pre.next = None
        return new_head
