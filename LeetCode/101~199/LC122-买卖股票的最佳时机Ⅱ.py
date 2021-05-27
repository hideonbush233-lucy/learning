# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*n
        for i in range(1,n):
            temp = prices[i]-prices[i-1] 
            if temp < 0:
                dp[i] = 0
            else:
                dp[i] = temp+dp[i-1]
        values = 0
        for i in range(1,n-1):
            if dp[i] != 0 and dp[i+1] != 0:
                dp[i] = 0
        return sum(dp)
