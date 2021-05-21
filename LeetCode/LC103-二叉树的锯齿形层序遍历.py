# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 广度优先遍历，不同的是根据当前层数确定加到ans中的是正序还是倒序
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        flag = 0
        ans = []
        que = [root]
        temp = []
        nextlevel = []
        while que:
            node = que[0]
            que.pop(0)
            temp.append(node.val)
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
            if len(que) == 0:
                que[:] = nextlevel
                if flag%2==0:
                    ans.append(temp)
                else:
                    ans.append(temp[::-1])
                flag += 1
                temp = []
                nextlevel = []
        return ans
