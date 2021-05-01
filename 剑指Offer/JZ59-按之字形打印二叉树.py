# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

# -*- coding:utf-8 -*-“”{{——
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 层次遍历
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        ans = []
        nextlevel = [pRoot]
        level = 0
        while len(nextlevel) != 0:
            temp = []
            sz = len(nextlevel)
            for i in range(sz):
                node = nextlevel[0]
                temp.append(node.val)
                nextlevel.pop(0)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            level += 1
            if level % 2 == 0:
                temp = temp[::-1]
            ans.append(temp)
        return ans
