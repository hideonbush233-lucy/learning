# 给你一个数组 nums ，请你完成两类查询，其中一类查询要求更新数组下标对应的值，另一类查询要求返回数组中某个范围内元素的总和。

# 实现 NumArray 类：

#     NumArray(int[] nums) 用整数数组 nums 初始化对象
#     void update(int index, int val) 将 nums[index] 的值更新为 val
#     int sumRange(int left, int right) 返回子数组 nums[left, right] 的总和（即，nums[left] + nums[left + 1], ..., nums[right]）
class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.length = len(nums)


    def update(self, index: int, val: int) -> None:
        self.arr[index] = val


    def sumRange(self, left: int, right: int) -> int:
        return sum(self.arr[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
