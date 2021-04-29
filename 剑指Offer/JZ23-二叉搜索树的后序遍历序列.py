# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。（ps：我们约定空树不是二叉搜素树）


# 递归
# 后序遍历最后一个为数的根节点，遍历确定左子树与右子树的分界点，检测右子树是否满足情况，然后递归

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence) == 0:
            return False
        root = sequence[-1]
        index = 0
        for i in range(len(sequence)):
            if sequence[i] >= root:
                index = i
                break
        for j in range(index,len(sequence)-1):
            if sequence[j] < root:
                return False
        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[0:index])
        right = True
        if index < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[index:-1])
        return left and right
