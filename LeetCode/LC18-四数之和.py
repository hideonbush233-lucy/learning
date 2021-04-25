# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

# 注意：答案中不可以包含重复的四元组。


# 类似于三数之和，排序加双指针，两个循环固定两个数，然后用双指针
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        n = len(nums)
        res = []
        for first in range(n-3):
            for second in range(first+1,n-2):
                pre = second + 1
                beh = n-1
                while pre<beh:
                    tmp = nums[first]+nums[second]+nums[pre]+nums[beh]
                    if tmp > target:
                        beh -= 1
                    elif tmp < target:
                        pre += 1
                    else:
                        index = [nums[first],nums[second],nums[pre],nums[beh]]
                        if index not in res:
                            res.append(index)
                        pre += 1
        return res
