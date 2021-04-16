# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。


# 笨方法，逐个考虑可能性，做好标志位，把所有情况考虑进去
class Solution:
    def isNumeric(self , str ):
        # write code here
        if not str:
            return False
        if str[-1] in ['e','E','+','-','.']:
            return False
        if str.count('.') > 1:
            return False
        signs = ['+','-']
        exs = ['e','E']
        nums = ['0','1','2','3','4','5','6','7','8','9']
        eflag = 0
        sflag = 0
        nflag = 0
        for char in str:
            if char not in nums and char not in exs and char not in signs and char != '.':
                return False
            if char in nums:
                nflag = 1
            if char in exs:
                if nflag == 0:
                    return False
                if eflag == 0:
                    eflag = 1
                else:
                    return False
            if eflag == 1:
                sflag = 0
            if char in signs:
                if sflag == 1:
                    return False
                else:
                    sflag = 1
            
            if char == '.' and eflag == 1:
                return False
        if sflag == 1 and str.find('+') != 0 and str.find('-') != 0:
            return False
        return True
      
      
# 直接用float    
class Solution:
    def isNumeric(self , str ):
        # write code here
        try:
            res = float(str)
            return True
        except:
            return False
