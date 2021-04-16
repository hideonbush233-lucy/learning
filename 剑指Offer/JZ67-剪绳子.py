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
      
# https://mp.weixin.qq.com/s?__biz=MzI3NzIwMjk4OA==&mid=2247484941&idx=1&sn=d268686f5408a8e431bd2e4a79dd7fc8&chksm=eb68974edc1f1e5823b9bd5485e32a91bcaaa6e3fb146bd8526d91bf6144f2da332ee2cd8b42&mpshare=1&scene=23&srcid=0416eoy626RzI6JNM9QQevId&sharer_sharetime=1618561576753&sharer_shareid=a5423d6d3794defc58f0d989fcdd8682#rd
