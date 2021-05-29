给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for item in nums:
        #     if nums.count(item) == 1:
        #         return item

        # 什么鬼？？？总是不擅长位运算
        return reduce(lambda x, y: x ^ y, nums)
