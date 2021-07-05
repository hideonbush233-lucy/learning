# 你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

# 取模性质 (a * b) % k = (a % k)(b % k) % k
# 快速幂
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # n = len(b)
        # index = 0
        # for i in range(n):
        #     index = 10*index+b[i]
        # return pow(a,index)%1337
        base = 1337
        def mypow(a,k):
            a %= base
            res = 1
            for _ in range(k):
                res *= a
                res %= base
            return res
        if not b:
            return 1
        last = b.pop()
        part1 = mypow(a,last)
        part2 = mypow(self.superPow(a,b),10)
        return (part1*part2)%base
