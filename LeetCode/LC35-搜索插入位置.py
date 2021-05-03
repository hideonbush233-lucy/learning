# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 你可以假设数组中无重复元素。


# 二分法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        if nums[0] >= target:
            return 0
        if nums[len(nums)-1] < target:
            return len(nums)
        while i<j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid
            elif nums[mid] > target:
                j = mid
            else:
                return mid
            if j-i == 1:
                return j
