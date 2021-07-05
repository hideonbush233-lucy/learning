# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        ans = sorted(dic.items(),key=lambda kv:(kv[1]))
        # print(ans)
        res = []
        n=len(res)
        for j in range(k):
            res.append(ans[n-1-j][0])
        return res[::-1]
