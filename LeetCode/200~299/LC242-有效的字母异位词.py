# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dic1 = {}
        for i in s:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        dic2 = {}
        for j in t:
            if j not in dic2:
                dic2[j] = 1
            else:
                dic2[j] += 1
        return dic1 == dic2
