# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）

# 把字符串分割为列表，然后利用count()函数
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) == 0:
            return -1
        res = []
        for char in s:
            res.append(char)
        for i in range(len(res)):
            if res.count(res[i]) == 1:
                return i
        return -1
