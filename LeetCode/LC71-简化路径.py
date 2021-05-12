

# 利用栈
# 先利用split()分割
class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        res,i = [],0
        while i<len(l):
            if l[i]=='..':
                if res: res.pop()
            elif l[i]!='.' and l[i]!='':
                res.append(l[i])
            i+=1
        return '/'+'/'.join(res)
