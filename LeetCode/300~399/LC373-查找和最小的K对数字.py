# 给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。

# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。

# 找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。

# 把所有和求出来然后排序
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        len_a , len_b = len(nums1), len(nums2)
        dic = {}
        #该索引是为了记录是该和是两个数组中的哪两个元素的坐标
        index = 0
        for i in nums1:
            for j in nums2:
                dic[index] = i + j
                index += 1
        dic = dict(sorted(dic.items(), key=lambda item: item[1]))
        # print(dic)
        result = []
        if k > len_a * len_b:
            k = len_a * len_b
        for key in dic.keys():
            #u在nums1中的位置
            i = key // len_b 
            #v在nums2中的位置
            j = key % len_b 
            result.append([nums1[i], nums2[j]])
            k -= 1
            if k == 0:
                break
        return result
