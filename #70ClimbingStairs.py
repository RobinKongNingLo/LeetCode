class Solution:
    def climbStairs(self, n: int) -> int:
        table = [1, 1] + [0]*(n-1)
        for i in range(2, len(table)):
            table[i] = table[i-1] + table[i-2]
        
        return table[-1]