# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

# 你应当 保留 两个分区中每个节点的初始相对位置。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(0,head)
        # 找到第一个大于x的节点，, r的前一个节点是r_pre
        r_pre, r = dummy, head
        while r and r.val<x: 
            r_pre=r_pre.next
            r=r.next
        if not r: return head  #说明不需要移动
        # 开始将r右边的小于x的数移到r_pre 和 r之间
        h_pre, h = r, r.next
        while h:
            if h.val<x:
                # r的右侧: h_pre指向原来h的下一个
                h_pre.next=h.next
                # r的左侧: h挪到r的前面
                r_pre.next = h
                h.next=r
                # 变更r_pre, h
                r_pre = h
                h = h_pre.next
            else:
                h=h.next
                h_pre=h_pre.next
        return dummy.next
