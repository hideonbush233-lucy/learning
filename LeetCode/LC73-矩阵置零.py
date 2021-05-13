# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

# 进阶：

#     一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
#     一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
#     你能想出一个仅使用常量空间的解决方案吗？


# O(mn)的方法，并不是最优
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        momo = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and not momo[i][j]:
                    for p in range(n):
                        if p != j and matrix[i][p] != 0:
                            matrix[i][p] = 0
                            momo[i][p] = True
                    for q in range(m):
                        if q != i and matrix[q][j] != 0:
                            matrix[q][j] = 0
                            momo[q][j] = True
                momo[i][j] = True
