# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
# 假定每组输入只存在唯一答案。



# 排序加双指针
# 直接把出现的这些结果加到res数组中，然后在数组中直接逐个比较与target的距离就好。
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = []
        for first in range(n-2):
            i = first + 1
            j = n-1
            while i < j:
                tmp = nums[first] + nums[i] + nums[j]
                res.append(tmp)
                if tmp > target:
                    j -= 1
                elif  tmp < target:
                    i += 1
                elif tmp == target:
                    return target
            res.append(tmp)
        best = res[0]
        for item in res:
            if abs(item - target) < abs(best - target):
                best = item
        return best

