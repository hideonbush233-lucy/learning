# 给定一个二叉树，检查它是否是镜像对称的。

 

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 这里需要用两个结点判断，因此需要新建函数
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(root1,root2):
            if not root1 or not root2:
                if not root1 and not root2:
                    return True
                else:
                    return False
            if root1.val != root2.val:
                return False
            return check(root1.left,root2.right) and check(root1.right,root2.left)

        return check(root.left,root.right)
