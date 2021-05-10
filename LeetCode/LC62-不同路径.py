# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

# 问总共有多少条不同的路径？



# 直接排列组合
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        top = 1
        num = m+n-2
        for i in range(num,num-m+1,-1):
            top *= i
        dowm = 1
        for j in range(1,m):
            dowm *= j
        return int(top/dowm)
