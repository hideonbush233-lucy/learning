# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# 进阶：你能尝试使用一趟扫描实现吗？
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 先扫描一边获取长度，再往后退得到需要删除的结点
# 在链表前添加一个锚点十分重要的，对于很多none情况很好解决
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        length = len(arr)
        dummy = ListNode(0, head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    
    
# 快慢指针，一遍即可实现，就是两个指针始终保持相同距离向后移动，
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next
