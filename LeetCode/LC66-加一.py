#给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

#最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

#你可以假设除了整数 0 之外，这个整数不会以零开头。


# 区分为9和非9的情况即可
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        elif digits[-1] == 9:
            digits[-1] = 0
            flag = 0
            for i in range(n-2,-1,-1):
                if digits[i] < 9:
                    digits[i] += 1
                    flag = 1
                    break
                else:
                    digits[i] = 0
            if  flag == 0:
                digits = [1] + digits
            return digits
