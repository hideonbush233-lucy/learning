# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

# 假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

# 你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 哈希表
        # dic = {}
        # for num in nums:
        #     if num not in dic:
        #         dic[num] = 1
        #     else:
        #         return num
        # 二分法
        n = len(nums)
        left = 1
        right = n-1
        ans = -1
        while left<=right:
            mid = (left+right)//2
            cnt = 0
            for i in range(n):
                if nums[i] <= mid:
                    cnt+=1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid -1
                ans = mid
        return ans
