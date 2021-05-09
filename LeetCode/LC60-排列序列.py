给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

给定 n 和 k，返回第 k 个排列。


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 计算 factor[k]=k!
        nums = [str(i) for i in range(1,n+1)]
        factor = [0,1]
        for i in range(2,n+1):
            factor.append(factor[-1]*i)
        ans = ''
        # 逐次计算每一位的数字
        def dfs(nums, n, k, ans):
            if n==1:
                return ans+nums[0]
            pos=1
            # 这里pos范围和k保持一致 k也是从1开始
            for pos in range(1,n+1):
                if k>factor[n-1]*(pos-1) and k<=factor[n-1]*pos:
                    break
            ans+=nums[pos-1]
            # 这里需要注意是 nums[0:(pos-1)]+nums[pos:]
            return dfs(nums[0:(pos-1)]+nums[pos:], n-1, k-(pos-1)*factor[n-1], ans)
        return dfs(nums, n, k, ans)
