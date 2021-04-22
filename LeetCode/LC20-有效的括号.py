# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

#     左括号必须用相同类型的右括号闭合。
#     左括号必须以正确的顺序闭合


# 利用栈的特性，当检测到右括号时，栈顶必须为对应的左括号
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 == 1:
            return False
        stack = []
        dict = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if char in dict:
                if not stack or stack[-1] != dict[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
