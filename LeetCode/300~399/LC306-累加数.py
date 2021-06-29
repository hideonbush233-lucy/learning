# 累加数是一个字符串，组成它的数字可以形成累加序列。

# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) == 0:
            return True

        n = len(num)
        if n < 3:
            return False

        def check(p1, p2, j):
            while j < n:
                p = str(int(p1) + int(p2)) # 前两个数知道了那么第三个也能确定，直接去比较同样位置上的数
                if num[j: j+len(p)] != p:
                    return False
                j += len(p)
                p1, p2 = p2, p
            return True


        for i in range(1, n//2+1) if num[0] != "0" else [1]:
            for j in range(i+1, n) if num[i] != "0" else [i+1]:
                p1 = num[:i]
                p2 = num[i:j]
                if check(p1, p2, j):
                    return True
        return False
