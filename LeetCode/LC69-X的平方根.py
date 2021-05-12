# 实现 int sqrt(int x) 函数。

# 计算并返回 x 的平方根，其中 x 是非负整数。

# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。


class Solution:
    def mySqrt(self, x: int) -> int:
        # 采用指数对数转换，貌似这种做法不好
        # if x == 0:
        #     return 0
        # ans = int(math.exp(0.5 * math.log(x)))
        # return ans + 1 if (ans + 1) ** 2 <= x else ans

        # 二分法
        if x == 0:
            return 0
        left = 1
        right = x
        while left < right:
            mid = (left+right)//2
            if right - left == 1:
                break
            if mid**2 > x:
                right = mid
            elif mid** 2 == x:
                return mid
            else:
                left = mid
        return left
