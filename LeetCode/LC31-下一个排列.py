# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须 原地 修改，只允许使用额外常数空间。


# 首先从后向前查找第一个顺序对 (i,i+1)(i,i+1)(i,i+1)，满足 a[i]<a[i+1]a[i] < a[i+1]a[i]<a[i+1]。这样「较小数」即为 a[i]a[i]a[i]。此时 [i+1,n)[i+1,n)[i+1,n) 必然是下降序列。

# 如果找到了顺序对，那么在区间 [i+1,n)[i+1,n)[i+1,n) 中从后向前查找第一个元素 jjj 满足 a[i]<a[j]a[i] < a[j]a[i]<a[j]。这样「较大数」即为 a[j]a[j]a[j]。

# 交换 a[i]a[i]a[i] 与 a[j]a[j]a[j]，此时可以证明区间 [i+1,n)[i+1,n)[i+1,n) 必为降序。我们可以直接使用双指针反转区间 [i+1,n)[i+1,n)[i+1,n) 使其变为升序，而无需对该区间进行排序。

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
