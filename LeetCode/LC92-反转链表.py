# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        dummy = ListNode(0,head)
        slow = dummy
        for i in range(left-1):
            slow = slow.next
        fast = slow.next
        for _ in range(right-left):
            next = fast.next
            fast.next = next.next
            next.next = slow.next
            slow.next = next
        return dummy.next
