# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        temp = []
        ans = []
        used = [0]*n
        def dfs():
            if len(temp) == n:
                if temp not in ans:
                    ans.append(temp[:])
                return
            for i in range(n):
                if used[i] != 0:
                    continue
                temp.append(nums[i])
                used[i] = 1
                dfs()
                temp.pop()
                used[i] = 0
        dfs()
        return ans
