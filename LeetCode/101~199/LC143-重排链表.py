# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 通过列表储存链表节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # if not head or not head.next or not head.next.next:
        #     return
        # temp = head
        # while temp.next.next:
        #     temp = temp.next
        # temp.next.next = head.next
        # head.next = temp.next
        # temp.next = None
        # self.reorderList(head.next.next)

        if not head:
            return
        
        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next
        
        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        
        vec[i].next = None
