# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

# 建立一个全局变量length，当前结点为none时返回0
class Solution:
    length = 0
    def TreeDepth(self, pRoot):
        # write code here
        tmp = 0
        if not pRoot:
            return tmp
        self.length = max(1 + self.TreeDepth(pRoot.left),1 + self.TreeDepth(pRoot.right))
        return self.length
