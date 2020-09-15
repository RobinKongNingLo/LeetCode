class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Row:
        for j in range(0,9):
            dict = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
            for i in range(0,9):
                entry = board[j][i]
                if entry == '.':
                    continue
                elif dict[entry] == 1: 
                    return False
                elif dict[entry] == 0:
                    dict[entry] = 1
                
        #Column:
        for j in range(0,9):
            dict = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
            for i in range(0,9):
                entry = board[i][j]
                if entry == '.':
                    continue
                elif dict[entry] == 1: 
                    return False
                elif dict[entry] == 0:
                    dict[entry] = 1
        
        #Sub-box:
        for j in range(0,3):
            for i in range(0,3):
                dict = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
                for m in range(0,3):
                    for n in range(0,3):
                        entry = board[3*j + m][3*i + n]
                        if entry == '.':
                            continue
                        elif dict[entry] == 1: 
                            return False
                        elif dict[entry] == 0:
                            dict[entry] = 1
        return True