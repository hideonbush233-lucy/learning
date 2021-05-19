# 给定一个二叉树的根节点 root ，返回它的 中序 遍历


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def travel(root):
            if not root:
                return
            travel(root.left)
            ans.append(root.val)
            travel(root.right)
        travel(root)
        return ans
