# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x &= (x - 1) # 通过该方法把二进制的最后一个1转换为0
                ones += 1
            return ones
        
        bits = [countOnes(i) for i in range(n + 1)]
        return bits
