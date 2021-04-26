# 操作给定的二叉树，将其变换为源二叉树的镜像。 


# 方法容易想到，但开始把边界条件想的太复杂了，实际上某个子节点为空时自然返回None
class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if not pRoot:
            return None
        pRoot.left,pRoot.right = self.Mirror(pRoot.right),self.Mirror(pRoot.left)
        return pRoot
