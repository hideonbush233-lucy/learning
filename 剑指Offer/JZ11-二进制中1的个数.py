# 有点难想到，对于位运算还不太熟
# 直接辗转除法取余会超时

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = n & 0xffffffff
        res = 0
        while(n != 0 ):
            res += 1
            n = (n-1)&n
        return res
