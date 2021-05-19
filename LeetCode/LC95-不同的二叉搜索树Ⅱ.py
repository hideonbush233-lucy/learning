# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTree(start,end):
            if start > end:
                return [None,]
            ans = []
            for i in range(start,end+1):
                lefttree = generateTree(start,i-1)
                righttree = generateTree(i+1,end)
                for l in lefttree:
                    for r in righttree:
                       temp = TreeNode(i)
                       temp.left = l
                       temp.right = r
                       ans.append(temp)
            return ans
        return generateTree(1,n) if n else []
