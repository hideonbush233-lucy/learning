# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。


# 动态规划，记录下达到每一个位置处的最小距离
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = grid
        for i in range(m):
            for j in range(n):
                if j==0 and i-1>=0:
                    dp[i][j] += dp[i-1][j]
                if i==0 and j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
                elif i>=1 and j>= 1:
                    dp[i][j] = dp[i][j] + min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
