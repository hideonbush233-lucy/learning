# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 注意几个关键点即可，逐个比较
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val >= l2.val:
            head = ListNode(l2.val)
            l2 = l2.next
        else:
            head = ListNode(l1.val)
            l1 = l1.next
        cur = head
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
                cur = cur.next
            else:
                cur.next = ListNode(l1.val)
                l1 = l1.next
                cur = cur.next
        if not l1:
            cur.next = l2
        if not l2:
            cur.next = l1
        return head
