# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

# 叶子节点 是指没有子节点的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        temp = []
        def func(node,tar):
            if not node:
                return
            temp.append(node.val)
            tar -= node.val
            if not node.left and not node.right and tar == 0:
                ans.append(temp[:])
            func(node.left,tar)
            func(node.right,tar)
            temp.pop()

        func(root,targetSum)
        return ans
