# 给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

# 你可以假设所有输入数组都可以得到满足题目要求的结果。

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()  #首先排序
        lenth=len(nums)  #计算长度
        if lenth>2:  #如果长度小于等于2，就不用处理
            if lenth%2==0:  #由于长度为偶数和奇数是不一样的，我们需要分情况讨论
                l1=nums[0:int(lenth//2)]  #将排序后小的一般拿出来
                l1=l1[::-1]  #倒序排
                l2=nums[int(lenth//2):]  #将排序后大的拿出来
                l2=l2[::-1]
                l=[]  #这个用于存储值
                for i in range(len(l1)):
                    l.append(l1[i])
                    l.append(l2[i])
                nums[:] = l  #最后替换
            else:
                l1=nums[0:int(lenth//2+1)]
                l1=l1[::-1]
                l2=nums[int(lenth//2+1):]
                l2=l2[::-1]
                l=[]
                for i in range(len(l1)):
                    if i!=len(l1)-1:
                        l.append(l1[i])
                        l.append(l2[i])
                    else:
                        l.append(l1[i])
                nums[:] = l  #最后替换
