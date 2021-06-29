# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

# 整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3**x


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
      # 暴力破解
        if n<1:
            return False

        if n == 1:
            return True
        ans = 1
        while ans<n:
            ans *= 3
        if ans == n:
            return True
        else:
            return False
       # 1162261467 = 3**19 是 int 范围最大的取值
        return n > 0 and (1162261467 % n == 0)
