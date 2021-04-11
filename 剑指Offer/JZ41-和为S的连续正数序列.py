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

# 滑动窗口法
# 首先是一个窗口，既然是一个窗口，就需要用窗口的左边界i和右边界j来唯一表示一个窗口，其次，滑动代表，窗口始终从左往右移动，这也表明左边界i和右边界j始终会往后移动，而不会往左移动。

#     初始化，i=1,j=1, 表示窗口大小为0
#     如果窗口中值的和小于目标值tsum， 表示需要扩大窗口，j += 1
#     否则，如果窗口值和大于目标值tsum，表示需要缩小窗口，i += 1
#     否则，等于目标值，存结果，缩小窗口，继续进行步骤2,3,4 
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum == 0:
            return []
        elif tsum == 1:
            return []
        l = r = 1
        res = []
        tmp = 0
        while l <= tsum//2+1:
            if tmp < tsum:
                tmp += r
                r += 1
            elif tmp > tsum:
                tmp -= l
                l += 1
            else:
                temp = []
                for k in range(l,r):
                    temp.append(k)
                res.append(temp)
                tmp -= l
                l += 1
        return res
