# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        ans = []
        def travel(root,deep):
            if not root:
                return
            if len(ans) < deep+1:
                ans.append([])
            ans[deep].append(root.val)
            travel(root.left, deep+1)
            travel(root.right, deep+1)
            
        
        travel(pRoot, 0)
        return ans
