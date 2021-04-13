# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

# 直接利用count()函数
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0
        for item in numbers:
            if numbers.count(item) > len(numbers)/2:
                return item
        return 0
