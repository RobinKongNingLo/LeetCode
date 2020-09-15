#time: 20ms 99.93% space: 14MB 22.51%
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                num_of_1 = 0
                for offset_i, offset_j in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0) , (1,1)]:
                    new_i = offset_i + i
                    new_j = offset_j + j
                    if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and board[new_i][new_j] > 0:
                        num_of_1 += 1
                if board[i][j] and (num_of_1 < 2 or num_of_1 > 3): #If current cell is live and the cell will die
                    board[i][j] = 2 #denote live to die as 2
                elif board[i][j] == 0 and num_of_1 == 3: #If current cell is dead and it will live
                    board[i][j] = -1 #denote die to live as -1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1