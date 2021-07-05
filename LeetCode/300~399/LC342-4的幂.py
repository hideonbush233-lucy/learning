# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4**x


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==2:
            return False
        return n>0 and 4**15 % n==0 and n%3==1
