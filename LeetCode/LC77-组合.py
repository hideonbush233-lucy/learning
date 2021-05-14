# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。


# 递归
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        num = [i for i in range(1,n+1)]
        temp = []
        def dfs(num,temp,length):
            if length == k:
                ans.append(temp)
                return
            for i in range(len(num)):
                dfs(num[i+1:],temp+[num[i]],length+1)
        dfs(num,temp,0)
        return ans
