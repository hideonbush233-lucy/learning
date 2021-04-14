# 输入一个整型数组，数组里有正数也有负数。
# 数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为 O(n).

# 动态规划，dp[i]记录以array[i]结尾的最大连续子数组的和
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [0]*len(array)
        res = array[0]
        dp[0] = array[0]
        for i in range(1,len(array)):
            dp[i] = max(array[i],array[i]+dp[i-1])
            res = max(res,dp[i])
        return res
