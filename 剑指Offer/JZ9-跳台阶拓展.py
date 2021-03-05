class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0 or number == 1:
            return 1
        dp = [1,1]
        for i in range(2,number+1):
            res = 0
            for j in range(i):
                res += dp[j]
            dp.append(res)
        return dp[number]
