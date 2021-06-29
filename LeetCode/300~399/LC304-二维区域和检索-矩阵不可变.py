# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
class NumMatrix:

    # def __init__(self, matrix: List[List[int]]):
    #     self.arr = matrix
    #     self.m,self.n = len(matrix), (len(matrix[0]) if matrix else 0)


    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     ans = 0
    #     for i in range(row1,row2+1):
    #         for j in range(col1,col2+1):
    #             ans += self.arr[i][j]
    #     return ans

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i][j + 1] = _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums

        total = sum(_sums[i][col2 + 1] - _sums[i][col1] for i in range(row1, row2 + 1))
        return total



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
