# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


# 动态规划，较简单，记录每个位置出的最大子序列值即可
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [nums[0]]
        for i in range(1,len(nums)):
            temp = max(dp[i-1]+nums[i],nums[i])
            dp.append(temp)
        return max(dp)
