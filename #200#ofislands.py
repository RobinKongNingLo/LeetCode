class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.findNghd(i, j, grid)
                    ans += 1
        return ans
                
    def findNghd(self, i, j, board):
        if i-1 >= 0 and board[i-1][j] == '1':
            board[i-1][j] = 'K'
            self.findNghd(i-1, j, board)
        if i+1 < len(board) and board[i+1][j] == '1':
            board[i+1][j] = 'K'
            self.findNghd(i+1, j, board)
        if j-1 >= 0 and board[i][j-1] == '1':
            board[i][j-1] = 'K'
            self.findNghd(i, j-1, board)
        if j+1 < len(board[0]) and board[i][j+1] == '1':
            board[i][j+1] = 'K'
            self.findNghd(i, j+1, board)