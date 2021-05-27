# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。


# 进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

# sort()排序后遍历，时间复杂度不行
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n <= 1:
            return n
        maxlen = 0
        sum = 1
        for i in range(1,n):
            temp = nums[i] - nums[i-1]
            if temp <= 1:
                sum += temp
            else:
                maxlen = max(maxlen,sum)
                sum = 1
        return max(maxlen,sum)
