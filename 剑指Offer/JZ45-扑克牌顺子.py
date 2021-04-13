# 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

# 把0剔除来，记录0的次数，排序，然后逐个遍历看是否满足递增
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) == 0:
            return False
        count = numbers.count(0)
        for j in range(count):
            numbers.remove(0)
        numbers = sorted(numbers)
        flag = 0
        res = numbers[0]
        for i in range(1,len(numbers)):
            if numbers[i] == res + 1:
                res = numbers[i]
            else:
                if 0 < numbers[i] - res -1 <= count and count > 0:
                    count -= (numbers[i] - res - 1)
                    res = numbers[i]
                else:
                    flag = 1
                    return False
        return True
