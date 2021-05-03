# 给定一个正整数 n ，输出外观数列的第 n 项。

# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

# 你可以将其视作是由递归公式定义的数字字符串序列：

#     countAndSay(1) = "1"
#     countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。


# 动态规划
class Solution:
    def countAndSay(self, n: int) -> str:
        dp = ['','1','11']
        for i in range(3,n+1):
            temp = dp[i-1]
            res = ''
            j = 1
            char = temp[0]
            num = 1
            while j < len(temp):
                if temp[j] == char:
                    num += 1
                    j += 1
                else:
                    res += str(num)+char
                    char = temp[j]
                    num = 1
                    j += 1
            res += str(num)+char
            dp.append(res)
        return dp[n]
