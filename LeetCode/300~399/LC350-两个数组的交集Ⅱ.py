# 给定两个数组，编写一个函数来计算它们的交集。
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for num in nums1:
            if num in nums2:
                ans.append(num)
                nums2.remove(num)
        return ans
