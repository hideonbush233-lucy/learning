# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

#     I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
#     X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
#     C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。


# 因为数字范围已经确定了，就直接逐个向下确定转换后的值，
class Solution:
    def intToRoman(self, num: int) -> str:
        n = len(str(num))
        res = ''
        num = str(num)
        if n == 4:
            res += 'M'*int(num[0])
            num = num[1:]
            n = len(num)
        if n == 3:
            if num[0] == '4':
                res += 'CD'
                num = num[1:]
                n = len(num)
                
            elif num[0] == '9':
                res += 'CM'
                num = num[1:]
                n = len(num)
            else:
                tmp = int(num[0])
                if tmp >= 5:
                    res += 'D'
                    tmp -= 5
                res += 'C'*tmp
                num = num[1:]
                n = len(num)
        if n == 2:
            if num[0] == '4':
                res += 'XL'
                num = num[1:]
                n = len(num)
            elif num[0] == '9':
                res += 'XC'
                num = num[1:]
                n = len(num)
            else:
                tmp = int(num[0])
                if tmp >= 5:
                    res += 'L'
                    tmp -= 5
                res += 'X'*tmp
                num = num[1:]
                n = len(num)
        if n == 1:
            if num[0] == '0':
                return res
            elif num[0] == '4':
                res += 'IV'
                return res
            elif num[0] == '9':
                res += 'IX'
                return res
            else:
                tmp = int(num[0])
                if tmp >= 5:
                    res += 'V'
                    tmp -= 5
                res += 'I'*tmp
                return res
