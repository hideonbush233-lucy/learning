# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # 太巧妙了 本质是新的元素与ans中的数组进行结合
        # res = [[]]
        # for i in nums:
        #     res = res + [[i] + num for num in res]
        # return res
        res = []
        n = len(nums)
        
        # 递归回溯
        def dfs(i, tmp):
            res.append(tmp)
            if i==n:
                return
            for j in range(i, n):
                dfs(j + 1,tmp + [nums[j]] )
        dfs(0, [])
        return res
