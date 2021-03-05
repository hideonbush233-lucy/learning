# 类似于递归，2*n 假设第一个横着放，则剩余空间为2*（n-2），若竖着放则剩余2*（n-1)，这两种可能的方法数相加即可 
# f(n) = f(n-1)+f(n-2)

class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0 or number == 1 or number == 2:
            return number
        dp = [0,1,2]
        for i in range(3,number+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[number]
