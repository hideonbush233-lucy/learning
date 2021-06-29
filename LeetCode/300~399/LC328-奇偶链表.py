# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
# 请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        cur = head
        used = []
        while cur and cur.next:
            cur = cur.next
        last = cur
        Flast = last
        cur = head

        while cur and cur.next and cur.next.next:
            if cur==Flast:
                break
            if cur.next==Flast:
                last.next = cur.next
                cur.next = cur.next.next
                last.next.next = None
                last = last.next
                cur = cur.next
                break
            last.next = cur.next
            cur.next = cur.next.next
            last.next.next = None
            last = last.next
            cur = cur.next
        return head
