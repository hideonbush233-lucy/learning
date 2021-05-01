#  请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
#   如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
#   例如 [abcesfcsadee]\begin{bmatrix} a & b & c &e \\ s & f & c & s \\ a & d & e& e\\ \end{bmatrix}\quad⎣⎡​asa​bfd​cce​ese​⎦⎤​ 
#   矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。 


class Solution:
    def hasPath(self , matrix , word ):
        # write code here
        def dfs(i,j,k):
            if not 0<=i<len(matrix) or not 0<=j<len(matrix[0]) or matrix[i][j] != word[k]:
                return False
            if len(word) - 1 == k:
                return True
            matrix[i][j] = ''
            res = dfs(i+1,j,k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
            matrix[i][j] = word[k]
            return res
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dfs(i,j,k=0):
                    return True
        return False
