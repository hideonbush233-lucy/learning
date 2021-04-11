# 输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）


# 双指针
# 如何让本来长度不相等的变为相等的？
# 假设链表A长度为a， 链表B的长度为b，此时a != b
# 但是，a+b == b+a
# 因此，可以让a+b作为链表A的新长度，b+a作为链表B的新长度。
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        cur1 = pHead1
        cur2 = pHead2
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
            if cur1 != cur2:
                if cur1 == None: 
                    cur1 = pHead2
                if cur2 == None: 
                    cur2 = pHead1
        return cur1
