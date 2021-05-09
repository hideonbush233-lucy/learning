# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。


# 借助螺旋矩阵那一题，也能解决
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans =[[0]*n for _ in range(n)]
        length = 1
        i = j = 0
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        index = 0
        while length <= n*n:
            ans[i][j] = length 
            length += 1

            new_i = i + direction[index][0]
            new_j = j + direction[index][1]
            if not (0<=new_i<n  and 0<=new_j<n and ans[new_i][new_j] == 0):
                index = (index+1)%4
            i += direction[index][0]
            j += direction[index][1]
        return ans
