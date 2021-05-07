# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

# 先沿对角线翻转，然后左右翻转
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        newarr = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n//2):
            for j in range(n):
                matrix[j][i],matrix[j][n-i-1] = matrix[j][n-i-1],matrix[j][i]
        
# 找到翻转规律，借用新的数组
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        newarr = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                newarr[j][n-i-1] = matrix[i][j]
        matrix[:] = newarr
