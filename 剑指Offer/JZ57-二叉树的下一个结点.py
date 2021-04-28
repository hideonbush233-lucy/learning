# 给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的next指针。
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# 首先得到根节点，然后实现中序遍历，最后遍历数组查看下一节点
class Solution:
    def GetNext(self, pNode):
        # write code here
        def pre_order(root,arr):
            if not root:
                return
            pre_order(root.left, arr)
            arr.append(root)
            pre_order(root.right, arr)
        root = TreeLinkNode(-1)
        cur = pNode
        while cur:
            root = cur
            cur = cur.next
        res = []
        pre_order(root, res)
        for i in range(len(res)):
            if res[i] == pNode and i + 1 != len(res):
                return res[i+1]
        return None
      
# 画图总结规律
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        while pNode.next:
            root = pNode.next
            if root.left == pNode:
                return root
            pNode = pNode.next
        return None
