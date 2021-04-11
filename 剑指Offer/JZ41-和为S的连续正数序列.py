# 找出所有和为S的连续正数序列? Good Luck!
# 返回值描述:
# 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序


# 暴力搜索
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum == 0:
            return []
        res = []
        for i in range(1,tsum//2+1):  # 左端点
            for j in range(i+1,tsum):  # 右端点
                tmp = 0
                temp = []
                for k in range(i,j+1): # 区间长度 求和
                    tmp += k
                    temp.append(k)
                if tmp == tsum:
                    res.append(temp)
                elif tmp > tsum:
                    break
        return res
