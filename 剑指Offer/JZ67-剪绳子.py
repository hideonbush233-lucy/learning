# 给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），每段绳子的长度记为k[1],...,k[m]。
# 请问k[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。


# 动态规划！！！
class Solution:
    def cutRope(self, number):
        # write code here
        dp = [0] * (number+1)
        dp[2] = 1
        for i in range(3,number+1):
            for j in range(2,i):
                dp[i] = max(dp[i],max(j*(i-j),j*dp[i-j]))
        return dp[number]

    
# 记忆化递归
# -*- coding:utf-8 -*-
class Solution:
    def func(self, num, dp):
        if num <= 4:
            return num
        res = 0
        if dp[num] != 0:
            return dp[num]
        for i in range(2,num):
            res = max(res,i*self.func(num-i,dp))
        dp[num] = res
        return res
    
    def cutRope(self, number):
        # write code here
        if number == 2:
            return 1
        if number == 3:
            return 2
        dp = [0] * (number+1)
        return self.func(number,dp)
