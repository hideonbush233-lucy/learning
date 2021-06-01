# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        def travel(root,nums):
            if not root:
                return 
            nums.append(root.val)
            travel(root.left,nums)
            travel(root.right,nums)
            return nums
        return travel(root,[])
