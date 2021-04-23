

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
