# 峰值元素是指其值大于左右相邻值的元素。

# 给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

# 你可以假设 nums[-1] = nums[n] = -∞ 。


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 法一 暴力破解
        # n = len(nums)
        # if n == 1:
        #     return 0
        # for i in range(n):
        #     if i == 0:
        #         if nums[i] > nums[1]:
        #             return 0
        #     elif i == n-1:
        #         if nums[i] > nums[i-1]:
        #             return n-1
        #     else:
        #         if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
        #             return i
        # 二分法
        def search(arr,l,r):
            if l == r :
                return l
            mid = (l+r)//2
            if arr[mid] > arr[mid+1]:
                return search(arr,l,mid)
            return search(arr,mid+1,r)
        n = len(nums)
        if n == 1:
            return 0
        return search(nums,0,n-1)
