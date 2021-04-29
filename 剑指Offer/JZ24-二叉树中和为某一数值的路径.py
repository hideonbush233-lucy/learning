# 输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 还是递归，需要注意到达叶子节点后pop返回
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        ans = []
        path = []
        
        def func(root,tar):
            if not root:
                return 
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                ans.append(list(path))
            func(root.left, tar)
            func(root.right, tar)
            path.pop()
        func(root, expectNumber)
        return ans
