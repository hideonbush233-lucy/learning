# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
# #         self.next = None
# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。

 

# 现有一个链表 -- head = [4,5,1,9]，它可以表示为:

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
