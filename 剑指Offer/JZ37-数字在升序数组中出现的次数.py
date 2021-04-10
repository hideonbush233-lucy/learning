# 统计一个数字在升序数组中出现的次数。

# 直接用count()函数
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
            if not data:
                return 0
            return data.count(k)
          
          
#遍历搜索
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
            if not data:
                return 0
            count = 0
            for item in data:
                if item == k:
                    count += 1
            return  count
