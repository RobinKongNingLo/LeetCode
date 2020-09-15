class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'K'
                self.findNghd(i, 0, board)
            if board[i][n-1] == 'O':
                board[i][n-1] = 'K'
                self.findNghd(i, n-1, board)
        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = 'K'
                self.findNghd(0, j, board)
            if board[m-1][j] == 'O':
                board[m-1][j] = 'K'
                self.findNghd(m-1, j, board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'K':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
    
    def findNghd(self, i, j, board):
        if i-1 >= 0 and board[i-1][j] == 'O':
            board[i-1][j] = 'K'
            self.findNghd(i-1, j, board)
        if i+1 < len(board) and board[i+1][j] == 'O':
            board[i+1][j] = 'K'
            self.findNghd(i+1, j, board)
        if j-1 >= 0 and board[i][j-1] == 'O':
            board[i][j-1] = 'K'
            self.findNghd(i, j-1, board)
        if j+1 < len(board[0]) and board[i][j+1] == 'O':
            board[i][j+1] = 'K'
            self.findNghd(i, j+1, board)
            