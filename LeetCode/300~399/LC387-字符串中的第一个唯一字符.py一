# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        if not s:
            return -1
        for i in range(n):
            if s[i] not in s[:i]+s[i+1:]:
                return i
        return -1
