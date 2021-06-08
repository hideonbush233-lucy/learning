# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

 

# 进阶：

#     尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#     你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        # for i in range(k):
        #     nums[:] = [nums[-1]] + nums[:-1]
        nums[:] = nums[n-k:] + nums[:n-k]
