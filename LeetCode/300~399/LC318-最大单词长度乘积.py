# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0




class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def check(s1,s2):
            for s in s1:
                if s in s2:
                    return False
            return True
            
        n = len(words)
        ans = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if check(words[i],words[j]):
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans
