# 给定一个整数 n, 返回从 1 到 n 的字典顺序。

# 例如，

# 给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

# 请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # 法一 字符字典序
        # ans = sorted(str(_) for _ in range(1,n+1))
        # ans_new = [int(_) for _ in ans]
        # return ans_new
        
        # 法二 递归
        arr = []
        def dfs(n,t):
            if t<=n:
                arr.append(t)
            else:
                return 
            for i in range(10):
                dfs(n,10*t+i)

        for i in range(1,10):
            dfs(n,i)
        return arr
