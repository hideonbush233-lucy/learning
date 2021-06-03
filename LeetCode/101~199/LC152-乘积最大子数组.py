# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [0]*n
        dp[0] = nums[0]
        mindp = [0]*n
        mindp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(nums[i],dp[i-1]*nums[i],nums[i]*mindp[i-1])
            mindp[i] = min(nums[i],dp[i-1]*nums[i],nums[i]*mindp[i-1])
        return max(dp)
