# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


# 直接遍历搜索
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        cur = pHead
        res = []
        while cur:
            if cur.val not in res:
                res.append(cur.val)
                cur = cur.next
            else:
                return cur
