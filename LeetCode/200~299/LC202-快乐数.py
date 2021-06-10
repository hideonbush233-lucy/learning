# 编写一个算法来判断一个数 n 是不是快乐数。

# 「快乐数」定义为：

#     对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
#     然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
#     如果 可以变为  1，那么这个数就是快乐数。

# 如果 n 是快乐数就返回 true ；不是，则返回 false 。

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def get_next(num):
            res = 0
            while num > 0:
                res += (num%10)**2
                num = num//10
            return res

        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = get_next(n)
        return False
