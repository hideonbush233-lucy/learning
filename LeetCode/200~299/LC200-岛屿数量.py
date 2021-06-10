# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。


# 递归把相邻的1全清空为0
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def clear(i,j,m,n,seen):
            if 0<=i+1<m and grid[i+1][j] == '1' and not seen[i+1][j]:
                grid[i+1][j] = '0'
                seen[i+1][j] = True
                clear(i+1,j,m,n,seen)
                
            if 0<=j+1<n and grid[i][j+1] == '1' and not seen[i][j+1]:
                grid[i][j+1] = '0'
                seen[i][j+1] = True
                clear(i,j+1,m,n,seen)               
                
            if 0<=j-1<n and grid[i][j-1] == '1' and not seen[i][j-1]:
                grid[i][j-1] = '0'
                seen[i][j-1] = True
                clear(i,j-1,m,n,seen)
            if 0<=i-1<m and grid[i-1][j] == '1' and not seen[i-1][j]:
                grid[i-1][j] = '0'
                seen[i-1][j] = True
                clear(i-1,j,m,n,seen)
            return 

        m,n = len(grid),len(grid[0])
        seen = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    seen[i][j] = True
                    clear(i,j,m,n,seen)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
        return count
