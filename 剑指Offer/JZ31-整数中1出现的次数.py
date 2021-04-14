# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数
# 例如，1~13中包含1的数字有1、10、11、12、13因此共出现6次


# 效率很低的方法，逐个算1的个数，然后加起来即可
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 1:
            return 0
        res = 0
        for i in range(1,n+1):
            res = res + numcount(i)
        return res
        
def numcount(num):
    count = 0
    while num > 0:
        temp = num%10
        if temp == 1:
            count += 1
        num = num//10
    return count


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 1:
            return 0
        res = 0
        m = 1
        while m<=n:
            a = n//m
            b = n%m
            res += (a+8)//10*m+(a%10==1)*(b+1)
            m *= 10
        return res
