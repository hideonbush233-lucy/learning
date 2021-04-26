#  输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
# 平衡二叉树（Balanced Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。


# 一遍过，有点开心哈哈哈
# 写了一个得到数结构深度的函数，然后利用递归编写条件
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        def get_length(root):
            if not root:
                return 0
            return max(get_length(root.left),get_length(root.right))+1
        if abs(get_length(pRoot.left)-get_length(pRoot.right)) <= 1 and self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right):
                return True
        else:
            return False
