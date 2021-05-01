# 请实现一个函数，用来判断一棵二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        def test(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val == root2.val and test(root1.left, root2.right) and test(root1.right,root2.left)
        return test(pRoot, pRoot)
