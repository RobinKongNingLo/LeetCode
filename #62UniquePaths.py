class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1]*m]+ [([1] + [0]*(m-1)) for i in range(n-1)]
        for i in range(1,n):
            for j in range(1,m):
                table[i][j] = table[i][j-1] + table[i-1][j]
        
        return table[-1][-1]