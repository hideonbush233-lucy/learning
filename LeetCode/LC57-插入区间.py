# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。


# 类似于上一题，直接把新区间加进来就好
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        ans = []
        for item in intervals:
            if not ans or ans[-1][1] < item[0]:
                ans.append(item)
            else:
                ans[-1][1] = max(ans[-1][1],item[1])
        return ans
