# 一个整型数组里除了两个数字只出现一次，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

# 投机取巧的方法 直接用count()函数
class Solution:
    def FindNumsAppearOnce(self , array ):
        # write code here
        res = []
        for item in array:
            if array.count(item) == 1:
                res.append(item)
        return sorted(res)
    
    
    
    class Solution:
    def FindNumsAppearOnce(self , array ):
        # write code here
        res = []
        for item  in array:
            if item in res:
                res.remove(item)
            else:
                res.append(item)
        return sorted(res)
      
  
