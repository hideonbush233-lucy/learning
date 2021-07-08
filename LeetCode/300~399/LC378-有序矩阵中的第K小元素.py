# 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m,n = len(matrix),len(matrix[0])
        ans = []
        for i in range(m):
            for j in range(n):
                ans.append(matrix[i][j])
        ans.sort()
        return ans[k-1]
