# 给定一个二叉树，返回所有从根节点到叶子节点的路径。

# 说明: 叶子节点是指没有子节点的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        def travel(node,temp):
            if node == root:
                temp = str(node.val)
                
            if not node.left and not node.right:
                self.ans.append(temp)
                return 
            
            if node.left:
                travel(node.left,temp+'->'+str(node.left.val))
            if node.right:
                travel(node.right,temp+'->'+str(node.right.val))
        travel(root,'')
        return self.ans
