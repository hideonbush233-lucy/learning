# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

# 利用栈，出现]就一直出栈
class Solution:
    def decodeString(self, s: str) -> str:
        nums=[]
        n=len(s)
        stack=[]
        num=0
        for i in range(n):
            if s[i].isdigit():
                num = 10*num+int(s[i])
                continue
            if num!=0:
                nums.append(num)
                num=0
            if s[i]==']':
                temp=''
                
                while stack[-1]!='[':
                    temp = stack.pop()+temp
                stack.pop()
                times = nums.pop()
                temp = times*temp
                for j in range(len(temp)):
                    stack.append(temp[j])
            else:
               stack.append(s[i])
        return ''.join(stack)
