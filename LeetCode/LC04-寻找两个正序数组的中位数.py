# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。


# 笨方法，把两个数组合并成一个新数组，然后取中位数
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1),len(nums2)
        i = j = 0
        ans = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        if i < m:
            ans += nums1[i:]
        elif j < n:
            ans += nums2[j:]
        length = len(ans)
        if length == 1:
            return ans[0]
        if length % 2 != 0:
            return ans[length//2]
        elif length % 2 == 0:
            return (ans[length//2] + ans[length//2-1])/2
          
# 二分法！！！
