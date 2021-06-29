# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumval = n*(n+1)/2
        sumtrue = sum(nums)
        return int(sumval-sumtrue)
