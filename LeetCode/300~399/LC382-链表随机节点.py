# 给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

# 进阶:
# 如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

# 每次只保留一个数，当遇到第 i 个数时，以 1/i的概率保留它，(i-1)/i的概率保留原来的数。
# 举例说明： 1 - 10
#     遇到1，概率为1，保留第一个数。
#     遇到2，概率为1/2，这个时候，1和2各1/2的概率被保留
#     遇到3，3被保留的概率为1/3，(之前剩下的数假设1被保留)，2/3的概率 1 被保留，(此时1被保留的总概率为 2/3 * 1/2 = 1/3)
#     遇到4，4被保留的概率为1/4，(之前剩下的数假设1被保留)，3/4的概率 1 被保留，(此时1被保留的总概率为 3/4 * 2/3 * 1/2 = 1/4)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        # self.stack = []
        # self.length = 0
        # while head:
        #     self.stack.append(head.val)
        #     self.length += 1
        #     head = head.next
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # index = random.randint(0,self.length-1)
        # return  self.stack[index]
        count = 0
        reserve = 0
        cur = self.head
        while cur:
            count += 1
            rand = random.randint(1,count)
            if rand == count:
                reserve = cur.val
            cur = cur.next
        return reserve


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
