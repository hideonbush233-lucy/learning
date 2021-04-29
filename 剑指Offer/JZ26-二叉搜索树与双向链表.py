# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    pre = None
    def Convert(self, pRootOfTree):
        # write code here
        def dfs(cur):
            if not cur: 
                return
            dfs(cur.left)
            if self.pre: # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else: # 记录头节点
                self.head = cur
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
            
        if not pRootOfTree: 
            return None
        self.pre = None
        dfs(pRootOfTree)
         
        return self.head
