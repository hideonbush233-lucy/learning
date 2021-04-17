# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？


# 直接全部遍历判断是否符合要求，另外格外需要注意行和列为1的情况
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        dp = [[0]*cols for _ in range(rows)]
        num = 0
        for i in range(rows):
            for j in range(cols):
                if self.func(i, j) <= threshold:
                    num += 1
                    dp[i][j] = 1
                elif rows == 1 or cols == 1:
                    return num
        return num
    def func(self,n,m):
        res = 0
        while n > 0:
            res += (n%10)
            n = n//10
        while m > 0:
            res += (m%10)
            m = m//10
        return res
