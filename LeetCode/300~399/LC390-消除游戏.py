# 给定一个从1 到 n 排序的整数列表。
# 首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。
# 第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。
# 我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
# 返回长度为 n 的列表中，最后剩下的数字。


class Solution:
    def lastRemaining(self, n: int) -> int:
      # 暴力超时
        # arr = [ _ for _ in range(1,n+1)]
        # level = 0
        # while  len(arr)>1:
        #     if level%2==0:
        #         for i in range(0,len(arr),1):
        #             if i < len(arr):
        #                 # print(arr[i])
        #                 arr.pop(i)
                        
        #     else:
        #         for i in range(len(arr)-1,-1,-2):
        #             # print(arr[i])
        #             arr.pop(i)
        #     level += 1
        # return arr[-1]
        return 1 if n==1 else 2*(n//2+1-self.lastRemaining(n//2))
