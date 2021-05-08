# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。


# 螺旋遍历，注意转向方法
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        ans = []
        i = j = 0
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        index = 0
        used = [[False]*n for _ in range(m)]
        while len(ans) < m*n:
            ans.append(matrix[i][j])
            used[i][j] = True
            new_i,new_j = i+direction[index][0],j+direction[index][1]
            if not( 0<=new_i<m and 0<=new_j<n and not used[new_i][new_j]):
                index = (index+1)%4
            i,j = i+direction[index][0],j+direction[index][1]
        return ans
