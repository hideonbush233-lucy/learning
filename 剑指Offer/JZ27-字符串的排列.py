# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。


# 递归法 值得好好揣摩，逐个固定，其余的作为新的字符串进行迭代
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) < 2:
            return [ss]
        res = set()
        
        for i in range(0,len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                res.add(ss[i]+j)
        return sorted(res)
