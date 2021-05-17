# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 递归，效率太慢，为了练练手
        # ans = []
        # nums1[:] = nums1[:m]
        # def func(arr1,arr2,num):
        #     if len(arr1) == 0 or num == m:
        #         ans.extend(arr2)
        #         return
        #     elif len(arr2) == 0:
        #         ans.extend(arr1)
        #         return
        #     else:
        #         if arr1[0] <= arr2[0]:
        #             ans.append(arr1[0])
        #             num += 1
        #             func(arr1[1:],arr2,num)
        #         else:
        #             ans.append(arr2[0])
        #             func(arr1,arr2[1:],num)
        # func(nums1,nums2,0)
        # nums1[:] = ans

        # 不讲武德
        # nums1[m:]=nums2
        # nums1.sort()
        # 双指针
