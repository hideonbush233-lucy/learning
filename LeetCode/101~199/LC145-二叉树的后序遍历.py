# 给定一个二叉树，返回它的 后序 遍历。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.dic.append(root.val)
        return self.dic
