# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 法一 采用笨方法，依次把不重复的元素添加到一个列表中，最后构建一个新链表并返回头节点
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        res = []
        delnums = []
        while pHead:
            if pHead.val not in res and pHead.val not in delnums:  # 这里的判断条件要特别注意，有的元素可能出现不止一次
                res.append(pHead.val)
            elif pHead.val in res:
                res.remove(pHead.val)
                delnums.append(pHead.val)
            pHead = pHead.next
        if len(res) == 0:
            return None
        head = ListNode(res[0])
        cur = head
        for i in range(1,len(res)):
            cur.next = ListNode(res[i])
            cur = cur.next
        return head
