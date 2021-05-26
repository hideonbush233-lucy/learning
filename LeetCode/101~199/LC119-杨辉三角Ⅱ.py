# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        for i in range(1,rowIndex+1):
            temp = [1]*(i+1)
            for j in range(1,i):
                temp[j] = dp[j-1]+dp[j]
            dp = temp[:]
        return dp
