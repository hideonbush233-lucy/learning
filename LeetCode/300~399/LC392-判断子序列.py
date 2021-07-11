# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

# 进阶：

# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？


# 递归
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1=len(s)
        n2=len(t)
        if n1>n2:
            return False
        for i in range(n1):
            if s[i] not in t:
                return False
                
        def check(s1,s2):
            if len(s1)>len(s2):
                return False
            if not s1:
                return True
            if s1[0] not in s2:
                return False
            for j in range(len(s2)):
                if s2[j] ==s1[0]:
                    return check(s1[1:],s2[j+1:])
        return check(s,t)
