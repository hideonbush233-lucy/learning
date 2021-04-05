# 将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
# 输入描述:
# 输入一个字符串,包括数字字母符号,可以为空
# 返回值描述:
# 如果是合法的数值表达则返回该数字，否则返回0


# 利用一个数字列表将每一个字符转换为对应的数字，借助index（）
# 计算数的方法 循环 res = 10 * res + num 重要 !!!
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s) == 0:
            return 0
        else:
            nums = ['0','1','2','3','4','5','6','7','8','9']
            res = 0
            flag = 1
            for item in s:
                if item == '+':
                    flag = 1
                elif item == '-':
                    flag = -1
                elif item in nums:
                    res = 10*res + nums.index(item)
                else:
                    return 0
            return flag*res
