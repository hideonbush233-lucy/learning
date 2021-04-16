#  在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

# 对于50%50\%50%的数据,size≤104size\leq 10^4size≤104
# 对于75%75\%75%的数据,size≤105size\leq 10^5size≤105
# 对于100%100\%100%的数据,size≤2∗105size\leq 2*10^5size≤2∗105


# 暴力破解，但对于10^5数据，O(N^2)算法超时
class Solution:
    def InversePairs(self, data):
        # write code here
        res = 0
        for i in range(len(data)-1):
            for j in range(i+1,len(data)):
                if data[i] > data[j]:
                    res += 1
        return res%1000000007

   
# 再推导推导
class Solution:
    def InversePairs(self, data):
        # write code here
        def merge(data, start, mid, end, temp):
            cnt = 0
            i = start
            j = mid + 1
            k = start
            while i <= mid and j <= end:  # data[start...1...mid]  data[mid+1...j...end]
                if data[j] < data[i]:
                    temp[k] = data[j]
                    cnt += j - k
                    j += 1
                    k += 1
                else:
                    temp[k] = data[i]
                    i += 1
                    k += 1
            while i <= mid:
                temp[k] = data[i]
                i += 1
                k += 1
            while j <= end:
                temp[k] = data[j]
                j += 1
                k += 1
            data[start:end+1] = temp[start:end+1]
            return cnt
         
        def divide(data, start, end, temp):
            cnt = 0
            if start < end:
                mid = (start + end) // 2
                cnt += divide(data, start, mid, temp)
                cnt += divide(data, mid+1, end, temp)
                cnt += merge(data, start, mid, end, temp)
            return cnt
         
        temp = data[:]
        count = divide(data, 0, len(data)-1, temp)
        return count % 1000000007
