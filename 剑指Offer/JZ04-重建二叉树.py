# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeLinkNode(pre[0])
        head = TreeLinkNode(pre[0])
        index = tin.index(pre[0])
        length = len(tin[:index])
        if index == 0:
            head.left = None
        else:
            head.left = self.reConstructBinaryTree(pre[1:length+1], tin[:index])
        if length + 1 < len(pre):
            head.right = self.reConstructBinaryTree(pre[length+1:], tin[index+1:])
        else: 
            head.right = None
        return head
