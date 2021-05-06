# 给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。

# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。


# 直接用split()函数
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            arr = s.split()
            if len(arr) == 0:
                return 0
            else:
                return len(arr[-1])
