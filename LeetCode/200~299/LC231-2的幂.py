# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

# 如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n%2 != 0 and n!= 1:
            return False
        elif n==1:
            return True
        ans = 1
        while ans < n:
            ans *= 2
            if ans == n:
                return True
        return False
