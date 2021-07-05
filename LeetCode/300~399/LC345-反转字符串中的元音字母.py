# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = []
        for ss in s:
            ans.append(ss)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        i,j = 0,len(s)-1
        # ans=['0']*len(s)
        while i<j:
            while s[i] not in vowels:
                ans[i] = s[i]
                i+=1
                if i>=len(s):
                    return ''.join(ans)
            while s[j] not in vowels:
                ans[j] = s[j]
                j-=1
                if j<0:
                    return ''.join(ans)
            ans[i],ans[j] = s[j],s[i]
            i+=1
            j-=1
        return ''.join(ans)
