# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

# 动态规划，记录这一天卖出的最大收益是多少
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 暴力超时
        # values = 0
        # for i in range(n-1):
        #     start = prices[i]
        #     for j in range(i+1,n):
        #         end = prices[j]
        #         if end-start > values:
        #             values = end-start
        # return values
        dp = [0]*n
        for i in range(1,n):
            temp = prices[i] - prices[i-1] + dp[i-1]
            if temp < 0:
                dp[i] = 0
            else:
                dp[i] = temp           
        return max(dp)
