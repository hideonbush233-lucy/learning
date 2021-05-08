# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # 必须先按照左区间排序
        new_arr = []
        for item in intervals:
            if not new_arr or new_arr[-1][1] < item[0]:
                new_arr.append(item)
            else:
                new_arr[-1][1] = max(new_arr[-1][1],item[1])  # 合并区间
        return new_arr
