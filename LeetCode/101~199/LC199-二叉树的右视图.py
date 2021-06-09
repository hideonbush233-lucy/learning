# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 广度优先遍历
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        nextlevel = []
        ans = []
        flag = True
        while queue:
            node = queue[0]
            queue.pop(0)
            if node:
                nextlevel.append(node.right)
                nextlevel.append(node.left)
                if flag:
                    ans.append(node.val)
                    flag = False
            if len(queue) == 0:
                queue[:] = nextlevel
                flag = True
                nextlevel = []
        return ans
