# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。
# 你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 如果只有数字，直接返回
        if expression.isdigit():
            return [int(expression)]

        res = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res
