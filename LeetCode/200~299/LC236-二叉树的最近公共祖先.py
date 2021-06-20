# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。

class Solution:
    def __init__(self):
        self.ans = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,p,q):
            if not root:
                return False
            lson = dfs(root.left,p,q)
            rson = dfs(root.right,p,q)
            if (lson and rson) or ((root.val==p.val or root.val==q.val) and (lson or rson)):
                self.ans = root
            return lson or rson or (root.val==p.val or root.val==q.val)
        dfs(root,p,q)
        return self.ans
