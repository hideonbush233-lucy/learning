# 给定一棵二叉搜索树，请找出其中的第k小的TreeNode结点

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 二叉搜索树，故为中寻遍历结果，采用递归进行遍历即可
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here、
        self.res=[]
        self.dfs(pRoot)
        return self.res[k-1] if 0<k<=len(self.res) else None
    def dfs(self,root):
        if not root:return
        self.dfs(root.left)
        self.res.append(root)
        self.dfs(root.right)
