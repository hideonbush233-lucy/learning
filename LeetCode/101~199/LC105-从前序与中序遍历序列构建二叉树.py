# 根据一棵树的前序遍历与中序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
            
        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        for i in range(len(preorder)):
            if inorder[i] == preorder[0]:
                break
        
        root.left = self.buildTree(preorder[1:i+1],inorder[0:i])
        root.right = self.buildTree(preorder[i+1:],inorder[i+1:])
        return root
