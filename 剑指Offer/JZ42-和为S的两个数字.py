# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。


# 先把和为tsum的数存到一个数组中，然后遍历找乘积最小的一组，排序输出
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res = []
        for item in array:
            if tsum-item in array:
                res.append(item)
        if len(res) == 0:
            return []
        mins = 0
        for i in range(1,len(res)):
            if res[i]*(tsum-res[i]) < res[mins]*(tsum-res[mins]):
                mins = i
        return sorted([res[i],tsum-res[i]])
