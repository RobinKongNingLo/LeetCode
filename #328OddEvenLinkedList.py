class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        self.board = [[0]*len(matrix[0])]*len(matrix)
        self.matrix = matrix
        max_length = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.board[i][j]:
                    max_length = max(max_length, self.board[i][j])
                else:
                    max_length = max(max_length, self.dfs(i, j))
                
        return max_length
            
    def dfs(self, i, j):
        tmp_max = 1
        if i-1 >= 0 and self.matrix[i-1][j] > self.matrix[i][j]: #upper
            if self.board[i-1][j]: #(i-1,j) is visited
                tmp_max = max(tmp_max, self.board[i-1][j] + 1)
            else:
                tmp_max = max(tmp_max, self.dfs(i-1, j) + 1)
                
        if i+1 < len(self.matrix) and self.matrix[i+1][j] > self.matrix[i][j]: #lower
            if self.board[i+1][j]: #(i+1,j) is visited
                tmp_max = max(tmp_max, self.board[i+1][j] + 1)
            else:
                tmp_max = max(tmp_max, self.dfs(i+1, j) + 1)
                
        if j-1 >= 0 and self.matrix[i][j-1] > self.matrix[i][j]: #left
            if self.board[i][j-1]: #(i,j-1) is visited
                tmp_max = max(tmp_max, self.board[i][j-1] + 1)
            else:
                tmp_max = max(tmp_max, self.dfs(i, j-1) + 1)
                
        if j+1 < len(self.matrix[0]) and self.matrix[i][j+1] > self.matrix[i][j]: #right
            if self.board[i][j+1]: #(i,j+1) is visited
                tmp_max = max(tmp_max, self.board[i][j+1] + 1)
            else:
                tmp_max = max(tmp_max, self.dfs(i, j+1) + 1)
        
        self.board[i][j] = tmp_max
        return tmp_max