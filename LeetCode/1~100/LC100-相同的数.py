# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归方法
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            if not p and not q:
                return True
            else:
                return False

        if p.val != q.val:
            return False
        if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
        else:
            return False
