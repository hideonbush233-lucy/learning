# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：

#     answer[i] % answer[j] == 0 ，或
#     answer[j] % answer[i] == 0

# 如果存在多个有效解子集，返回其中任何一个均可

# 动态规划
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        f = [[x] for x in nums] # answer at nums[i]
        for j in range(len(nums)):
            for i in range(j):
                if nums[j]%nums[i]==0 and len(f[i])+1 > len(f[j]):
                    f[j] = f[i] + [nums[j]]
        return max(f, key=len)
