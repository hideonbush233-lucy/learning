# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 
# 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # dic = {}
        # ans = []
        # for num in nums:
        #     if num not in dic:
        #         dic[num] = 1
        #         ans.append(num)
        #     else:
        #         dic[num] += 1
        #     if dic[num] == 2:
        #         ans.remove(num)
        # return ans
        ans = []
        for num in nums:
            if nums.count(num) == 1:
                ans.append(num)
        return ans
