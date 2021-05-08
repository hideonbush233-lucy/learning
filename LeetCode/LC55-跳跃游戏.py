# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标。

# 贪心算法
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 72 / 75 个通过测试用例
        # 超时了，应该是递归层数太深
        # def jump(index):
        #     if index == len(nums)-1:
        #         return True
        #     if nums[index] == 0:
        #         return False
        #     temp = False
        #     for i in range(index+1,index+1+nums[index]):
        #         temp = temp or jump(i)
        #     return temp
        # ans = jump(0)
        # return ans

        # 实际上只需要关注能达到的最远位置
        n = len(nums)
        most = 0
        for i in range(n):
            if most >= n:
                return True
            if most < i:
                return False
            most = max(most,i+nums[i])
        return True
