# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。


# 需要确定最短的字符串长度，while循环每个字符都与第一个字符串的字符比较即可，flag=1表明出现了不同字符
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        i = 0
        flag = 0
        if n == 0:
            return ''
        minlength = len(strs[0])
        for j in range(1,n):
            minlength = min(minlength,len(strs[j]))
        if minlength == 0:
            return ''
        while i < minlength:
            for j in range(1,n):
                if strs[0][i] != strs[j][i]:
                    flag = 1
                    break
            if flag == 1:
                break
            i += 1
        return strs[0][0:i]
