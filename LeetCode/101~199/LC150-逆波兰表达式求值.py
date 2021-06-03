# 根据 逆波兰表示法，求表达式的值。

# 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

 

# 说明：

#     整数除法只保留整数部分。
#     给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        n = len(tokens)
        nums = []
        sign = ['+','-','*','/']
        for i in range(n):
            if tokens[i] not in sign:
                nums.append(int(tokens[i]))
            else:
                a = nums.pop()
                b = nums.pop()
                if tokens[i] == '+':
                    a = a+b
                    nums.append(a)
                elif tokens[i] == '-':
                    a = b-a
                    nums.append(a)
                elif tokens[i] == '*':
                    a = a*b
                    nums.append(a)
                elif tokens[i] == '/':
                    a = int(b/a)
                    nums.append(a)
        return nums[-1]
