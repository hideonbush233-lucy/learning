假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
# 老熟人了，动态规划优化版
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        a = 1
        b = 2
        for i in range(3,n+1):
            c = a+b
            a,b = b,c
        return c
