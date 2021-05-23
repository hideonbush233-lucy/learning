# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 直接利用上一题，实际应该根据链表查找中结点
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def func(nums):
            if len(nums) == 0:
                return None
            elif len(nums) == 1:
                return TreeNode(nums[0])
            n = len(nums)
            mid = n//2
            root = TreeNode(nums[mid])
            root.left = func(nums[:mid])
            root.right = func(nums[mid+1:])
            return root
        return func(nums)
