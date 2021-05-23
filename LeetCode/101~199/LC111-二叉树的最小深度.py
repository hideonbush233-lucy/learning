# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明：叶子节点是指没有子节点的节点。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return 1+self.minDepth(root.right)
        elif not root.right:
            return 1+self.minDepth(root.left)
        else:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
