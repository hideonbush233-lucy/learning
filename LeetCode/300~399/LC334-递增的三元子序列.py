# 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

# 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；
# 否则，返回 false 。


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # n = len(nums)
        # if n<3:
        #     return False
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         if nums[j] > nums[i] and nums[j] < max(nums[j+1:]):
        #             return True
        # return False
        n = len(nums)
        if n < 3:
            return False
        small, mid = max(nums), max(nums)
        for i in range(n):
            if nums[i] <= small:
                small = nums[i]
            elif nums[i] <= mid:
                mid = nums[i]
            elif nums[i] > mid:
                return True
        return False
