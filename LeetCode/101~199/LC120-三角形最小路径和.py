# 给定一个三角形 triangle ，找出自顶向下的最小路径和。

# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
# 也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。


# 动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            dp[i][0] = triangle[i][0] + dp[i-1][0]
            dp[i][i] = triangle[i][i] + dp[i-1][i-1]
            for j in range(1,i):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j-1],dp[i-1][j])
        return min(dp[-1])
