# 给定一个非负整数数组，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

# 假设你总是可以到达数组的最后一个位置。


# 动态规划
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [1000]*len(nums)
        dp[0] = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] >= i-j:
                    dp[i] = min(dp[j]+1,dp[i])
        return dp[len(nums)-1]
