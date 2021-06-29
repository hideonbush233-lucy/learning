# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        slist = s.split(' ')
        seen = []
        if len(pattern) != len(slist):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if slist[i] in seen:
                    return False
                dic[pattern[i]] = slist[i]
                seen.append(slist[i])
            else:
                if dic[pattern[i]] != slist[i]:
                    return False
        return True
