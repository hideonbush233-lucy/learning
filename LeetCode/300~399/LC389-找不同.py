# 给定两个字符串 s 和 t，它们只包含小写字母。

# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

# 请找出在 t 中被添加的字母。

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        for j in t:
            if j not in dic:
                return j
            else:
                dic[j] -= 1
            if dic[j] == -1:
                return j
