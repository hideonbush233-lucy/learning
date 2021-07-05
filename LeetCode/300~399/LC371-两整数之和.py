# 不使用运算符 + 和 - ，计算两整数a 、b之和。


# 异或 不带进位的求和
# 进位结果使用与运算和移位运算
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1 
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
