# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 广度优先遍历 采用队列实现  记录下下一层的结点
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = [root]
        nextlevel = []
        ans = []
        temp = []
        while que:
            temp.append(que[0].val)
            cur = que[0]
            if cur.left:
                nextlevel.append(cur.left)
            if cur.right:
                nextlevel.append(cur.right)
            que.pop(0)
            if len(que)==0:
                ans.append(temp)
                temp = []
                que[:] = nextlevel
                nextlevel = []
        return ans
