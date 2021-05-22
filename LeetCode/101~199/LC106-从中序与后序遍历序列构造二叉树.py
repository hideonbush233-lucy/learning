# 根据一棵树的中序遍历与后序遍历构造二叉树。

# 跟上一题一样呢，观察递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                break

        root.left = self.buildTree(inorder[:i],postorder[:i])
        root.right = self.buildTree(inorder[i+1:],postorder[i:-1])
        return root
