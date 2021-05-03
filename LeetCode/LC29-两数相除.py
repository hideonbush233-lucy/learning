# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

# 返回被除数 dividend 除以除数 divisor 得到的商。

# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2


# 位运算，还要再学习
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a=2**31
        flag = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        result = 0
        while dividend>=divisor:
            count+=1
            divisor <<= 1
        while count>0:
            count-=1
            divisor >>= 1
            if dividend>=divisor:
                result += 1<<count
                dividend -= divisor
        if flag: result=-result
        if -a<=result<=a-1:
            return result
        else:return a-1
