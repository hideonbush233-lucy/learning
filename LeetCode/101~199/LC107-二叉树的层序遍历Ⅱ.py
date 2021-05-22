# 给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 直接套用前面的层序遍历，然后返回的时候逆序输出就可以
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = [root]
        nextlevel = []
        ans = []
        temp = []
        while que:
            node = que[0]
            temp.append(node.val)
            que.pop(0)
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
            if len(que) == 0:
                ans.append(temp)
                que[:] = nextlevel
                nextlevel = []
                temp = []
        return ans[::-1]
