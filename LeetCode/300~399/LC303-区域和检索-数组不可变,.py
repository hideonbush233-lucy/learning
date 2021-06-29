# 给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

# 实现 NumArray 类：

#     NumArray(int[] nums) 使用数组 nums 初始化对象
#     int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点
# （也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.length = len(nums)


    def sumRange(self, left: int, right: int) -> int:
        return sum(self.arr[left:right+1])



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
