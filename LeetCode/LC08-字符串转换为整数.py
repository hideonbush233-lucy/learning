# 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

# 函数 myAtoi(string s) 的算法如下：

#     读入字符串并丢弃无用的前导空格
#     检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
#     读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
#     将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
#     如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
#     返回整数作为最终结果。

# 注意：

#     本题中的空白字符只包括空格字符 ' ' 。
#     除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。

# 利用正则表达式
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        import re
        at_oi_re = re.compile('^[ ]*([+-]?\d+)')
        if not at_oi_re.search(s):
            return 0
        res = int(at_oi_re.findall(s)[0])
        return min(max(res, -2 ** 31), 2 ** 31 - 1)

# 逐个判断，需要每一种情况都考虑好，比较费事  
class Solution:
  def myAtoi(self, s: str) -> int:
    if len(s) == 0:
        return 0

    nums = ['0','1','2','3','4','5','6','7','8','9']
    signs = ['+','-']
    res = ''
    flag = 1
    sflag = 0
    nflag = 0
    for char in s:
        if char == ' ':
            if nflag == 1 or sflag == 1:
                break
            if nflag == 0:
                continue
        if char in signs:
            if nflag == 1:
                break
            if sflag == 1:
                return 0

            if char == '+':
                sflag = 1
                flag = 1
                continue
            else:
                sflag = 1
                flag = -1
                continue
        elif char in nums:
            res += char
            nflag = 1
        else:
            break

    if nflag == 0:
        return  0
    if res == '':
        return 0
    return min(max(flag*int(res),-2**31),2**31-1)
