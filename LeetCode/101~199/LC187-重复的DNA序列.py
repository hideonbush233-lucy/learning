# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # n = len(s)
        # if n<=10:
        #     return []
        # ans = []
        # for i in range(n-10):
        #     res = s[i:i+10]
        #     if res in s[i+1:] and res not in ans:
        #         ans.append(res)
        # return ans
        L, n = 10, len(s)     
        seen, output = set(), set()

        # iterate over all sequences of length L
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return list(output)
