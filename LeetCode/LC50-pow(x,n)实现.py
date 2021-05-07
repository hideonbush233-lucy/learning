# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 这个方法不知道怎么总在奇怪的样例失败，吸取了快速幂的思想
        # if n == 0:
        #     return 1
        # elif n == 1:
        #     return x
        # elif n > 0:
        #     if n % 2 == 0:
        #         return self.myPow(x,n/2)**2
        #     else:
        #         return (self.myPow(x,(n-1)/2)**2)*x
        # elif n < 0:
        #     return 1/self.myPow(x,-n)

        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
