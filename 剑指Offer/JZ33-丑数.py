# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。


# 根据丑数定义，丑数应该是每一个丑数乘以2,3或5的结果。因此以第一个丑数1分别乘以2,3或5取最小值为下一个丑数，每一个丑数都是前面丑数乘以2,3,5得到。
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
            return index
        res = [1]*index
        pos2 = pos3 = pos5 = 0
        for i in range(1,index):
            tmp = min(res[pos2]*2,res[pos3]*3,res[pos5]*5)
            res[i] = tmp
            if res[i] == res[pos2]*2:
                pos2 += 1
            if res[i] == res[pos3]*3:
                pos3 += 1
            if res[i] == res[pos5]*5:
                pos5 += 1
        return res[index-1]
