# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
# 不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
# 对于A长度为1的情况，B无意义，故而无法构建，因此该情况不会存在。 


# 构建一个函数返回指定位置的乘积
class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        res = []
        for i in range(n):
            res.append(self.func(A,i))
        return res
    def func(self,nums,pos):
        tmp = 1
        if pos == 0:
            for j in range(1,len(nums)):
                tmp *= nums[j]
            return tmp
        if pos == len(nums)-1:
            for j in range(len(nums)-1):
                tmp *= nums[j]
            return tmp
        else:
            for j in range(pos):
                tmp *= nums[j]
            for j in range(pos+1,len(nums)):
                tmp *= nums[j]
            return tmp
