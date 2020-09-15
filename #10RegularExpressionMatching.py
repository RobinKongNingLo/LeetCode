class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #Initialize boolean table T
        s = ' ' + s
        p = ' ' + p
        T = [[0]*len(p) for i in range(len(s))]
        T[0][0] = 1
        
        #e.g. match empty string with "a*"
        for j in range(1,len(p)):
            if p[j] == '*':
                T[0][j] = T[0][j-2]
        
        for i in range(1,len(s)):
            for j in range(1,len(p)):
                if p[j] == s[i] or p[j] == '.':
                    T[i][j] = T[i-1][j-1]
                elif p[j] == '*':
                    T[i][j] = T[i][j-2]
                    if s[i] == p[j-1] or p[j-1] == '.':
                        T[i][j] = T[i][j] + T[i-1][j]
        
        return T[-1][-1]
                        