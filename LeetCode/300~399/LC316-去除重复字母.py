# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        from collections import Counter

        d = Counter(s)

        stack = []
        for i in s:
            d[i] -= 1
            if i in stack:
                continue
            while stack and stack[-1] > i and d[stack[-1]] > 0:
                    stack.pop()
                    
            stack.append(i)
            # print(stack)
        return ''.join(stack)
