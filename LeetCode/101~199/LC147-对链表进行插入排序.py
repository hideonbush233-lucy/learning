# 对链表进行插入排序。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0,head)
        cur = head.next
        lastorder = head
        while cur:
            if cur.val > lastorder.val:
                lastorder = cur
                cur = cur.next
            else:
                pre = dummy
                while pre.next.val < cur.val:
                    pre = pre.next
                lastorder.next = cur.next
                node = pre.next
                pre.next = cur
                cur.next = node
                cur = lastorder.next
        return dummy.next
