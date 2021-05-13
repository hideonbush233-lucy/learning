# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

#     每行中的整数从左到右按升序排列。
#     每行的第一个整数大于前一行的最后一个整数。
  
 

# 根据矩阵特性先确定target所在行，然后遍历
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        i = j = 0
        while i < m-1:
            if matrix[i+1][0] < target:
                i += 1
            elif matrix[i+1][0] == target:
                return True
            else:
                break
        for j in range(n):
            if matrix[i][j] == target:
                return True
        return False
