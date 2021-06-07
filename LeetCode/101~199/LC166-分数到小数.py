# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

# 如果小数部分为循环小数，则将循环的部分括在括号内。

# 如果存在多个答案，只需返回 任意一个 。

# 对于所有给定的输入，保证 答案字符串的长度小于 104 。


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0): #正负号判断，异或
            res.append("-")

        numer = abs(numerator)      #取整
        denomin = abs(denominator)

        a, remaind = divmod(numer, denomin)
        res.append(str(a))
        if remaind == 0:            #整除，直接返回
            return "".join(res)

        res.append(".")             #添加小数点
        dic = {}
        while remaind != 0:
            if remaind in dic:      #如果有循环，添加括号
                res.insert(dic[remaind], "(")
                res.append(")")
                break
            
            dic[remaind] = len(res) #记录括号的位置
            remaind *= 10           #余数加0，继续除法
            a, remaind = divmod(remaind, denomin)
            res.append(str(a))

        return "".join(res)
