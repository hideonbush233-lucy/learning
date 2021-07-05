# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10**n 。

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        if n == 0: return 1
        if n > 10: return 0

        cnt = 9 
        ans = 10
        for i in range(2,n+1):
            cnt *= (10 - i + 1)
            ans += cnt
        return ans
