# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0'
