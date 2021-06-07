# 给定一个整数 n，返回 n! 结果尾数中零的数量。

class Solution:
    def trailingZeroes(self, n: int) -> int:

        # def trailing(n):
        #     if n==0 or n==1:
        #         return 1
        #     a=1
        #     for i in range(2,n+1):
        #         a = a*i
        #     return a
        
        # res = trailing(n)
        # ans = 0
        # while res%10 == 0:
        #     ans += 1
        #     res = res // 10
        # return ans
        zero_count = 0
        current_multiple = 5
        while n >= current_multiple:
            zero_count += n // current_multiple
            current_multiple *= 5
        return zero_count
