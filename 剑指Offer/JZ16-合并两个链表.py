# 复杂一点的办法，逐个比较加入新链表中，最后返回头节点
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        if pHead1.val < pHead2.val:
            head = pHead1
            pHead1 = pHead1.next
        elif pHead1.val >= pHead2.val:
            head = pHead2
            pHead2 = pHead2.next
        cur = head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        if pHead1 == None:
            cur.next = pHead2
        elif pHead2 == None:
            cur.next = pHead1
        return head
