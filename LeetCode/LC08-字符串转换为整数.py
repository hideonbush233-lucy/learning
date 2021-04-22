

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        import re
        at_oi_re = re.compile('^[ ]*([+-]?\d+)')
        if not at_oi_re.search(s):
            return 0
        res = int(at_oi_re.findall(s)[0])
        return min(max(res, -2 ** 31), 2 ** 31 - 1)
