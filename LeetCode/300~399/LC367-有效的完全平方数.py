# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

# 进阶：不要 使用任何内置的库函数，如  sqrt 。

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        nums = []
        i = 1
        while i**2 <= num:
            nums.append(i**2)
            i+=1
        if nums[-1] == num:
            return True
        else:
            return False
