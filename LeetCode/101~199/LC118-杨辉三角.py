# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for i in range(1,numRows):
            temp = [1] * (i+1)
            for j in range(1,i):
                temp[j] = dp[i-1][j-1] + dp[i-1][j]
            dp.append(temp)
        return dp
