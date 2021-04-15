# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。


# 贪心，自定义排序 
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        res = []
        if len(numbers) == 0:
            return ''
        if len(numbers) == 1:
            return numbers[0]
        compare = lambda n1,n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
        array = sorted(numbers,cmp = compare)
        return ''.join([str(i) for i in array])

    
r# 定义一个函数实现全排列，然后把字符转换为数字，排序得到最小数
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        n = len(numbers)
        if len(numbers) == 0:
            return ''
        if len(numbers) == 1:
            return numbers[0]
        res = permutation(numbers)
        new_res = []
        for i in range(len(res)):
            tmp = int(''.join(str(num) for num in res[i]))
            new_res.append(tmp)
        new_res = sorted(new_res)
        return new_res[0]
        
def permutation(nums):
    if len(nums) <= 1:
        return [nums]
    r = []
    for i in range(len(nums)):
        s = nums[:i] + nums[i+1:]
        p = permutation(s)
        for x in p:
            r.append(nums[i:i+1]+x)
    return r
