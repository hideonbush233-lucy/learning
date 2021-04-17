# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
# 在本题中，匹配是指字符串的所有字符匹配整个模式。
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配




# 动态规划，第一遍不会
class Solution:
    def match(self , str , pattern ):
        # write code here
        len1,len2 = len(str),len(pattern)
        dp = [[False]*(len2+1) for _ in range(len1+1)]
        dp[0][0] = True #边界条件:对于[0][i]和[i][0]都认为是False，所以不需要单独赋值
        # 初始化首行
        for j in range(2, len2+1, 2):
            dp[0][j] = dp[0][j - 2] and pattern[j - 1] == '*'
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                #只需要关注True的传递即可，所以str[i]和pattern[j]不相等时不需要考虑
                if str[i-1] == pattern[j-1] or pattern[j-1] == ".":
                    dp[i][j] |= dp[i-1][j-1] #注意为了防止出问题，全部都用|=
                if pattern[j-1] == "*":#还需要考虑前一个是都相等
                    if pattern[j-2] ==  str[i-1] or pattern[j-2] == ".":#这里认为*不会出现在pattern的第一个
                        dp[i][j] |= dp[i][j-2] #取消前一个
                        dp[i][j] |= dp[i][j-1] #乘1
                        dp[i][j] |= dp[i-1][j] #乘n个（n≥2），j不能减只能i减
                    else:#不相等的情况只能取消，是j-2而不是j-1
                        dp[i][j] |= dp[i][j-2]
        return dp[len1][len2]
